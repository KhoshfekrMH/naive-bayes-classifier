import pandas as pd

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
# endregion

# region 4.likelihood

# ------ male -------
BachelorsAndMale = []
Hs_guardAndMale = []
th11AndMale = []
MastersAndMale = []
th9AndMale = []
someCollageAndMale = []
Assoc_acdmAndMale = []
Assoc_vocAndMale = []
prof_SchoolAndMale = []
th7_th8AndMale = []
th10AndMale = []
st1_th4AndMale = []
th5_th6AndMale = []
th12AndMale = []
PreschoolAndMale = []
DoctorateAndMale = []
for i in range(32560):
    if Education[i] == ' Bachelors' and Sex[i] == ' Male':
        BachelorsAndMale.append(Education[i])
    elif Education[i] == ' HS-grad' and Sex[i] == ' Male':
        Hs_guardAndMale.append(Education[i])
    elif Education[i] == ' 11th' and Sex[i] == ' Male':
        th11AndMale.append(Education[i])
    elif Education[i] == ' Masters' and Sex[i] == ' Male':
        MastersAndMale.append(Education[i])
    elif Education[i] == ' 9th' and Sex[i] == ' Male':
        th9AndMale.append(Education[i])
    elif Education[i] == ' Some-college' and Sex[i] == ' Male':
        someCollageAndMale.append(Education[i])
    elif Education[i] == ' Assoc-acdm' and Sex[i] == ' Male':
        Assoc_acdmAndMale.append(Education[i])
    elif Education[i] == ' Assoc-voc' and Sex[i] == ' Male':
        Assoc_vocAndMale.append(Education[i])
    elif Education[i] == ' Prof-school' and Sex[i] == ' Male':
        prof_SchoolAndMale.append(Education[i])
    elif Education[i] == ' 7th-8th' and Sex[i] == ' Male':
        th7_th8AndMale.append(Education[i])
    elif Education[i] == ' 10th' and Sex[i] == ' Male':
        th10AndMale.append(Education[i])
    elif Education[i] == ' 1st-4th' and Sex[i] == ' Male':
        st1_th4AndMale.append(Education[i])
    elif Education[i] == ' 5th-6th' and Sex[i] == ' Male':
        th5_th6AndMale.append(Education[i])
    elif Education[i] == ' 12th' and Sex[i] == ' Male':
        th12AndMale.append(Education[i])
    elif Education[i] == ' Preschool' and Sex[i] == ' Male':
        PreschoolAndMale.append(Education[i])
    else:
        DoctorateAndMale.append(Education[i])
pBachelorsAndMale = len(BachelorsAndMale) / len(Male)
pHs_guardAndMale = len(Hs_guardAndMale) / len(Male)
pth11AndMale = len(th11AndMale) / len(Male)
pMastersAndMale = len(MastersAndMale) / len(Male)
pth9AndMale = len(th9) / len(Male)
psomeCollageAndMale = len(someCollageAndMale) / len(Male)
pAssoc_acdmAndMale = len(Assoc_vocAndMale) / len(Male)
pAssoc_vocAndMale = len(Assoc_vocAndMale) / len(Male)
pprof_SchoolAndMale = len(prof_SchoolAndMale) / len(Male)
pth7_th8AndMale = len(th7_th8AndMale) / len(Male)
pth10AndMale = len(th10AndMale) / len(Male)
pst1_th4AndMale = len(st1_th4AndMale) / len(Male)
pth5_th6AndMale = len(th5_th6AndMale) / len(Male)
pth12AndMale = len(th12AndMale) / len(Male)
pPreschoolAndMale = len(PreschoolAndMale) / len(Male)
pDoctorateAndMale = len(DoctorateAndMale) / len(Male)

