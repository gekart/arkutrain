Dockerfile Challenge (derived from source)
Our manager has tasked us with a very important project, aparently customers are complaining that our Random Cat Generator has been down for some time. It's super urgent - Sev 1, interwebs down/down or something.

We only know a little bit about the app, the previous engineer has rage quit and all we have is the source code and a few details.

So far we know:

It's a Python app
That it ran in a Docker container before
The network engineer said the container used to listen on port 5000/TCP, something about exposè, maybe they were french?
It was based on the python:alpine docker image
There was mention of a requirements.txt file, and a pip install command?
Steps
Create a project folder
Copy the app.py and requirements.txt into that folder (see below)
In the project folder create a templates folder
Copy index.html into the templates folder
Create a Dockerfile for this Python app
Build a container image with the Dockerfile
Run a container from the image and load the app in a browser to test
Tell our manager we're back online!
