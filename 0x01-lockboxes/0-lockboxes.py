import threading

# Define a lockbox as a threading.Lock object
lockdown = threading.Lock()

# Function that requires exclusive access to a shared resource
def canUnlockAll(boxes):
    with lockbox:
        # Access shared resource here
        # ...

# Multiple threads can run the same function
thread1 = threading.Thread(target=critical_section_of_code)
thread2 = threading.Thread(target=critical_section_of_code)

thread1.start()
thread2.start()
