# builtin imports
import os

# 3rd party imports
from flask import Flask, render_template, request, redirect
import flask
print(flask.__version__) # version 1.1.2

# local imports
from . import api
from . import analyze



# Create the app
app = Flask(__name__)



# Define the routes
@app.route('/')
def index():
	api_data = api.get_data('GOOGL')
	df = analyze.get_dataframe(api_data)
	frontend_data = analyze.get_frontend_data(df)
	return frontend_data

@app.route('/about')
def about():
  return render_template('about.html')



# Main execution loop
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


