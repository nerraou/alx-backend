import express from 'express';
import { createClient } from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const redisClient = createClient();
const queue = kue.createQueue();

const AVAILABLE_SEATS_REDIS_KEY = 'available_seats';
const QUEUE_NAME = 'reserve_seat';

let reservationEnabled = true;

redisClient.getAsync = promisify(redisClient.get).bind(redisClient);
redisClient.setAsync = promisify(redisClient.set).bind(redisClient);

redisClient.on('ready', () => {
  redisClient.setAsync(AVAILABLE_SEATS_REDIS_KEY, 50);
});

function reserveSeat(value) {
  return redisClient.setAsync(AVAILABLE_SEATS_REDIS_KEY, value);
}

function getCurrentAvailableSeats() {
  return redisClient.getAsync(AVAILABLE_SEATS_REDIS_KEY);
}

app.get('/available_seats', async (request, response) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();

  response.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (request, response) => {
  if (!reservationEnabled) {
    response.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create(QUEUE_NAME, {}).save(() => {
    response.json({ status: 'Reservation in process' });
  });

  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);

    response.json({ status: 'Reservation failed' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
});

app.get('/process', (request, response) => {
  queue.process(QUEUE_NAME, async (job, done) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();

    if (!reservationEnabled) {
      done(new Error('Not enough seats available'));

      return;
    }

    await reserveSeat(numberOfAvailableSeats - 1);

    if (numberOfAvailableSeats === 1) {
      reservationEnabled = false;
      return;
    }

    done();
  });

  response.json({ status: 'Queue processing' });
});

const PORT = 1245;

app.listen(PORT, () => {
  console.log('listening on port:', PORT);
});
