import random, time, queue
from multiprocessing.managers import BaseManager

# queue for sending tasks
task_queue = queue.Queue()
# queue for receiving tasks
result_queue = queue.Queue()


# create QueueManager inherit from BaseManager
class QueueManager(BaseManager):
    pass


# register both queues onto network, assign queue objects to callable parameter
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def run():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # bind port 5000, set authentication key abc
    manager = QueueManager(address=('10.128.200.46', 80), authkey=b'abc')
    # start queue
    manager.start()
    # get queue objects from network
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # put some tasks into queue
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # read from result queue
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=60)
        print('Result: %s' % r)
    # Close
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    run()