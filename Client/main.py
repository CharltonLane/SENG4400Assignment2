import os
import json
import time
import requests

from google.cloud import pubsub_v1

target_api = os.environ.get("TARGET_API", "https://c3299743seng4400a2.ts.r.appspot.com/dashboard")
target_api = 'http://127.0.0.1:5000/dashboard' #  Debug code to test locally.

# Set authentication credentials environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c3299743seng4400a2-bc323ed679a2.json"


# I did not write this function. See the stackoverflow link for source.
def primes(n):
    """ Returns  a list of primes < n
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def generate_message(question, answer, time_taken):
    message = {"question": question, "answer": answer, "time_taken": time_taken, "time_generated": time.time()}
    return message


def callback(message):
    # Read the message.
    message_data = json.loads(message.data)

    if message_data["question"] <= 1000000:  # Ignore any question greater than 1000000
        message.ack()

        # Generate primes and measure the time taken.
        start = time.time()
        answer = primes(message_data["question"])
        end = time.time()
        time_taken = round(((end-start) * 1000))

        # Generate a message containing the primes and time taken to compute.
        output_message = generate_message(message_data["question"], answer, time_taken)
        print(output_message)

        response = requests.post(target_api, json=output_message)
        print("Response: ", response)


def main():
    project_id = "c3299743seng4400a2"
    subscription_id = "PubSubQueueForOffline-sub"

    # Number of seconds the subscriber should listen for messages
    timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

    while True:
        # Wrap subscriber in a 'with' block to automatically call close() when done.
        with subscriber:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result()


if __name__ == '__main__':
    main()
