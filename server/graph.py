'''
Graph the data into a nice visualization for the user.  (using Bokeh)
'''
# 3rd-party
import bokeh.plotting as bp
from bokeh.resources import CDN
from bokeh.embed import file_html
import numpy as np

# local
from . import global_constants as GC



STAT_TYPE_TO_COLOR = {
	'open': 'blue',
	'high': 'green',
	'low': 'red',
	'close': 'orange',
}


def get_x_and_y_values(data):
	sorted_dates = list(sorted(data['open'].keys()))
	x = list(range(len(sorted_dates)))
	y = {
		stat_type: [data[stat_type][d] for d in sorted_dates]
		for stat_type in GC.STAT_TYPES
	}
	# app.logger.info(f'\nx values: {x}\ny values: {y}\n\n')
	return x, y


def graph_data(data, is_stat_type_displayed, ticker):
	# x-axis is date, y-axis is stock-price
	x, y = get_x_and_y_values(data)
	# create the plot
	plot = bp.figure(
		title=f'{ticker} stock price',
	)
	# add line to the plot
	for stat_type in GC.STAT_TYPES:
		if is_stat_type_displayed[stat_type]:
			plot.line(
				x,
				y[stat_type],
				legend_label=f'{stat_type} price',
				line_width=3,
				color=STAT_TYPE_TO_COLOR[stat_type],
			)
	# return the plot
	return plot


def get_html_file(plot):
	html = file_html(plot, CDN, 'my plot')
	return html