Married_civ_spouseAndMale = []
Never_marriedAndMal = []
DivorcedAndMale = []
SeperatedAndMale = []
Married_spouse_absentAndMale = []
Married_AF_spousAndMale = []
WidowedAndMale = []
for i in range(32560):
    if Status[i] == ' Married-civ-spouse' and Sex[i] == ' Male':
        Married_civ_spouseAndMale.append(Status[i])
    elif Status[i] == ' Never-married' and Sex[i] == ' Male':
        Never_marriedAndMal.append(Status[i])
    elif Status[i] == ' Divorced' and Sex[i] == ' Male':
        DivorcedAndMale.append(Status[i])
    elif Status[i] == ' Married-spouse-absent' and Sex[i] == ' Male':
        Married_spouse_absentAndMale.append(Status[i])
    elif Status[i] == ' Widowed' and Sex[i] == ' Male':
        WidowedAndMale.append(Status[i])
    elif Status[i] == ' Married-AF-spouse' and Sex[i] == ' Male':
        Married_AF_spousAndMale.append(Status[i])
    else:
        SeperatedAndMale.append(Status[i])

pMarried_civ_spouseAndMale = len(Married_civ_spouseAndMale) / len(Male)
pNever_marriedAndMal = len(Never_marriedAndMal) / len(Male)
pDivorcedAndMale = len(DivorcedAndMale) / len(Male)
pSeperatedAndMale = len(SeperatedAndMale) / len(Male)
pMarried_spouse_absentAndMale = len(Married_spouse_absentAndMale) / len(Male)
pMarried_AF_spousAndMale = len(Married_AF_spousAndMale) / len(Male)
pWidowedAndMale = len(WidowedAndMale) / len(Male)

Adm_clericalAndMale = []
Craft_repairAndMale = []
SalesAndMale = []
Exec_managerialAndMale = []
Handlers_cleanersAndMale = []
Transport_movingAndMale = []
Prof_specialtyAndMale = []
Farming_fishingAndMale = []
Tech_supportAndMale = []
Machine_op_inspctAndMale = []
Protective_servAndMale = []
Other_serviceAndMale = []
for i in range(32560):
    if Others[i] == ' Adm-clerical' and Sex[i] == ' Male':
        Adm_clericalAndMale.append(Others[i])
    elif Others[i] == ' Craft-repair' and Sex[i] == ' Male':
        Craft_repairAndMale.append(Others[i])
    elif Others[i] == ' Sales' and Sex[i] == ' Male':
        SalesAndMale.append(Others[i])
    elif Others[i] == ' Exec-managerial' and Sex[i] == ' Male':
        Exec_managerialAndMale.append(Others[i])
    elif Others[i] == ' Handlers-cleaners' and Sex[i] == ' Male':
        Handlers_cleanersAndMale.append(Others[i])
    elif Others[i] == ' Transport-moving' and Sex[i] == ' Male':
        Transport_movingAndMale.append(Others[i])
    elif Others[i] == ' Prof-specialty' and Sex[i] == ' Male':
        Prof_specialtyAndMale.append(Others[i])
    elif Others[i] == ' Farming-fishing' and Sex[i] == ' Male':
        Farming_fishingAndMale.append(Others[i])
    elif Others[i] == ' Tech-support' and Sex[i] == ' Male':
        Tech_supportAndMale.append(Others[i])
    elif Others[i] == ' Machine-op-inspct' and Sex[i] == ' Male':
        Machine_op_inspctAndMale.append(Others[i])
    elif Others[i] == ' Protective-serv' and Sex[i] == ' Male':
        Protective_servAndMale.append(Others[i])
    else:
        Other_serviceAndMale.append(Others[i])

