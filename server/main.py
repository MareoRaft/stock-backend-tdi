# builtin imports
import os

# 3rd party imports
from flask import Flask, render_template, request, redirect, send_from_directory
import flask
# print(flask.__version__) # version 1.1.2

# local imports
from . import api
from . import analyze
from . import graph



# Create the app
REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PATH = os.path.join(REPO_PATH, 'templates')
app = Flask(__name__, static_folder=STATIC_PATH)



# Define the routes
@app.route('/static', defaults={'path': 'index.html'})
@app.route('/static/<path:path>')
def serve_static_file(path):
	app.logger.info('serve static file')
	return send_from_directory(app.static_folder, path)


@app.route('/stock-graph')
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
	app.run(
		host='0.0.0.0',
		port=port,
	)


