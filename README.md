Run
--------------------
To run the server, do

	# Python module and var for the flask `app` var
	export FLASK_APP=server.main:app
	export FLASK_ENV=development
	pip3 install flask-dotenv==0.1.2
	flask run




Testing
--------------------
To run tests, do

	pip3 install pytest-dotenv
	pytest




Deploying
------------------
To deploy

	# update requirements.txt if you haven't done so already, and check changes into git
	pipreqs --force
	git diff
	(git commit, etc)
    git push heroku master