pAdm_clericalAndMale = len(Adm_clericalAndMale) / len(Male)
pCraft_repairAndMale = len(Craft_repairAndMale) / len(Male)
pSalesAndMale = len(SalesAndMale) / len(Male)
pExec_managerialAndMale = len(Exec_managerialAndMale) / len(Male)
pHandlers_cleanersAndMale = len(Handlers_cleanersAndMale) / len(Male)
pTransport_movingAndMale = len(Transport_movingAndMale) / len(Male)
pProf_specialtyAndMale = len(Prof_specialtyAndMale) / len(Male)
pFarming_fishingAndMale = len(Farming_fishingAndMale) / len(Male)
pTech_supportAndMale = len(Tech_supportAndMale) / len(Male)
pMachine_op_inspctAndMale = len(Machine_op_inspctAndMale) / len(Male)
pProtective_servAndMale = len(Protective_servAndMale) / len(Male)
pOther_serviceAndMale = len(Other_serviceAndMale) / len(Male)

whiteSkinAndMale = []
blackSkinAndMale = []
asianSkinAndMale = []
EskimoSkinAndMale = []
OtherSkinAndMale = []
for i in range(32560):
    if skinColor[i] == ' White' and Sex[i] == ' Male':
        whiteSkinAndMale.append(skinColor[i])
    elif skinColor[i] == ' Black' and Sex[i] == ' Male':
        blackSkinAndMale.append(skinColor[i])
    elif skinColor[i] == ' Amer-Indian-Eskimo' and Sex[i] == ' Male':
        EskimoSkinAndMale.append(skinColor[i])
    elif skinColor[i] == ' Other' and Sex[i] == ' Male':
        OtherSkinAndMale.append(skinColor[i])
    else:
        asianSkinAndMale.append(skinColor[i])
pwhiteSkinAndMale = len(whiteSkinAndMale) / len(Male)
pblackSkinAndMale = len(blackSkinAndMale) / len(Male)
pasianSkinAndMale = len(asianSkinAndMale) / len(Male)
pEskimoSkinAndMale = len(EskimoSkinAndMale) / len(Male)
pOtherSkinAndMale = len(OtherSkinAndMale) / len(Male)

# ------ female -------
BachelorsAndFemale = []
Hs_guardAndFemale = []
th11AndFemale = []
MastersAndFemale = []
th9AndFemale = []
someCollageAndFemale = []
Assoc_acdmAndFemale = []
Assoc_vocAndFemale = []
prof_SchoolAndFemale = []
th7_th8AndFemale = []
th10AndFemale = []
st1_th4AndFemale = []
th5_th6AndFemale = []
th12AndFemale = []
PreschoolAndFemale = []
DoctorateAndFemale = []
for i in range(32560):
    if Education[i] == ' Bachelors' and Sex[i] == ' Female':
        BachelorsAndFemale.append(Education[i])
    elif Education[i] == ' HS-grad' and Sex[i] == ' Female':
        Hs_guardAndFemale.append(Education[i])
    elif Education[i] == ' 11th' and Sex[i] == ' Female':
        th11AndFemale.append(Education[i])
    elif Education[i] == ' Masters' and Sex[i] == ' Female':
        MastersAndFemale.append(Education[i])
    elif Education[i] == ' 9th' and Sex[i] == ' Female':
        th9AndFemale.append(Education[i])
    elif Education[i] == ' Some-college' and Sex[i] == ' Female':
        someCollageAndFemale.append(Education[i])
    elif Education[i] == ' Assoc-acdm' and Sex[i] == ' Female':
        Assoc_acdmAndFemale.append(Education[i])
    elif Education[i] == ' Assoc-voc' and Sex[i] == ' Female':
        Assoc_vocAndFemale.append(Education[i])
    elif Education[i] == ' Prof-school' and Sex[i] == ' Female':
        prof_SchoolAndFemale.append(Education[i])
    elif Education[i] == ' 7th-8th' and Sex[i] == ' Female':
        th7_th8AndFemale.append(Education[i])
    elif Education[i] == ' 10th' and Sex[i] == ' Female':
        th10AndMale.append(Education[i])
    elif Education[i] == ' 1st-4th' and Sex[i] == ' Female':
        st1_th4AndFemale.append(Education[i])
    elif Education[i] == ' 5th-6th' and Sex[i] == ' Female':
        th5_th6AndFemale.append(Education[i])
    elif Education[i] == ' 12th' and Sex[i] == ' Female':
        th12AndFemale.append(Education[i])
    elif Education[i] == ' Preschool' and Sex[i] == ' Female':
        PreschoolAndFemale.append(Education[i])
    else:
        DoctorateAndFemale.append(Education[i])
