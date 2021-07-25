General README

Charlton Lane
C3299743
SENG4400 Assignment 2


This is the general readme to explain the folder structure and other general info.


==== Info ==== 

The three folders Server, Client and Dashboard are all PyCharm projects. They should be setup ready to run in virtual python 3.8 environments with all requiremtns satisfied already in their own virtual envs.

Part 1 is the server. This code exists inside of the Server folder. 
main.py is the  server as per the requirements of part 1. 
cloud_function_single.py is the server's functionality adapted to a cloud function used in part 4.

Part 2 is the Client. This code exists inside of the Client folder
main.py is the client as per the requirements of part 2.
cloud_function.py is the client adapted to be a cloud function.

Part 3 is the dashboard. This code is within the Dashboard folder.
The dashboard uses Python with Flask for the backend and Vue.js and javascript for the frontend.
Within the templates folder is index.html. This is the only page of the dashboard.
Within static is the css and javascript files. these two files with index.html make up the frontend.
main.py is the python/flask backend.

All projects have a requirements.txt file. This provides alist of the required modules that should be installed to make the code run.
The authentication key seng4400c3299743-c62a01a02db1.json is included in each project to authenticate the app to communicate with google cloud. There is likely a more secure way of storing this key but for simplicity I've done it like this.
