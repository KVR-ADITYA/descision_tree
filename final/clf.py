import numpy as np
import pandas as pd
from read_data import *

for i in range(1, 57):
    file_name = f'../data/{i}.csv'
    df, data = read_data(file_name, clf=True)
    np.savetxt(f"../new_data/n{i}.csv", data, delimiter=",")
