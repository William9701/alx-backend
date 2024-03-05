import kue from "kue";

// Step 1: Create a queue with Kue
const queue = kue.createQueue();

// Step 2: Create an object containing the Job data
const jobData = {
  phoneNumber: "1234567890",
  message: "This is the code to verify your account",
};

// Step 3: Create a queue named push_notification_code and create a job
const job = queue.create("push_notification_code", jobData);

// Event listener for successful job creation
job.on("enqueue", (id, type) => {
  console.log(`Notification job created: ${job.id}`);
});

// Event listener for job failure
job.on("failed", (err) => {
  console.error(`Notification job failed: ${err}`);
});

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error(`Error creating Notification job: ${err}`);
    process.exit(1);
  }
});