pBachelorsAndFemale = len(BachelorsAndFemale) / len(Female)
pHs_guardAndFemale = len(Hs_guardAndFemale) / len(Female)
pth11AndFemale = len(th11AndFemale) / len(Female)
pMastersAndFemale = len(MastersAndFemale) / len(Female)
pth9AndFemale = len(th9) / len(Female)
psomeCollageAndFemale = len(someCollageAndFemale) / len(Female)
pAssoc_acdmAndFemale = len(Assoc_vocAndFemale) / len(Female)
pAssoc_vocAndFemale = len(Assoc_vocAndFemale) / len(Female)
pprof_SchoolAndFemale = len(prof_SchoolAndFemale) / len(Female)
pth7_th8AndFemale = len(th7_th8AndFemale) / len(Female)
pth10AndFemale = len(th10AndFemale) / len(Female)
pst1_th4AndFemale = len(st1_th4AndFemale) / len(Female)
pth5_th6AndFemale = len(th5_th6AndFemale) / len(Female)
pth12AndFemale = len(th12AndFemale) / len(Female)
pPreschoolAndFemale = len(PreschoolAndFemale) / len(Female)
pDoctorateAndFemale = len(DoctorateAndFemale) / len(Female)

Married_civ_spouseAndFemale = []
Never_marriedAndFemale = []
DivorcedAndFemale = []
SeperatedAndFemale = []
Married_spouse_absentAndFemale = []
Married_AF_spousAndFemale = []
WidowedAndFemale = []
for i in range(32560):
    if Status[i] == ' Married-civ-spouse' and Sex[i] == ' Female':
        Married_civ_spouseAndFemale.append(Status[i])
    elif Status[i] == ' Never-married' and Sex[i] == ' Female':
        Never_marriedAndFemale.append(Status[i])
    elif Status[i] == ' Divorced' and Sex[i] == ' Female':
        DivorcedAndFemale.append(Status[i])
    elif Status[i] == ' Married-spouse-absent' and Sex[i] == ' Female':
        Married_spouse_absentAndFemale.append(Status[i])
    elif Status[i] == ' Widowed' and Sex[i] == ' Female':
        WidowedAndFemale.append(Status[i])
    elif Status[i] == ' Married-AF-spouse' and Sex[i] == ' Female':
        Married_AF_spousAndFemale.append(Status[i])
    else:
        SeperatedAndFemale.append(Status[i])

pMarried_civ_spouseAndFemale = len(Married_civ_spouseAndFemale) / len(Female)
pNever_marriedAndMal = len(Never_marriedAndMal) / len(Female)
pDivorcedAndFemale = len(DivorcedAndFemale) / len(Female)
pSeperatedAndFemale = len(SeperatedAndFemale) / len(Female)
pMarried_spouse_absentAndFemale = len(Married_spouse_absentAndFemale) / len(Female)
pMarried_AF_spousAndFemale = len(Married_AF_spousAndFemale) / len(Female)
pWidowedAndFemale = len(WidowedAndFemale) / len(Female)

