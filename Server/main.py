""" Publishes multiple messages to a Google Pub/Sub topic. """
import time
import os
import json
import random

from google.cloud import pubsub_v1


publish_delay = int(os.environ.get("PUBLISH_DELAY", 1000))  # Default delay in milliseconds.
largest_random_number = int(os.environ.get("MAX_RANDOM_NUMBER", 1000000))  # Default maximum random number to generate.

# Set authentication credentials environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c3299743seng4400a2-bc323ed679a2.json"


def create_message(random_number):
    message = {"question": random_number}
    return json.dumps(message)


def main():
    project_id = "c3299743seng4400a2"
    topic_id = "PubSubQueueForOffline"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    cutoff = 10
    while cutoff > 0:
        cutoff -= 1
        data = create_message(random.randint(0, largest_random_number))

        print(data)

        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data.encode("utf-8"))

        # Wait the given amount of time.
        time.sleep(publish_delay / 1000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
