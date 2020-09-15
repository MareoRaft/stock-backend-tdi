import pytest

from api import *

def test_get_data():
	data = get_data('GOOGL')
	assert type(data) == dict
	sub_data = data[list(sorted(data.keys()))[0]]
	assert type(sub_data) == dict
	assert set(sub_data.keys()) == {'1. open', '2. high', '3. low', '4. close', '5. volume'}

