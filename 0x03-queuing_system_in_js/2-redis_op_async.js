import redis from "redis";
import { promisify } from "util";

// Create a Redis client
const client = redis.createClient();

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Event listener for successful connection
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// Event listener for connection error
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Close the Redis connection when the script ends (optional)
process.on("exit", () => {
  client.quit();
});

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting value for ${schoolName}: ${err.message}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

// Async function to display the value for a given school
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    if (value === null) {
      console.log(`No value found for ${schoolName}.`);
    } else {
      console.log(`${value}`);
    }
  } catch (error) {
    console.error(`Error getting value for ${schoolName}: ${error.message}`);
  }
}

// Example usage
async function example() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
}

example();
