import datetime
import json
import flask
from flask import Flask, request, render_template, make_response
import os
from google.cloud import firestore


# Set authentication credentials environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "seng4400c3299743-c62a01a02db1.json"


# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()


app = Flask(__name__)


def store_answer(data):
    doc_ref = db.collection(u'answersCollection').document(str(data['time_generated']))

    data["new"] = True
    doc_ref.set(data)


def fetch_answers(last_time):

    docs = db.collection(u'answersCollection').where(u'time_generated', u'>=', last_time).stream()

    output = []
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        output.append(doc.to_dict())

    return output


def fetch_50_answers():
    docs = db.collection(u'answersCollection').order_by("time_generated").limit(50).stream()

    output = []
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        output.append(doc.to_dict())

    return output


@app.route('/get50Entries', methods=['GET'])
def get_50_entries():

    results = fetch_50_answers()

    output = {"data": results}

    print("Output of first 50: ", output)

    return make_response(output, 200)


@app.route('/getNewEntries', methods=['POST'])
def get_new_entries():

    print("You're boy", request.json)
    time = request.json['lastCheckDate']/1000
    print("The date and the time of the boys is ", time)
    results = fetch_answers(time)
    print("Rweults: ", results)

    output = {"data": results}

    print("Output: ", output)

    return make_response(output, 200)



@app.route('/dashboard', methods=['POST'])
def post_answer():
    print("Got post request")

    print("The json: ", request.json)

    store_answer(request.json)
    print("Completed processing of request.")

    #past_answers_from_db = fetch_answers(50)

    return make_response(
        "OK",
        200,
    )


@app.route('/')
def root():
    return render_template('index.html')



