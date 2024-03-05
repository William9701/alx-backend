import redis from "redis";

const cliSub = redis.createClient();

cliSub.on("error", (error) => {
  console.log(`Redis cliSubent not connected to the server: ${error.message}`);
});

cliSub.on("connect", () => {
  console.log("Redis cliSubent connected to the server");
});

const CHANNEL = 'holberton school channel';

cliSub.subscribe(CHANNEL);

cliSub.on('message', (channel, message) => {
  if (channel === CHANNEL) console.log(message);
  if (message === 'KILL_SERVER') {
    cliSub.unsubscribe(CHANNEL);
    cliSub.quit();
  }
});