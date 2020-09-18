Run
--------------------
To run, do

    heroku local

To run the server with gunicorn manually, do

    export all .env vars
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

	cd client
	npm run build
	# update requirements.txt if you haven't done so already
	pipreqs --force
	# check changes into git
	git diff
	(git commit, etc)
    git push heroku master


