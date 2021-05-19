import json
import flask
from flask import Flask, request, render_template, make_response
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


@app.route('/get50Entries')
def get_50_entries():
    results = fetch_answers(50)

    output = {"data": []}
    for entry in results:
        output["data"].append({"answer": entry["answer"], "time_taken": entry["time_taken"]})
    print("Output of first 50: ", output)

    return make_response(output, 200)


@app.route('/getNewEntries')
def get_new_entries():
    results = fetch_answers(1)
    #print("Rweults: ", results)

    output = {"data": []}
    for entry in results:
        #print(entry["answer"])
        #print(entry["time_taken"])
        output["data"].append({"answer": entry["answer"], "time_taken": entry["time_taken"]})
    print("Output: ", output)

    return make_response(output, 200)


@app.route('/dashboard', methods=['POST'])
def post_answer():
    print("Got post request")

    request.get_data()

    data = request.json
    json_data = json.loads(data)

    store_answer(json_data)
    print("Completed processing of request.")

    #past_answers_from_db = fetch_answers(50)

    return make_response(
        "OK",
        200,
    )


@app.route('/')
def root():
    return render_template('index.html')



