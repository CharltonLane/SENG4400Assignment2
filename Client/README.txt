(Firefox crashes on some of the Google Cloud pages for me. Chrome was fine)



This README assumes you have read the README for the Client project.
To Run the client you just need to make sure the project_id variable is set to the project ID of the cloud project 
and the subscription_id variable is set to the subscription ID of the queue subscription created on google cloud (should be "<name of the topic>-sub" by default).

The JSON key file should also be placed inside the Server/ folder, and it's name is given so the environment variables can be set (2 lines up from where project_id is set).

==== To Run the program ==== 

Open the Server folder as a PyCharm project.
Run main.py