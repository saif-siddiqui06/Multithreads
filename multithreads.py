import threading

# Function 1
def function1():
    while True:
        # Code for function 1
        print("Function 1 is running")

# Function 2
def function2():
    while True:
        # Code for function 2
        print("Function 2 is running")

# Create threads for each function
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish (optional)
# thread1.join()
# thread2.join()
