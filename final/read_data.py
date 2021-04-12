import numpy as np
import pandas as pd
import os


def classify(data_array, clf=-1):
    clf_column = data_array.shape[1]-1
    if clf != -1:
        clf_column = clf
    data_array[data_array[:, clf_column] > 0] = 1
    # print(data_array[:10])
    return data_array


def normalize(data_array):
    for i in range(data_array.shape[1]-1):
        arr = data_array[:, i]
        data_array[:, i] = (arr-np.min(arr))/np.max(arr)
    return data_array


def read_data(file_name, clf=False, norm=False):
    data_array = np.genfromtxt(file_name, delimiter=',')
    columns = ['f'+str(i) for i in range(data_array.shape[1])]

    if clf:
        data_array = classify(data_array)
    if norm:
        data_array = normalize(data_array)

    df = pd.DataFrame(data_array, columns=columns)
    # print(df.head(10))
    # print(data_array[0])
    return df, data_array


if __name__ == "__main__":
    file_name = "../data/1.csv"
    target_file = "../normalized_data/1.csv"
    df, data_array = read_data(file_name, clf=True)
