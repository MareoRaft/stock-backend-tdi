'''
Analyse the data and re-output.
'''
# 3rd-party
import pandas
import numpy as np

def get_dataframe(api_data):
	''' Given the data object from the api, load it into a pandas dataframe and return it. '''
	df = pandas.DataFrame.from_dict(
		data=api_data,
		orient='index',
		dtype=np.float64,
	)
	return df


def get_frontend_data(df):
	''' Output the data object for consumption by the frontend. '''
	frontend_obj = df.to_dict(
		orient='dict', # modify this to change data structure!
	)
	return frontend_obj
