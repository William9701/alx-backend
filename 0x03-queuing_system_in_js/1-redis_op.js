import redis from "redis";

// Create a Redis client
const client = redis.createClient();

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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting value for ${schoolName}: ${err.message}`);
    } else {
      redis.print(`Reply: ${reply}`);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err.message}`);
    } else if (value === null) {
      console.log(`No value found for ${schoolName}.`);
    } else {
      redis.print(`${value}`);
    }
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
