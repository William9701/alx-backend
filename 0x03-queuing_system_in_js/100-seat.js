import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = promisify(client.get).bind(client);

reserveSeat(50);

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats('available_seats');
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.error(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  const availableSeats = await getCurrentAvailableSeats('available_seats');
  if (availableSeats > 0) {
    const newAvailableSeats = availableSeats - 1;
    reserveSeat(newAvailableSeats);
    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }
    queue.process('reserve_seat', async (job, done) => {
      if (newAvailableSeats >= 0) {
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    });
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});