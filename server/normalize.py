def fix_stat_type(api_stat_type):
	API_STAT_TYPE_TO_STAT_TYPE = {
		'1. open': 'open',
		'2. high': 'high',
		'3. low': 'low',
		'4. close': 'close',
	}
	if api_stat_type in API_STAT_TYPE_TO_STAT_TYPE:
		return API_STAT_TYPE_TO_STAT_TYPE[api_stat_type]
	else:
		return api_stat_type

def fix_stat_types_in_dic(dic):
	clean_data = {fix_stat_type(k):v for k,v in dic.items()}
	return clean_data

def fix_stat_types_in_data(data):
	clean_data = {k:fix_stat_types_in_dic(v) for k,v in data.items()}
	return clean_data
