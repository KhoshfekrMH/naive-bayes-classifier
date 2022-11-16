import statistics

import pandas as pd
import numpy as np

df = pd.read_csv('adult.csv', na_values=' ?')
# region 1.fixing missing datas

dataFrame = df.fillna(method='pad')

# endregion

# region 2.separate column and number of prior
Sex = df['Sex']
Male = []
Female = []
for i in range(32560):
    if Sex[i] == ' Male':
        Male.append(Sex[i])
    else:
        Female.append(Sex[i])

MaleNum = len(Male)
FemaleNum = len(Female)
# endregion
