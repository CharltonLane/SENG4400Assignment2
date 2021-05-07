""" Publishes multiple messages to a Google Pub/Sub topic. """
import time
import os
import json
import random

from google.cloud import pubsub_v1


publish_delay = 1000  # Delay in milliseconds.
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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c3299743seng4400a2-bc323ed679a2.json"

    project_id = "c3299743seng4400a2"
    topic_id = "PubSubQueue"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    while True:
        data = create_message(random.randint(0, largest_random_number))

        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data.encode("utf-8"))

        # Publish failures shall be handled in the callback function.
        future.add_done_callback(get_callback(future, data))

        # Wait the given amount of time.
        time.sleep(publish_delay / 1000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
