import multiprocessing
import time

def python3_process(queue):
    # Receive the data from the queue
    shared_data = queue.get()
    print("Python 3 Client: Received data:", shared_data)

if __name__ == '__main__':
    # Create a multiprocessing queue
    shared_queue = multiprocessing.Queue()

    # Start the Python 3 process
    process = multiprocessing.Process(target=python3_process, args=(shared_queue,))
    process.start()

    # Data to be shared
    shared_data = {"key": "value"}

    # Put the data into the queue
    shared_queue.put(shared_data)

    # Wait for the process to finish
    process.join()

    # Close the queue
    shared_queue.close()
    shared_queue.join_thread()