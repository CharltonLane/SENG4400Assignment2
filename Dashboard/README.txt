Dashboard README

Charlton Lane
C3299743
SENG4400 Assignment 2


==== To create the web service on Google App Engine ====

Choose the "App engine" button from the side panel
Choose to create an application
Set the region to australia-southeast1 (I guess this is optional) and hit Create app
Set the language to python and leave it set to standard

Now on the Cloud SDK command line app (You'll need to download + install this), run the following while in the directory of the project
gcloud init
This should run you through choosing which project you want to work with.

then use the command:
gcloud app deploy
This will deploy the Dashboard code to google cloud as a web app. It will take a minute or so and give you the URL that the app is hosted at.



==== To run the Dashboard locally ====

Open the Dashboard folder as a PyCharm project.

Run main.py using a flask server configuration.
This should already be set up in the project but if not, create a new run configuration and choose "Flask server", set the target to the path of main.py and the working directory to the Dashboard folder.

Open the URL that appears in the console after running, this should be http://localhost:5000 (http://127.0.0.1:5000)
If there have been any items pushed from the Server to the Client via the queue while this app is running, they will appear on the dashboard.

It is also possible to use the buttons at the top of the dashboard to create new items, this is a lot slower due to latency so it will take a few seconds for changes to appear.
