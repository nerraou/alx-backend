import { createClient } from 'redis';

const client = createClient();

const HOLBERTON_SCHOOL_CHANNEL = 'holberton school channel';

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(
    `Redis client not connected to the server: Error: ${error.message}`,
  );
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log('About to send', message);
    client.publish(HOLBERTON_SCHOOL_CHANNEL, message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
