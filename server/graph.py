'''
Graph the data into a nice visualization for the user.  (using Bokeh)
'''
# 3rd-party
import bokeh.plotting as bp
from bokeh.resources import CDN
from bokeh.embed import file_html
import numpy as np


def get_x_and_y_values(data, app):
	sorted_dates = list(sorted(data.keys()))
	x = list(range(len(sorted_dates)))
	y = [data[d] for d in sorted_dates]
	app.logger.info(f'\nx values: {x}\ny values: {y}\n\n')
	return x, y


def graph_data(data, app):
	# x-axis is date, y-axis is stock-price
	x, y = get_x_and_y_values(data, app)
	# create the plot
	plot = bp.figure(
		title='Daily stock price',
	)
	# add line to the plot
	plot.line(x, y, legend_label='avg price', line_width=3, color='green')
	# return the plot
	return plot


def get_html_file(plot):
	html = file_html(plot, CDN, 'my plot')
	return html
