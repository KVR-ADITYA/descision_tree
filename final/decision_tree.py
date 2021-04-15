import numpy as np
import pandas as pd
import os
from final_metrics import *
from read_data import *


class Node:
    def __init__(self):
        pass


def decsion_tree(file_name):
    df, data_arr = read_data(file_name, clf=True, norm=True)


if __name__ == '__main__':
    file_name = '../data/1.csv'
    decsion_tree(file_name)
