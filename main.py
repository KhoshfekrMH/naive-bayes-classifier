import statistics

import pandas as pd
import numpy as np

df = pd.read_csv('adult.csv', na_values=' ?')
# region 1.fixing missing datas

dataFrame = df.fillna(method='pad')

# endregion

# region 2.separate column and number of prior
Sex = dataFrame['Sex']
Male = []
Female = []
for i in range(32560):
    if Sex[i] == ' Male':
        Male.append(Sex[i])
    else:
        Female.append(Sex[i])

MaleNum = len(Male)
FemaleNum = len(Female)
SexNum = len(Sex)

Education = dataFrame['Education']
Bachelors = []
Hs_guard = []
th11 = []
Masters = []
th9 = []
someCollage = []
Assoc_acdm = []
Assoc_voc = []
prof_School = []
th7_th8 = []
th10 = []
st1_th4 = []
th5_th6 = []
th12 = []
Preschool = []
Doctorate = []
for i in range(32560):
    if Education[i] == ' Bachelors':
        Bachelors.append(Education[i])
    elif Education[i] == ' HS-grad':
        Hs_guard.append(Education[i])
    elif Education[i] == ' 11th':
        th11.append(Education[i])
    elif Education[i] == ' Masters':
        Masters.append(Education[i])
    elif Education[i] == ' 9th':
        th9.append(Education[i])
    elif Education[i] == ' Some-college':
        someCollage.append(Education[i])
    elif Education[i] == ' Assoc-acdm':
        Assoc_acdm.append(Education[i])
    elif Education[i] == ' Assoc-voc':
        Assoc_voc.append(Education[i])
    elif Education[i] == ' Prof-school':
        prof_School.append(Education[i])
    elif Education[i] == ' 7th-8th':
        th7_th8.append(Education[i])
    elif Education[i] == ' 10th':
        th10.append(Education[i])
    elif Education[i] == ' 1st-4th':
        st1_th4.append(Education[i])
    elif Education[i] == ' 5th-6th':
        th5_th6.append(Education[i])
    elif Education[i] == ' 12th':
        th12.append(Education[i])
    elif Education[i] == ' Preschool':
        Preschool.append(Education[i])
    else:
        Doctorate.append(Education[i])

Status = dataFrame['Status']
Married_civ_spouse = []
Never_married = []
Divorced = []
Seperated = []
Married_spouse_absent = []
Married_AF_spous = []
Widowed = []
for i in range(32560):
    if Status[i] == ' Married-civ-spouse':
        Married_civ_spouse.append(Status[i])
    elif Status[i] == ' Never-married':
        Never_married.append(Status[i])
    elif Status[i] == ' Divorced':
        Divorced.append(Status[i])
    elif Status[i] == ' Married-spouse-absent':
        Married_spouse_absent.append(Status[i])
    elif Status[i] == ' Widowed':
        Widowed.append(Status[i])
    elif Status[i] == ' Married-AF-spouse':
        Married_AF_spous.append(Status[i])
    else:
        Seperated.append(Status[i])

Others = dataFrame['Others']
Adm_clerical = []
Craft_repair = []
Sales = []
Exec_managerial = []
Handlers_cleaners = []
Transport_moving = []
Prof_specialty = []
Farming_fishing = []
Tech_support = []
Machine_op_inspct = []
Protective_serv = []
Other_service = []
for i in range(32560):
    if Others[i] == ' Adm-clerical':
        Adm_clerical.append(Others[i])
    elif Others[i] == ' Craft-repair':
        Craft_repair.append(Others[i])
    elif Others[i] == ' Sales':
        Sales.append(Others[i])
    elif Others[i] == ' Exec-managerial':
        Exec_managerial.append(Others[i])
    elif Others[i] == ' Handlers-cleaners':
        Handlers_cleaners.append(Others[i])
    elif Others[i] == ' Transport-moving':
        Transport_moving.append(Others[i])
    elif Others[i] == ' Prof-specialty':
        Prof_specialty.append(Others[i])
    elif Others[i] == ' Farming-fishing':
        Farming_fishing.append(Others[i])
    elif Others[i] == ' Tech-support':
        Tech_support.append(Others[i])
    elif Others[i] == ' Machine-op-inspct':
        Machine_op_inspct.append(Others[i])
    elif Others[i] == ' Protective-serv':
        Protective_serv.append(Others[i])
    else:
        Other_service.append(Others[i])

skinColor = dataFrame['Skin Color']
whiteSkin = []
blackSkin = []
asianSkin = []
EskimoSkin = []
OtherSkin = []
for i in range(32560):
    if skinColor[i] == ' White':
        whiteSkin.append(skinColor[i])
    elif skinColor[i] == ' Black':
        blackSkin.append(skinColor[i])
    elif skinColor[i] == ' Amer-Indian-Eskimo':
        EskimoSkin.append(skinColor[i])
    elif skinColor[i] == ' Other':
        OtherSkin.append(skinColor[i])
    else:
        asianSkin.append(skinColor[i])

# endregion


# region 3. Calculate each Probability of each Prior
pMale = MaleNum / SexNum
pFemale = FemaleNum / SexNum