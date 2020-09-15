import pytest

from analyze import *

API_DATA = {
    '2020-09-14 19:00:00': {
	      '1. open': '1511.0500',
	      '2. high': '1512.3800',
	      '3. low': '1511.0500',
	      '4. close': '1512.3800',
	      '5. volume': '1486',
    },
    '2020-09-15 19:00:00': {
	      '1. open': '1611.0500',
	      '2. high': '1612.3800',
	      '3. low': '1611.0500',
	      '4. close': '1612.3800',
	      '5. volume': '1486',
    },
}

def test_get_dataframe():
	df = get_dataframe(API_DATA)
	assert type(df['1. open'][0]) == np.float64
	assert df['1. open'][0] == np.float64(1511.05)

def test_get_frontend_data():
	df = get_dataframe(API_DATA)
	frontend_data = get_frontend_data(df)
	assert frontend_data['1. open']['2020-09-14 19:00:00'] == np.float64(1511.05)
