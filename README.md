# Sample Dockerized Flask Application

## Basic concepts

- A **docker image** is essentially a well-packaged program that is battery-included, it brings it's own bottle and every dependency it needs to run a service.

- A **docker container** is a running docker image. It's best to think of it as an active and running process than some packaged cargo on a ship. Ideally containers are stateless meaning they're disposable like Kleenex and don't contain important information in them once they're done, just like how you wouldn't write your bank account info on a napkin and expect it to last.

- A **docker volume** can be inserted into a container on startup in order for it to keep its important bits if you decide to violate the stateless best practice.

Once these become a part of your mental models it should be easier to read through guides and/or documentations online.

## How to run this thing

You can run the application locally with python3 (once you have flask installed) with
```bash
export STORAGE_DIR=./messages
export FLASK_APP=./app.py
python3 -m flask run
```
and see that it is running by visiting http://localhost:5000 in your browser.

To ship this thing to docker.otenv.com for deployment as one single thing, you would need to construct a docker image. The instructions for that is written in the form of Dockerfile, which specifies what commands to run on a fresh "system" in order to get it to the point where the application can be run with one single command.

Begin the construction by running
```
docker build . --tag flask-app
```
and see the output of commands the background process had ran to get the image ready.

At this point you can either run the image you have just built locally or publish it to a docker registry (e.g. docker.otenv.com).

To run it locally just do `docker run -p 5000:5000 flask-app` and verify it with the same steps as above.

To publish it to docker.otenv.com run
```bash
docker tag flask-app docker.otenv.com/sample-flask-app:v1
docker push docker.otenv.com/sample-flask-app:v1
```
and you should see the image being pushed.
