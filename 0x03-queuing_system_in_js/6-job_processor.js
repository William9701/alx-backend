import kue from "kue";

// Step 1: Create a queue with Kue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message ${message}`
  );
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
