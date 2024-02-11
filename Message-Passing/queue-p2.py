import multiprocessing
import time

def python2_process(queue):
    # Data to be shared
    shared_data = {"key": 1}

    # Put the data into the queue
    queue.put(shared_data)

if __name__ == '__main__':
    # Create a multiprocessing queue
    shared_queue = multiprocessing.Queue()

    # Start the Python 2 process
    process = multiprocessing.Process(target=python2_process, args=(shared_queue,))
    process.start()

    # Wait for the process to finish
    process.join()

    # Close the queue
    shared_queue.close()
    shared_queue.join_thread()