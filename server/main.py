# builtin imports
import os

# 3rd party imports
from flask import Flask, render_template, request, redirect, send_from_directory
import flask

# local imports
from . import api
from . import normalize
from . import analyze
from . import graph
from . import global_constants as GC



# Create the app
app = Flask(__name__)



# Define the routes
@app.route('/')
def index():
	# get url params
	ticker = flask.request.args.get('ticker', default='VZ')
	is_stat_type_displayed = {
		stat_type: flask.request.args.get(stat_type, default='false') == 'true'
		for stat_type in GC.STAT_TYPES
	}
	# computer everything
	api_data = api.get_data(ticker)
	clean_data = normalize.fix_stat_types_in_data(api_data)
	app.logger.info(clean_data)
	df = analyze.get_dataframe(clean_data)
	frontend_data = analyze.get_frontend_data(df)
	plot = graph.graph_data(frontend_data, is_stat_type_displayed, app)
	graph_html = graph.get_html_file(plot)
	return graph_html



# Main execution loop
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


