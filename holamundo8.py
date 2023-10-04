import threading
import time

def job_scheduler(f, n):
    def delayed_execution():
        time.sleep(n / 1000)  # Convert milliseconds to seconds
        f()

    threading.Thread(target=delayed_execution).start()

# Example function to be executed
def my_function():
    print("Job executed!")

# Using the job_scheduler with my_function
print("Scheduling job...")
job_scheduler(my_function, 2000)  # Schedule my_function to be called after 2000 milliseconds
print("Job scheduled. Waiting for execution...")
