import { createClient } from 'redis';

const client = createClient();

const HOLBERTON_SCHOOL_CHANNEL = 'holberton school channel';
const KILL_COMMAND = 'KILL_SERVER';

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(
    `Redis client not connected to the server: Error: ${error.message}`,
  );
});

client.on('message', (channel, message) => {
  console.log(message);

  if (message === KILL_COMMAND) {
    client.unsubscribe(HOLBERTON_SCHOOL_CHANNEL);
    client.quit();
  }
});

client.subscribe(HOLBERTON_SCHOOL_CHANNEL);
