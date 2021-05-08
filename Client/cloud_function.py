import base64
import os
import json
import time
import requests

target_api = os.environ.get("TARGET_API", "https://c3299743seng4400a2.ts.r.appspot.com/dashboard")


# I did not write this function. See the stackoverflow link for source.
def primes(n):
    """ Returns  a list of primes < n
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def generate_message(answer, time_taken):
    message = {"answer": answer, "time_taken": time_taken}
    return json.dumps(message)


def callback(event, context):
    # Read the message.
    message_data = json.loads(base64.b64decode(event['data']))

    if message_data["question"] <= 1000000:  # Ignore any question greater than 1000000
        # Generate primes and measure the time taken.
        start = time.time()
        answer = primes(message_data["question"])
        end = time.time()
        time_taken = round(((end-start) * 1000))

        # Generate a message containing the primes and time taken to compute.
        output_message = generate_message(answer, time_taken)
        print(output_message)

        response = requests.post(target_api, json=output_message)
        print("Response: ", response)


