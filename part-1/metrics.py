import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def _entropy(values):
	counts = np.bincount(values)
	probs = counts[np.nonzero(counts)] / float(len(values))
	return - np.sum(probs * np.log(probs))

def _information_gain(feature, y):
	feature_set_indices = np.nonzero(feature)[1]
	feature_not_set_indices = [i for i in feature_range if i not in feature_set_indices]
	entropy_x_set = _entropy(y[feature_set_indices])
	entropy_x_not_set = _entropy(y[feature_not_set_indices])

	return entropy_before - (((len(feature_set_indices) / float(feature_size)) * entropy_x_set)
							 + ((len(feature_not_set_indices) / float(feature_size)) * entropy_x_not_set))	

def gain_metrics(data):
	# data['f20'].values[data['f20'].values > 0] = 1
	nparray = data.to_numpy()
	feature_size = nparray.shape[1]
	# print(feature_size)
	feature_range = range(0, feature_size)
	entropy_before = _entropy(data['f20'])
	print(entropy_before)
	information_gain_scores = []
	for feature in data.T:
		information_gain_scores.append(_information_gain(feature, data['f20']))
	print(information_gain_scores)    
	return information_gain_scores, []


def chi_sq(data):
	pass

def gini_impurity_total(a=0, b=0, c=0, d=0):
	total_elements = a + b + c + d
	gini_1 = 1 - np.square(a/(a+b)) - np.square(b/(a+b))
	gini_2 = 1 - np.square(c/(c+d)) - np.square(d/(c+d))
	total_gini = ((a+b)/total_elements) * gini_1 + ((c+d)/total_elements) * gini_2
	return total_gini

def gini_impurity(a=0, b=0):
	return 1 - np.square(a/(a+b)) - np.square(b/(a+b))    

def gini_split(data):
	ans = []
	mean_data = data.mean(axis = 0)
	for i in range (0,20):
		q = data[data['f'+str(i)]>=data['f'+str(i)].mean()]
		q_dash = data[data['f'+str(i)] < data['f'+str(i)].mean()]
		dval = q[q['f20']>=1]
		cval = q[q['f20'] == 0]
		bval = q_dash[q_dash['f20']>=1]
		aval = q_dash[q_dash['f20'] == 0]
		a = len(aval)
		b = len(bval)
		c = len(cval)
		d = len(dval)
		ans.append(gini_impurity_total(a,b,c,d))
	return ans


def misclf_err(data):
	pass


def calculate_metrics(data):
	gain_ratio, info_gain = gain_metrics(data)
	#chi_sq = chi_sq(data)
	gini_values = gini_split(data)
	#misclf_err = misclf_err(data)
	#return gain_ratio, chi_sq, gini_split, info_gain, misclf_err
	return gain_ratio, info_gain, gini_values

def read_data(filename):
	df = pd.read_csv('../data/'+filename+'.csv')
	row1 = df.columns
	row2 = []
	cols = {}
	for i in range(len(row1)):
		cols[str(row1[i])] = 'f'+str(i)
		# row2.append(float(row1[i]))

	df.rename(columns=cols, inplace=True)
	# df.loc[len(df.index)] = row2
	#print(df.dtypes)
	return df


if __name__ == '__main__':
	metric_dict_gain_ratio = {}
	# metric_dict_chi_sq = {}
	metric_dict_gini_split = {}
	metric_dict_info_gain = {}
	# metric_dict_misclf_err = {}
	for i in range(1, 2):
		gain_ratio, info_gain, gini_split = calculate_metrics(read_data(str(i)))
		print(gain_ratio)
		print(blah)
		print(info_gain)
		print(gini_split)	
	# for i in range(1, 57):
	# 	gain_ratio, chi_sq, gini_split, info_gain, misclf_err = calculate_metrics(
	# 		read_data(str(i)))	
	# 	metric_dict_gain_ratio[str(i)] = gain_ratio
	# 	metric_dict_chi_sq[str(i)] = chi_sq
	# 	metric_dict_gini_split[str(i)] = gini_split
	# 	metric_dict_info_gain[str(i)] = info_gain
	# 	metric_dict_misclf_err[str(i)] = misclf_err

	# results = pd.DataFrame(metric_dict_gain_ratio)
	# results.to_csv('./resultsmetrics-gain_ratio.csv')

	# results = pd.DataFrame(metric_dict_chi_sq)
	# results.to_csv('./resultsmetrics-chi_sq.csv')

	# results = pd.DataFrame(metric_dict_gini_split)
	# results.to_csv('./resultsmetrics-gini_split.csv')

	# results = pd.DataFrame(metric_dict_info_gain)
	# results.to_csv('./resultsmetrics-info_gain.csv')

	# results = pd.DataFrame(metric_dict_misclf_err)
	# results.to_csv('./resultsmetrics-misclf_err.csv')
