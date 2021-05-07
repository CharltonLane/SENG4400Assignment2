"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
import time
import os
import json
import random

# use pip install --upgrade google-cloud-pubsub
from google.cloud import pubsub_v1


largest_random_number = 1000

def get_callback(f, data):
    def callback(f):
        try:
            print(f.result())
        except:  # noqa
            print("Please handle {} for {}.".format(f.exception(), data))
    return callback


def create_message(random_number):
    message = {"question": random_number}
    return json.dumps(message)


def main():
    # Set authentication credentials environment variable.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "totemic-carrier-313004-2b48dbdd22fe.json"

    project_id = "totemic-carrier-313004"
    topic_id = "SENG4400A2PubSub"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    for i in range(1):
        data = create_message(random.randint(0, largest_random_number))

        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data.encode("utf-8"))

        # Publish failures shall be handled in the callback function.
        future.add_done_callback(get_callback(future, data))

    print("Done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
