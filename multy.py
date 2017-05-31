import multiprocessing
from time import sleep

def worker():
    """worker function"""
    while True:
    	print("Hello")
    # return

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
        # jobs.append(p)
    p.start()
    sleep(2)
    p.terminate()
    p.join()
    p.start()
    sleep(2)
    p.terminate()
    p.join()
    