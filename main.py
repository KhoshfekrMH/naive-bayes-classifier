import statistics

import pandas as pd
import numpy as np


df = pd.read_csv('adult.csv', na_values=' ?')
# region 1.fixing missing datas

dataFrame = df.fillna(method='pad')


