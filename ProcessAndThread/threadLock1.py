import time, threading


# assume this is your back balance:
balance = 0


def change_it(n):
    # deposit money at first and then withdraw, the balance should be zero
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)