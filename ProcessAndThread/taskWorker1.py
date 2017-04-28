import time, sys, queue
from multiprocessing.managers import BaseManager


# create similar queue manager
class QueueManager(BaseManager):
    pass

# because this is getting queue from network, only provide names when registering
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# connect to server
server_addr = '10.128.200.46'
print('Connect to server %s...' % server_addr)
# port and authentication key should be identical with master
m = QueueManager(address=(server_addr, 80), authkey=b'abc')
# connect through network
m.connect()
# get queue objects from queue
task = m.get_task_queue()
result = m.get_result_queue()
# get tasks from queue and put results into another queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# close
print('worker exit.')
