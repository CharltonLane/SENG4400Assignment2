"""
Publishes a single message to a Google Pub/Sub topic.
https://australia-southeast1-seng4400c3299743.cloudfunctions.net/ServerSingle
"""
import os
import json
import random
from google.cloud import pubsub_v1


largest_random_number = int(os.environ.get("MAX_RANDOM_NUMBER", 1000000))  # Default maximum random number to generate.


def create_message(random_number):
    message = {"question": random_number}
    return json.dumps(message)


def main(request):
    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
        }
        return ('', 204, headers)
    else:
        project_id = "seng4400c3299743"
        topic_id = "PubSubQueue"

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, topic_id)

        try:
            data = create_message(random.randint(0, request.json["MAX_RANDOM_NUMBER"]))
        except KeyError:
            data = create_message(random.randint(0, largest_random_number))

        print(data)

        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data.encode("utf-8"))

        # Set CORS headers for main requests
        headers = {
            'Access-Control-Allow-Origin': '*',
        }

        return ('', 200, headers)
