import json

from flask import Flask, request,  render_template
import os
from google.cloud import datastore

# Set authentication credentials environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c3299743seng4400a2-bc323ed679a2.json"

datastore_client = datastore.Client()
app = Flask(__name__)


def store_answer(data):
    entity = datastore.Entity(key=datastore_client.key('item'), exclude_from_indexes=("answer", "time_taken"))
    entity.update(data)
    datastore_client.put(entity)


def fetch_answers(limit):
    query = datastore_client.query(kind='item')
    results = query.fetch(limit=limit)

    return results


@app.route('/dashboard', methods=['POST'])
def post_answer():
    print("Got post request")

    request.get_data()

    data = request.json
    json_data = json.loads(data)

    store_answer(json_data)
    print("Completed processing of request.")
    return "All good!", 200


@app.route('/')
def root():
    past_answers_from_db = fetch_answers(50)

    return render_template('index.html', past_answers=past_answers_from_db)



