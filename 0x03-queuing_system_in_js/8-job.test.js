import kue from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('testing createPushNotificationsJobs failures', () => {
  it('invalid jobs array', () => {
    chai
      .expect(() => {
        createPushNotificationsJobs({}, queue);
      })
      .to.throw('Jobs is not an array');
  });
});

describe('testing createPushNotificationsJobs successes', () => {
  it('create jobs from list', () => {
    const list = [
      {
        phoneNumber: '4153518783',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518784',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    createPushNotificationsJobs(list, queue);

    chai.expect(queue.testMode.jobs.length).to.equal(2);
    chai
      .expect(queue.testMode.jobs[0].type)
      .to.equal('push_notification_code_3');
    chai.expect(queue.testMode.jobs[0].data).to.eql(list[0]);
  });
});
