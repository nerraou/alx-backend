import { createClient } from 'redis';

const client = createClient(1);

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(
    `Redis client not connected to the server: Error: ${error.message}`,
  );
});