Adm_clericalAndFemale = []
Craft_repairAndFemale = []
SalesAndFemale = []
Exec_managerialAndFemale = []
Handlers_cleanersAndFemale = []
Transport_movingAndFemale = []
Prof_specialtyAndFemale = []
Farming_fishingAndFemale = []
Tech_supportAndFemale = []
Machine_op_inspctAndFemale = []
Protective_servAndFemale = []
Other_serviceAndFemale = []
for i in range(32560):
    if Others[i] == ' Adm-clerical' and Sex[i] == ' Female':
        Adm_clericalAndFemale.append(Others[i])
    elif Others[i] == ' Craft-repair' and Sex[i] == ' Female':
        Craft_repairAndFemale.append(Others[i])
    elif Others[i] == ' Sales' and Sex[i] == ' Female':
        SalesAndFemale.append(Others[i])
    elif Others[i] == ' Exec-managerial' and Sex[i] == ' Female':
        Exec_managerialAndFemale.append(Others[i])
    elif Others[i] == ' Handlers-cleaners' and Sex[i] == ' Female':
        Handlers_cleanersAndFemale.append(Others[i])
    elif Others[i] == ' Transport-moving' and Sex[i] == ' Female':
        Transport_movingAndFemale.append(Others[i])
    elif Others[i] == ' Prof-specialty' and Sex[i] == ' Female':
        Prof_specialtyAndFemale.append(Others[i])
    elif Others[i] == ' Farming-fishing' and Sex[i] == ' Female':
        Farming_fishingAndFemale.append(Others[i])
    elif Others[i] == ' Tech-support' and Sex[i] == ' Female':
        Tech_supportAndFemale.append(Others[i])
    elif Others[i] == ' Machine-op-inspct' and Sex[i] == ' Female':
        Machine_op_inspctAndFemale.append(Others[i])
    elif Others[i] == ' Protective-serv' and Sex[i] == ' Female':
        Protective_servAndFemale.append(Others[i])
    else:
        Other_serviceAndFemale.append(Others[i])
pAdm_clericalAndFemale = len(Adm_clericalAndFemale) / len(Female)
pCraft_repairAndFemale = len(Craft_repairAndFemale) / len(Female)
pSalesAndFemale = len(SalesAndFemale) / len(Female)
pExec_managerialAndFemale = len(Exec_managerialAndFemale) / len(Female)
pHandlers_cleanersAndFemale = len(Handlers_cleanersAndFemale) / len(Female)
pTransport_movingAndFemale = len(Transport_movingAndFemale) / len(Female)
pProf_specialtyAndFemale = len(Prof_specialtyAndFemale) / len(Female)
pFarming_fishingAndFemale = len(Farming_fishingAndFemale) / len(Female)
pTech_supportAndFemale = len(Tech_supportAndFemale) / len(Female)
pMachine_op_inspctAndFemale = len(Machine_op_inspctAndFemale) / len(Female)
pProtective_servAndFemale = len(Protective_servAndFemale) / len(Female)
pOther_serviceAndFemale = len(Other_serviceAndFemale) / len(Female)

whiteSkinAndFemale = []
blackSkinAndFemale = []
asianSkinAndFemale = []
EskimoSkinAndFemale = []
OtherSkinAndFemale = []
for i in range(32560):
    if skinColor[i] == ' White' and Sex[i] == ' Female':
        whiteSkinAndFemale.append(skinColor[i])
    elif skinColor[i] == ' Black' and Sex[i] == ' Female':
        blackSkinAndFemale.append(skinColor[i])
    elif skinColor[i] == ' Amer-Indian-Eskimo' and Sex[i] == ' Female':
        EskimoSkinAndFemale.append(skinColor[i])
    elif skinColor[i] == ' Other' and Sex[i] == ' Female':
        OtherSkinAndFemale.append(skinColor[i])
    else:
        asianSkinAndFemale.append(skinColor[i])

pwhiteSkinAndFemale = len(whiteSkinAndFemale) / len(Female)
pblackSkinAndFemale = len(blackSkinAndFemale) / len(Female)
pasianSkinAndFemale = len(asianSkinAndFemale) / len(Female)
pEskimoSkinAndFemale = len(EskimoSkinAndFemale) / len(Female)
pOtherSkinAndFemale = len(OtherSkinAndFemale) / len(Female)
# endregion

