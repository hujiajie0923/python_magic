import threading
import time


def thread_decorator(func):
    def wrapper(*args):
        threads = []
        print('start thread time: ', time.ctime())

        # calculate the args count
        loops = range(len(args))

        # insert all threads to thread list
        for i in args:
            t = threading.Thread(target=func, args=(i,))
            threads.append(t)

        # start all threads
        for i in loops:
            threads[i].start()

        # waiting all thread close
        for i in loops:
            threads[i].join()

        print('thread all done: ', time.ctime())
    return wrapper


@thread_decorator
def loop(sleep):
    print('start {} loop: '.format(sleep), time.ctime())
    time.sleep(sleep)
    print('loop {} done: '.format(sleep), time.ctime())


if __name__ == '__main__':
    loop(4, 5, 3)
