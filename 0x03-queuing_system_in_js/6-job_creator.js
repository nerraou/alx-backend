import kue from 'kue';

const queue = kue.createQueue();

const pushNotificationCodeJob = queue
  .create('push_notification_code', {
    phoneNumber: '0601020304',
    message: 'hello world',
  })
  .save(() => {
    console.log('Notification job created', pushNotificationCodeJob.id);
  });

pushNotificationCodeJob
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
