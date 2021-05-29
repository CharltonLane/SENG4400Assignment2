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
    doc_ref.set(data)


def fetch_new_answers(last_time):
    # Finds all answers with a time_generated later than the last time checked by the dashboard.
    docs = db.collection(u'answersCollection').where(u'time_generated', u'>=', last_time).stream()

    return get_data_from_docs(docs)


def fetch_50_answers():
    # Finds the 50 most recent answers (but they're in the wrong order).
    docs = db.collection(u'answersCollection').order_by("time_generated",
                                                        direction=firestore.Query.DESCENDING).limit(50).stream()
    data = get_data_from_docs(docs)
    data.reverse()  # Put them in the righter order, so newest are first.

    return data


def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


def get_data_from_docs(docs):
    output = []
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        output.append(doc.to_dict())
    return output

# ======== Routes ======== #

@app.route('/get50Entries', methods=['GET'])
def get_50_entries():
    # Pulls the 50 most recent entries from the firestore.
    output = {"data": fetch_50_answers()}

    return make_response(output, 200)


@app.route('/getNewEntries', methods=['POST'])
def get_new_entries():
    # Search for any entries that have been added since the given time.
    time = request.json['lastCheckDate']/1000
    output = {"data": fetch_new_answers(time)}
    print("Output: ", output)

    return make_response(output, 200)


@app.route('/clearAllEntries')
def clear_all_entries():
    # Search for any entries that have been added since the given time.
    delete_collection(db.collection(u'answersCollection'), 50)
    print("Deleted firestore contents")

    return make_response("OK", 200)



@app.route('/dashboard', methods=['POST'])
def post_answer():
    # Receives and stores an answer that has been posted from the Client.
    store_answer(request.json)
    #print("Completed processing of request.")

    return make_response(
        "OK",
        200,
    )


@app.route('/')
def root():
    # Display the dashboard.
    return render_template('index.html')



