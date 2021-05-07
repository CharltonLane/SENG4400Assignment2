import json

from flask import Flask, request,  render_template
import os
from google.cloud import datastore

# Set authentication credentials environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "c3299743seng4400a2-bc323ed679a2.json"

datastore_client = datastore.Client()

app = Flask(__name__)

# This is used when running locally only. When deploying to Google App
# Engine, a webserver process such as Gunicorn will serve the app. This
# can be configured by adding an `entrypoint` to app.yaml.
# Flask's development server will automatically serve static files in
# the "static" directory. See:
# http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
# App Engine itself will serve those files as configured in app.yaml.
# app.run(host='0.0.0.0', port=8080, debug=True)


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
    #try:
    request.get_data()

    data = request.json
    json_data = json.loads(data)

    store_answer(json_data)
    print("Completed processing of request.")
    return "All good!", 200
    #except Exception as e:
        #print("Oh noh")
        #return f"An Error Occured: {e}"


@app.route('/')
def root():
    past_answers_from_db = fetch_answers(50)

    return render_template('index.html', past_answers=past_answers_from_db)



