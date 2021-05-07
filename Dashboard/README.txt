(Firefox crashes on some of the Google Cloud pages for me. Chrome was fine)

==== To Create the web service on Google App Engine ====

Choose the "App engine" button from the side panel
Choose to create an application
Set the region to australia-southeast1 (I guess this is optional) and hit Create app
Set the language to python and leave it set to standard

Now on the Cloud SDK command line app (You'll need to download + install this), run the following while in the directory of the project
gcloud init
This should run you through choosing which project you want to work with.

gcloud app deploy
This will deploy the Dashboard code to google cloud as a web app. It will take a minute or so and give you the URL that the app is hosted at.



==== To Run the program locally ==== 

Open the Dashboard folder as a PyCharm project.
Change the URL from "https://c3299743seng4400a2.ts.r.appspot.com/Dashboard" to "http://127.0.0.1:5000/Dashboard"

Run main.py
Open the URL that appears in the console, should be https://localhost:5000
If there have been any items pushed from the Server to the Client via the queue while this app is running, they will appear here after the page refreshes.