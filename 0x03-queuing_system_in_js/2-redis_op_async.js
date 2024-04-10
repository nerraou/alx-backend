import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(
    `Redis client not connected to the server: Error: ${error.message}`,
  );
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);

  const value = await getAsync(schoolName);

  print(null, value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
