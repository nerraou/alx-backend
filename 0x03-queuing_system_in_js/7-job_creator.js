import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

jobs.forEach((data) => {
  const pushNotificationCodeJob = queue
    .create('push_notification_code_2', data)
    .save(() => {
      console.log('Notification job created', pushNotificationCodeJob.id);
    });

  pushNotificationCodeJob
    .on('complete', () => {
      console.log('Notification job', pushNotificationCodeJob.id, 'completed');
    })
    .on('failed', (error) => {
      console.log(
        'Notification job',
        pushNotificationCodeJob.id,
        `failed: ${error}`,
      );
    })
    .on('progress', (progress) => {
      console.log(
        'Notification job',
        `#${pushNotificationCodeJob.id}`,
        `${progress}%`,
        'complete',
      );
    });
});
