import queue
import random

def message_generator():
    # random message generator
    content_message = random.randint(10, 99)
    
    # timestamp with a random delay
    timestamp_message = random.randint(1, 100) * random.random()#datetime.now().timestamp() * random.random()
    message = (content_message, round(timestamp_message, 3))

    return message

def process_message(message):
    print(message)

# task creator
def task(queue, message):
    queue.put(message)

# get queue
def get_queue(queue):
    messages = []

    while not queue.empty():
        msg = queue.get()
        messages.append(msg)

    return messages

# create tasks
def sender(queue, num_tasks):
    print("Sender Tasks")

    for i in range(num_tasks):
        message = message_generator()
        task(queue, message)
        print(f"Task {i}: {message}")

# sequencer tasks
def sequencer(queue):
    messages = []

    # get queue
    messages = get_queue(queue)

    messages_sorted = sorted(messages, key=lambda x: x[1])

    print("\nSequencer Tasks")
    for i in range(len(messages_sorted)):
        task(queue, messages_sorted[i])
        print(f"Task {i}: {messages_sorted[i]}")

# receiver tasks
def receiver(queue):
    messages = get_queue(queue)

    print("\nReceiver Tasks")

    for i in range(len(messages)):
        print(f"Processsing task {i}:")
        process_message(messages[i])

def main():

    messages_queue = queue.Queue()

    num_tasks = 3

    sender(messages_queue, num_tasks)

    sequencer(messages_queue)

    receiver(messages_queue)

if __name__ == "__main__":
    main()