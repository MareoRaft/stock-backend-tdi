import pytest

from graph import *


def test_graph_data():
	plot = graph_data()


def test_get_html_file():
	plot = graph_data()
	html = get_html_file(plot)
	assert type(html) == str
	assert html.strip().startswith('<!DOCTYPE html>')
