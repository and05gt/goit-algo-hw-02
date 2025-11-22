import uuid
import time
import random
from queue import Queue

requests = [
"Emergency resuscitation: Blue screen on [Laptop Model]",
"Upgrade memory: [Client's Last Name] requests 32GB",
"Urgent: Coffee in the keyboard [All-in-One Model]",
"Strange noise: PC fan sounds like a jet engine",
"OS won't boot after BIOS update"
]

queue = Queue()

def generate_request():
    new_request = {
        "id": str(uuid.uuid4()),
        "name": random.choice(requests)
        }
    queue.put(new_request)
    print(f"Request added to queue: {new_request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request["name"]}")
    else:
        print("Queue is empty, no requests to process.")

def main():
    print("Press Ctrl+C to stop the program.\n")
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()