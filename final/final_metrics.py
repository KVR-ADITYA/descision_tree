import numpy as np
import pandas as pd
import os
from read_data import *


def gini_impurity(x, y):
    col_data = np.vstack((x, y)).T
    avg = np.mean(col_data[:, 0])
    g_data = col_data[col_data[:, 0] >= avg]
    l_data = col_data[col_data[:, 0] < avg]
    d = len(g_data[g_data[:, 1] == 1])
    c = len(g_data[g_data[:, 1] == 0])
    b = len(l_data[l_data[:, 1] == 1])
    a = len(l_data[l_data[:, 1] == 0])
    total_elements = a + b + c + d
    gini_1 = 1 - np.square(a/(a+b)) - np.square(b/(a+b))
    gini_2 = 1 - np.square(c/(c+d)) - np.square(d/(c+d))
    total_gini = ((a+b)/total_elements) * gini_1 + \
        ((c+d)/total_elements) * gini_2
    return total_gini


def gini(data_arr):
    cols = data_arr.shape[1]
    gini_indices = [gini_impurity(
        data_arr[:, i], data_arr[:, cols-1]) for i in range(1)]
    return gini_indices


def calculate_metrics(filename):
    df, data_arr = read_data(filename, clf=True)
    gini_index = gini(data_arr)
    # print(len(data_arr))


if __name__ == '__main__':
    filename = '../data/1.csv'
    calculate_metrics(filename)
