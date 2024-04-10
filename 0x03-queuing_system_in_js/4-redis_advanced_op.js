import { createClient, print } from 'redis';

const client = createClient();

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(
    `Redis client not connected to the server: Error: ${error.message}`,
  );
});

const HASH_KEY = 'HolbertonSchools';

client.hset(HASH_KEY, 'Portland', '50', print);
client.hset(HASH_KEY, 'Seattle', '80', print);
client.hset(HASH_KEY, 'New York', '20', print);
client.hset(HASH_KEY, 'Bogota', '20', print);
client.hset(HASH_KEY, 'Cali', '40', print);
client.hset(HASH_KEY, 'Paris', '2', print);

client.hgetall(HASH_KEY, (error, result) => {
  console.log(result);
});
