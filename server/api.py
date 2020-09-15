'''
Functions to retrieve desired data from the API.
'''

# 3rd-party
from alpha_vantage.timeseries import TimeSeries

def get_data(ticker):
	ts = TimeSeries()
	data, metadata = ts.get_intraday(ticker)
	# The data has the following structure (shown by example):
	# {
	#     '2020-09-14 19:00:00': {
	# 	      '1. open': '1511.0500',
	# 	      '2. high': '1512.3800',
	# 	      '3. low': '1511.0500',
	# 	      '4. close': '1512.3800',
	# 	      '5. volume': '1486',
	#     },
	#	  ...
	# }
	return data

