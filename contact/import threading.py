import threading
import time

NUM_PHILOSOPHERS = 4
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
eating_sem = threading.Semaphore(NUM_PHILOSOPHERS - 1)

def philosopher(index):
    while True:
        think(index)
        eat(index)

def think(index):
    print(f"Philosopher {index} is thinking.")
    time.sleep(1)

def eat(index):
    eating_sem.acquire()

    forks[index].acquire()
    forks[(index + 1) % NUM_PHILOSOPHERS].acquire()

    print(f"Philosopher {index} is eating.")
    time.sleep(2)

    forks[index].release()
    forks[(index + 1) % NUM_PHILOSOPHERS].release()

    eating_sem.release()

if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

    for philosopher_thread in philosophers:
        philosopher_thread.start()

    for philosopher_thread in philosophers:
        philosopher_thread.join()
