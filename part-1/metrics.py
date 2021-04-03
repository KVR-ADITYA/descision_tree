import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gain_metrics(data):
    pass


def chi_sq(data):
    pass


def gini_split(data):
    pass


def misclf_err(data):
    pass


def calculate_metrics(data):
    gain_ratio, info_gain = gain_metrics(data)
    chi_sq = chi_sq(data)
    gini_split = gini_split(data)
    misclf_err = misclf_err(data)
    return gain_ratio, chi_sq, gini_split, info_gain, misclf_err


def read_data(filename):
    df = pd.read_csv('./data/'+filename+'.csv')
    row1 = df.columns
    row2 = []
    cols = {}
    for i in range(len(row1)):
        cols[str(row1[i])] = 'f'+str(i)
        # row2.append(float(row1[i]))

    df.rename(columns=cols, inplace=True)
    # df.loc[len(df.index)] = row2
    print(df.dtypes)
    return df


if __name__ == '__main__':
    metric_dict_gain_ratio = {}
    metric_dict_chi_sq = {}
    metric_dict_gini_split = {}
    metric_dict_info_gain = {}
    metric_dict_misclf_err = {}
    for i in range(1, 57):
        gain_ratio, chi_sq, gini_split, info_gain, misclf_err = calculate_metrics(
            read_data(str(i)))
        metric_dict_gain_ratio[str(i)] = gain_ratio
        metric_dict_chi_sq[str(i)] = chi_sq
        metric_dict_gini_split[str(i)] = gini_split
        metric_dict_info_gain[str(i)] = info_gain
        metric_dict_misclf_err[str(i)] = misclf_err

    results = pd.DataFrame(metric_dict_gain_ratio)
    results.to_csv('./resultsmetrics-gain_ratio.csv')

    results = pd.DataFrame(metric_dict_chi_sq)
    results.to_csv('./resultsmetrics-chi_sq.csv')

    results = pd.DataFrame(metric_dict_gini_split)
    results.to_csv('./resultsmetrics-gini_split.csv')

    results = pd.DataFrame(metric_dict_info_gain)
    results.to_csv('./resultsmetrics-info_gain.csv')

    results = pd.DataFrame(metric_dict_misclf_err)
    results.to_csv('./resultsmetrics-misclf_err.csv')
