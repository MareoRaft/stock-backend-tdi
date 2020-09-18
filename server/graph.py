'''
Graph the data into a nice visualization for the user.  (using Bokeh)
'''
# 3rd-party
import bokeh.plotting as bp
from bokeh.resources import CDN
from bokeh.embed import file_html
import numpy as np


def get_x_and_y_values(data, app):
	sorted_dates = list(sorted(data['4. close'].keys()))
	x = list(range(len(sorted_dates)))
	y = [data['1. open'][d] for d in sorted_dates]
	y_close = [data['4. close'][d] for d in sorted_dates]
	# app.logger.info(f'\nx values: {x}\ny values: {y}\n\n')
	app.logger.info(f'rstu')
	return x, y, y_close


def graph_data(data, is_close_displayed, app):
	# x-axis is date, y-axis is stock-price
	x, y, y_close = get_x_and_y_values(data, app)
	# create the plot
	plot = bp.figure(
		title='Daily stock price',
	)
	# add line to the plot
	plot.line(x, y, legend_label='avg price', line_width=3, color='green')
	if is_close_displayed:
		plot.line(x, y_close, legend_label='close price', line_width=3, color='yellow')
	# return the plot
	return plot


def get_html_file(plot):
	html = file_html(plot, CDN, 'my plot')
	return html
