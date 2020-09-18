# builtin imports
import os

# 3rd party imports
from flask import Flask, render_template, request, redirect, send_from_directory
import flask
print(flask.__version__) # version 1.1.2

# local imports
from . import api
from . import analyze
from . import graph



# Create the app
app = Flask(__name__, static_folder='client/build')



# Define the routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
	if path != '' and os.path.exists(f'{app.static_folder}/{path}'):
		return send_from_directory(app.static_folder, path)
	else:
		return send_from_directory(app.static_folder, 'index.html')



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


@app.route('/about')
def about():
  return render_template('about.html')



# Main execution loop
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(
		host='0.0.0.0',
		port=port,
	)


