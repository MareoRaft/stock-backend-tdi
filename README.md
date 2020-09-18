# About
This is the repo for the **backend** of the Stock Ticker App Milestone Project for TDI (The Data Incubator).  The repo for the **frontend** is [here](https://github.com/MareoRaft/stock-frontend-tdi).




Run
--------------------
To run, do

    heroku local

To run the server with gunicorn manually, do

    # export all .env vars
    gunicorn server.main:app

To run with flask manually, do

	# Python module and var for the flask `app` var
	export FLASK_APP=server.main:app
	export FLASK_ENV=development
	pip3 install flask-dotenv==0.1.2
	flask run




Test
--------------------
To run tests

	pip3 install pytest-dotenv
	pytest




Build & Deploy
--------------------
To build & deploy

	# update requirements.txt if you haven't done so already
	pipreqs --force
	git diff
	# check changes into git if there are any
    git push heroku master


