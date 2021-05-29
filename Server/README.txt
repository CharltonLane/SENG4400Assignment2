Server README

Charlton Lane
C3299743
SENG4400 Assignment 2


==== To create the Pub/Sub Queue ==== 
In google cloud, create a project.
Navigate to the Pub/Sub button in the menu to the right, under the Three horizontal lines.
On the "Topics" section, near the top, click "CREATE TOPIC". Give it a topic ID. Leave "Create a default subscription" checked. 

To become authorised to access the queue, you need to make a service account and give it permissions.
Navigate to the IAM & Admin tab and select the Service Accounts sub-tab
Click the "CREATE SERVICE ACCOUNT" button towards the top of the page
1. Name it
2. Select the Owner role under the Quick access label on the "Role" dropdown
Choose DONE

Now Click on the email that is shown for the service account
Click KEYS towards the top of the page
Create a new key by clicking Add key > New key > JSON
A key file will be downloaded.

I've set it up so this key is placed in the root directory of each of the projects that use it. This probably isn't the best way to store this as it should be kept more securely.
So for this project, place the JSON key file inside of the Client folder.

To run the server you need to make sure the project_id and topic_id variables are set to the project ID of the cloud project, and the topic ID of the Pub/Sub queue on google cloud.
The JSON key file should also be placed inside the Server/ folder, and it's name is given so the environment variables can be set (2 lines up from where project_id is set).


==== To run the program ====

Open the Server folder as a PyCharm project. The project is setup to use a virtual environment of python 3.8
Run main.py

The PubSub queue being used is called "PubSubQueueOfflineUse". The PubSub queue being used by the deployed app in part 4 is called "PubSubQueue".
If you want to spam the deployed system with questions, change "PubSubQueueOfflineUse" to "PubSubQueue" on line 24.

If there are any dependencies missing you can install them using the following command
pip install -r requirements.txt


==== Other ====

The publish delay and maximum random number size are both configurable via environment variables. These are PUBLISH_DELAY and MAX_RANDOM_NUMBER respectively.

cloud_function_single.py is a modified version of the Server that can be used as a Google Cloud Function. It only adds a single question to the queue.
It also has code to handle being called as a request, and to support CORS