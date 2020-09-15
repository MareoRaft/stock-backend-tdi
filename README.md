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
