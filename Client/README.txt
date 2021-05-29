Client README

Charlton Lane
C3299743
SENG4400 Assignment 2


==== Setup ====

This README assumes you have read the README for the Client project.
To Run the client you just need to make sure the project_id variable is set to the project ID of the cloud project 
and the subscription_id variable is set to the subscription ID of the queue subscription created on google cloud (should be "<name of the topic>-sub" by default).

The JSON key file should also be placed inside the Server/ folder, and it's name is given so the environment variables can be set (2 lines up from where project_id is set).


==== To Run the program ==== 

Open the Server folder as a PyCharm project. Again this project is set up with a virtual environment of python 3.8.
Run main.py

The code is set to subscribe to the PubSub queue called "PubSubQueueOfflineUse-sub". This is only used by the offline version of Server and client. To subscribe to the PubSub being used for the deployed system, change this to just "PubSubQueue-sub"
If you want to send to a local instance of the dashboard, either set the environment variable "TARGET_API" to 'http://127.0.0.1:5000/dashboard', or uncomment line 9.

If any dependencies are missing, install them with
pip install -r requirements.txt

==== Other ====

The rest api is configurable though the environment variable TARGET_API.

I've added some more data to the response that is sent to the dashboard.
It includes "answer" and "time_taken" as required in the assignment spec but I've also added "question" and "time_generated" as I'm showing them on the dashboard.

cloud_function.py is a modified version of the Client that can be used as a Google Cloud Function.