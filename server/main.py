# builtin imports
import os

# 3rd party imports
from flask import Flask, render_template, request, redirect, send_from_directory
import flask

# local imports
from . import api
from . import analyze
from . import graph



# Create the app
app = Flask(__name__)



# Define the routes
@app.route('/')
def index():
	# get url params
	ticker = flask.request.args.get('ticker')
	# computer everything
	api_data = api.get_data(ticker)
	df = analyze.get_dataframe(api_data)
	frontend_data = analyze.get_frontend_data(df)
	desired_data = frontend_data['1. open']
	plot = graph.graph_data(desired_data, app)
	graph_html = graph.get_html_file(plot)
	return graph_html



# Main execution loop
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


