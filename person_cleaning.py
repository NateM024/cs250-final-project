import pandas as pd

#identify columns to use
use_columns = ['DUPERSID', 'FAMSZE31', 'REGION31', 'AGE31X', 'SEX', 'RACEV2X', 'MARRY31X', 'EDUCYR', 'HIDEG', 'FTSTU23X', 'EVERSERVED', 'ACTDTY31', 'OTHLGSPK', 'WHTLGSPK', 
               'BORNUSA', 'HIBPDX', 'CHDDX', 'ANGIDX', 'MIDX', 'OHRTDX', 'STRKDX', 'EMPHDX', 'CHOLDX', 'CANCERDX', 'CABLADDR', 'CABREAST', 'CACERVIX', 'CACOLON', 
               'CALUNG', 'CALYMPH', 'CAMELANO', 'CAOTHER', 'CAPROSTA', 'CASKINNM', 'CASKINDK', 'CAUTERUS', 'DIABDX_M18', 'JTPAIN31_M18', 'ARTHDX', 'ASTHDX','RTHLTH31',
               'MNHLTH31', 'COVIDEVER31', 'LCEVER31', 'COVAXEVR31', 'WLKLIM31', 'ACTLIM31','SOCLIM31','COGLIM31', 'OFTSMK53', 'EMPST31H', 'FOODST23', 'TTLP23X', 'FAMINC23', 
               'CHLDP23X', 'POVCAT23', 'INTRP23X', 'SSECP23X', 'ALIMP23X', 'BUSNP23X', 'DIVDP23X', 'SALEP23X', 'TRSTP23X', 'PENSP23X', 'IRASP23X', 'UNEMP23X', 'WCMPP23X', 'VETSP23X', 
               'CASHP23X', 'OTHRP23X', 'SSIP23X', 'PUBP23X', 'INSCOV23', 'PRIV31', 'TRI31X', 'MCARE31X', 'MCAID31X', 'VAPROG31', 'GOVTA31', 'IHSAT31', 'PRIEU31', 'DENTIN31_M23', 'PMEDIN31']

# import dataset
df = pd.read_excel('person_records.xlsx', usecols=use_columns)

print('loaded the dataset')

# inspect data
print(df.head())
print(df.info())
print(df.tail())
print(df.shape)

# rename columns not being transformed
df.rename(columns={ 'FAMSZE31' : 'FAMILY_SIZE',
                    'AGE31X' : 'AGE',
                    'TTLP23X' : 'TOTAL_INCOME', 
                    'FAMINC23' : 'FAMILY_INCOME',
                    'INTRP23X' : 'INTEREST_INCOME',
                    'BUSNP23X' : 'BUSINESS_INCOME',
                    'DIVDP23X' : 'DIVIDEND_INCOME',
                    'SALEP23X' : 'SALES_INCOME',
                    'TRSTP23X' : 'TRUST/RENT_INCOME',
                    'PENSP23X' : 'PENSION_INCOME',
                    'IRASP23X' : 'IRA_INCOME',
                    'SSECP23X' : 'SOCIAL_SECURITY_INCOME',
                    'UNEMP23X' : 'UNEMPLOYMENT_INCOME',
                    'VETSP23X' : 'VETERAN_INCOME',
                    'ALIMP23X' : 'ALIMONY_INCOME',
                    'WCMPP23X' : 'WORKERS_COMPENSATION',
                    'CASHP23X' : 'REGULAR_CASH_CONTRIBUTION',
                    'OTHRP23X' : 'OTHER_INCOME',
                    'CHLDP23X' : 'CHILD_SUPPORT',
                    'SSIP23X' : 'SSI_INCOME',
                    'PUBP23X' : 'PUBLIC_ASSISTANCE'}, inplace=True)

# remove the 294 people with constant, reoccuring responses of -1 (inapplicable)
df = df[df['FAMILY_SIZE'] != -1] # note: the same 294 occur w/ -1 in more than just this column
print('Rows: ', len(df))

# transform the region column column
df['NORTHEAST'] = (df['REGION31'] == 1).astype(int)
df['MIDWEST'] = (df['REGION31'] == 2).astype(int)
df['SOUTH'] = (df['REGION31'] == 3).astype(int)
df['WEST'] = (df['REGION31'] == 4).astype(int)
df.drop('REGION31', axis=1, inplace=True)

# transform sex column column
df['MALE'] = (df['SEX'] == 1).astype(int)
df.drop('SEX', axis=1, inplace=True)

#transform race column column
df['WHITE'] = (df['RACEV2X'] == 1).astype(int)
df['BLACK'] = (df['RACEV2X'] == 2).astype(int)
df['AMERICAN_INDIAN'] = (df['RACEV2X'] == 3).astype(int)
df['ASIAN_INDIAN'] = (df['RACEV2X'] == 4).astype(int)
df['CHINESE'] = (df['RACEV2X'] == 5).astype(int)
df['FILIPINO'] = (df['RACEV2X'] == 6).astype(int)
df['OTHER_ASIAN'] = (df['RACEV2X'] == 10).astype(int)
df['MULTIRACIAL'] = (df['RACEV2X'] == 12).astype(int)
df.drop('RACEV2X', axis=1, inplace=True)

# transforom the marriage column column
df['MARRIED'] = (df['MARRY31X'] == 1).astype(int)
df['WIDOWED'] = (df['MARRY31X'] == 2).astype(int)
df['DIVORCED'] = (df['MARRY31X'] == 3).astype(int)
df['SEPARATED'] = (df['MARRY31X'] == 4).astype(int)
df['NEVER_MARRIED'] = ((df['MARRY31X'] == 5) | (df['MARRY31X'] == 6)).astype(int)
df.drop('MARRY31X', axis=1, inplace=True)

# transform the education column column
df['NO_EDUCATION'] = (df['EDUCYR'] == 0).astype(int)
df['GRADES_1-8'] = ((df['EDUCYR'] >= 1) & (df['EDUCYR'] <= 8)).astype(int)
df['HIGH_SCHOOL'] = ((df['EDUCYR'] >= 9) & (df['EDUCYR'] <= 12)).astype(int)
df['COLLEGE'] = ((df['EDUCYR'] >= 13) & (df['EDUCYR'] <= 17)).astype(int)
df.drop('EDUCYR', axis=1, inplace=True)

# transform highest degree column
df['NO_DEGREE'] = (df['HIDEG'] == 1).astype(int)
df['GED'] = (df['HIDEG'] == 2).astype(int)
df['HIGH_SCHOOL_DIPLOMA'] = (df['HIDEG'] == 3).astype(int)
df['BACHELORS'] =(df['HIDEG'] == 4).astype(int)
df['MASTERS'] = (df['HIDEG'] == 5).astype(int)
df['DOCTORATE'] = (df['HIDEG'] == 6).astype(int)
df['OTHER_DEGREE'] = (df['HIDEG'] == 7).astype(int)
df.drop('HIDEG', axis=1, inplace=True)

# transform college student column
df['FULL_TIME_COLLEGE'] = (df['FTSTU23X'] == 1).astype(int) 
df['PART_TIME_COLLEGE'] = (df['FTSTU23X'] == 2).astype(int)
df['NOT_COLLEGE_STUDENT'] = (df['FTSTU23X'].isin([3, -1, -7, -8])).astype(int) 
df.drop('FTSTU23X', axis=1, inplace=True)

# transform served in military column
df['MILITARY_SERVICE'] = (df['EVERSERVED'] == 1).astype(int)
df.drop('EVERSERVED', axis=1, inplace=True)

# transform active duty column
df['CURRENTLY_IN_MILITARY'] = (df['ACTDTY31'] == 1).astype(int)
df['CURRENTLY_NOT_IN_MILITARY'] = (df['ACTDTY31'].isin([2, -7, -8])).astype(int)
df['TOO_YOUNG/OLD_FOR_MILITARY'] = (df['ACTDTY31'].isin([3,4])).astype(int)
df.drop('ACTDTY31', axis=1, inplace=True)

# transform speaks other language at home column
df['OTHER_LANGUAGE_AT_HOME'] = (df['OTHLGSPK'] == 1).astype(int)
df.drop('OTHLGSPK', axis=1, inplace=True)

# transform langauges spoken column
df['ENGLISH_ONLY'] = (df['WHTLGSPK'] == -1).astype(int)
df['ENGLISH_SPANISH'] = (df['WHTLGSPK'] == 2).astype(int)
df['ENGLISH_OTHER'] = (df['WHTLGSPK'] == 3).astype(int)
df['TOO_YOUNG_TO_SPEAK'] = (df['WHTLGSPK'] == 5).astype(int)
df.drop('WHTLGSPK', axis=1, inplace=True)

# transform born in usa column column
df['BORN_IN_USA'] = (df['BORNUSA'] == 1).astype(int)
df.drop('BORNUSA', axis=1, inplace=True)

# transform high blood pressure column
df['HIGH_BLOOD_PRESSURE'] = (df['HIBPDX'] == 1).astype(int)
df.drop('HIBPDX', axis=1, inplace=True)

# transform coronary heart disease column
df['CORONARY_HEART_DISEASE'] = (df['CHDDX'] == 1).astype(int)
df.drop('CHDDX', axis=1, inplace=True)

# transform angina diagnosis column
df['ANGINA'] = (df['ANGIDX'] == 1).astype(int)
df.drop('ANGIDX', axis=1, inplace=True)

# transform heart attack column
df['HEART_ATTACK'] = (df['MIDX'] == 1).astype(int)
df.drop('MIDX', axis=1, inplace=True)

# transform other heart issues column
df['OTHER_HEART_DISEASE'] = (df['OHRTDX'] == 1).astype(int)
df.drop('OHRTDX', axis=1, inplace=True)

# transform stroke column
df['STROKE'] = (df['STRKDX'] == 1).astype(int)
df.drop('STRKDX', axis=1, inplace=True)

# transform emphysema column
df['EMPHYSEMA'] = (df['EMPHDX'] == 1).astype(int)
df.drop('EMPHDX', axis=1, inplace=True)

# transform high cholesterol column
df['HIGH_CHOLESTEROL'] = (df['CHOLDX'] == 1).astype(int)
df.drop('CHOLDX', axis=1, inplace=True)

# transform cancer diagnosis column
df['CANCER_DIAGNOSIS'] = (df['CANCERDX'] == 1).astype(int)
df.drop('CANCERDX', axis=1, inplace=True)

# transform bladder cancer column
df['BLADDER_CANCER'] = (df['CABLADDR'] == 1).astype(int)
df.drop('CABLADDR', axis=1, inplace=True)

# transform breast cancer column
df['BREAST_CANCER'] = (df['CABREAST'] == 1).astype(int)
df.drop('CABREAST', axis=1, inplace=True)

# transform cervical cancer column
df['CERVICAL_CANCER'] = (df['CACERVIX'] == 1).astype(int)
df.drop('CACERVIX', axis=1, inplace=True)

# transform colon cancer column
df['COLON_CANCER'] = (df['CACOLON'] == 1).astype(int)
df.drop('CACOLON', axis=1, inplace=True)

# transform lung cancer column
df['LUNG_CANCER'] = (df['CALUNG'] == 1).astype(int)
df.drop('CALUNG', axis=1, inplace=True)

# transform lymphoma cancer column
df['LYMPHOMA_CANCER'] = (df['CALYMPH'] == 1).astype(int)
df.drop('CALYMPH', axis=1, inplace=True)

# transform skin melanoma cancer column
df['SKIN_MELANOMA_CANCER'] = (df['CAMELANO'] == 1).astype(int)
df.drop('CAMELANO', axis=1, inplace=True)

# transform other cancer column
df['OTHER_CANCER'] = (df['CAOTHER'] == 1).astype(int)
df.drop('CAOTHER', axis=1, inplace=True)

# transform prostate cancer column
df['PROSTATE_CANCER'] = (df['CAPROSTA'] == 1).astype(int)
df.drop('CAPROSTA', axis=1, inplace=True)

# transform skin nonmelanoma cancer column
df['SKIN_NONMELANOMA_CANCER'] = (df['CASKINNM'] == 1).astype(int)
df.drop('CASKINNM', axis=1, inplace=True)

# transform other skin cancer column
df['UNKNOWN_SKIN_CANCER'] = (df['CASKINDK'] == 1).astype(int)
df.drop('CASKINDK', axis=1, inplace=True)

# transform uterine cancer column
df['UTERINE_CANCER'] = (df['CAUTERUS'] == 1).astype(int)
df.drop('CAUTERUS', axis=1, inplace=True)

# transform diabetes column
df['DIABETES'] = (df['DIABDX_M18'] == 1).astype(int)
df.drop('DIABDX_M18', axis=1, inplace=True)

# transform joint pain column
df['JOINT_PAIN'] = (df['JTPAIN31_M18'] == 1).astype(int)
df.drop('JTPAIN31_M18', axis=1, inplace=True)

# transform arthritis column
df['ARTHRITIS'] = (df['ARTHDX'] == 1).astype(int)
df.drop('ARTHDX', axis=1, inplace=True)

# transform asthma column
df['ASTHMA'] = (df['ASTHDX'] == 1).astype(int)
df.drop('ASTHDX', axis=1, inplace=True)

# transform ever had COVID column
df['HAD_COVID'] = (df['COVIDEVER31'] == 1).astype(int)
df.drop('COVIDEVER31', axis=1, inplace=True)

# transform ever recieved COVID vaccination column
df['COVID_VAX_EVER'] = (df['COVAXEVR31'] == 1).astype(int)
df.drop('COVAXEVR31', axis=1, inplace=True)

# transform ever had long COVID column
df['HAD_LONG_COVID'] = (df['LCEVER31'] == 1).astype(int)
df.drop('LCEVER31', axis=1, inplace=True)

# transform percieved health columns
## account for negative values
df['RTHLTH31'] = df[df['RTHLTH31'] > 0]['RTHLTH31']
df['RTHLTH31'] = df['RTHLTH31'].fillna(value=df['RTHLTH31'].median())
## categorize 
df['EXCELLENT_HEALTH'] = (df['RTHLTH31'] == 1).astype(int)
df['VERY_GOOD_HEALTH'] = (df['RTHLTH31'] == 2).astype(int)
df['GOOD_HEALTH'] = (df['RTHLTH31'] == 3).astype(int)
df['FAIR_HEALTH'] = (df['RTHLTH31'] == 4).astype(int)
df['POOR_HEALTH'] = (df['RTHLTH31'] == 5).astype(int)
## drop column
df.drop('RTHLTH31', axis=1, inplace=True)

# transform percieved mental health columns
## account for negative values
df['MNHLTH31'] = df[df['MNHLTH31'] > 0]['MNHLTH31']
df['MNHLTH31'] = df['MNHLTH31'].fillna(value=df['MNHLTH31'].median())
## categorize 
df['EXCELLENT_MENTAL_HEALTH'] = (df['MNHLTH31'] == 1).astype(int)
df['VERY_GOOD_MENTAL_HEALTH'] = (df['MNHLTH31'] == 2).astype(int)
df['GOOD_MENTAL_HEALTH'] = (df['MNHLTH31'] == 3).astype(int)
df['FAIR_MENTAL_HEALTH'] = (df['MNHLTH31'] == 4).astype(int)
df['POOR_MENTAL_HEALTH'] = (df['MNHLTH31'] == 5).astype(int)
## drop column
df.drop('MNHLTH31', axis=1, inplace=True)

# transform limitation in physical functioning column
df['PHYSICAL_LIMITATIONS'] = (df['WLKLIM31'] == 1).astype(int)
df.drop('WLKLIM31', axis=1, inplace=True)

# transform limitation in physical functioning column
df['WORK/HOUSE/SCHOOL_LIMIATION'] = (df['ACTLIM31'] == 1).astype(int)
df.drop('ACTLIM31', axis=1, inplace=True)

# transform limitation in physical functioning column
df['SOCIAL_LIMITATION'] = (df['SOCLIM31'] == 1).astype(int)
df.drop('SOCLIM31', axis=1, inplace=True)

# transform limitation in physical functioning column
df['COGNITIVE_LIMITATION'] = (df['COGLIM31'] == 1).astype(int)
df.drop('COGLIM31', axis=1, inplace=True)

# transform smoking frequency column
df['SMOKES_EVERYDAY'] = (df['OFTSMK53'] == 1).astype(int)
df['SMOKES_SOME_DAYS'] = (df['OFTSMK53'] == 2).astype(int)
df['NEVER_SMOKES'] = ((df['OFTSMK53'].isin([3, -7, -8])) | ((df['AGE'] >= 17) & (df['OFTSMK53'] == -1))).astype(int)
df['TOO_YOUNG_TO_SMOKE'] = (df['AGE'] < 17).astype(int) # only people over 17 were asked about smoking

# transform employed column
df['EMPLOYED'] = ((df['EMPST31H'] == 1) | (df['EMPST31H'] == 2)).astype(int)
df['TOO_YOUNG_TO_WORK'] = (df['AGE'] <= 15).astype(int) # only people over 15 were asked about employment
df.drop('EMPST31H', axis=1, inplace=True)

# transform food stamps column
df['PURCHASED_FOOD_STAMPS'] = (df['FOODST23'] == 1).astype(int)
df.drop('FOODST23', axis=1, inplace=True)

# transform poverty column
df['POOR'] = (df['POVCAT23'] == 1).astype(int)
df['NEAR_POOR'] = (df['POVCAT23'] == 2).astype(int)
df['LOW_INCOME'] = (df['POVCAT23'] == 3).astype(int)
df['MIDDLE_INCOME'] = (df['POVCAT23'] == 4).astype(int)
df['HIGH_INCOME'] = (df['POVCAT23'] == 5).astype(int)
df.drop('POVCAT23', axis=1, inplace=True)

# transform private/public insurance column
df['ANY_PRIVATE_INSURANCE'] = (df['INSCOV23'] == 1).astype(int)
df['ONLY_PUBLIC_INSURANCE'] = (df['INSCOV23'] == 2).astype(int)
df['NO_INSURANCE'] = (df['INSCOV23'] == 3).astype(int)
df.drop('INSCOV23', axis=1, inplace=True)

# transform private insurance coverage column
df['PRIVATE_COVERAGE'] = (df['PRIV31'] == 1).astype(int)
df.drop('PRIV31', axis=1, inplace=True)

# transform tricare/champva coverage column
df['TRICARE_COVERAGE'] = (df['TRI31X'] == 1).astype(int)
df['CHAMPVA_COVERAGE'] = (df['TRI31X'] == 2).astype(int)
df.drop('TRI31X', axis=1, inplace=True)

# transform medicare coverage column
df['MEDICARE_COVERAGE'] = (df['MCARE31X'] == 1).astype(int)
df.drop('MCARE31X', axis=1, inplace=True)

# transform medicaid coverage column
df['MEDICAID/SCHIP_COVERAGE'] = (df['MCAID31X'] == 1).astype(int)
df.drop('MCAID31X', axis=1, inplace=True)

# transform veteran affairs coverage column
df['VETERAN_AFFAIRS_COVERAGE'] = (df['VAPROG31'] == 1).astype(int)
df.drop('VAPROG31', axis=1, inplace=True)

# transform indian health service coverage
df['INDIAN_HEALTH_SERVICE_COVERAGE'] = (df['IHSAT31'] == 1).astype(int)
df.drop('IHSAT31', axis=1, inplace=True)

# transform other public coverage column
df['OTHER_PUBLIC_COVERAGE'] = (df['GOVTA31'] == 1).astype(int)
df.drop('GOVTA31', axis=1, inplace=True)

# transform covered by employer/union column
df['COVERED_BY_EMPLOYER/UNION'] = (df['PRIEU31'] == 1).astype(int)
df.drop('PRIEU31', axis=1, inplace=True)

# transform private insurance with dental coverage column
df['PRIVATE_WITH_DENTAL'] = (df['DENTIN31_M23'] == 1).astype(int)
df.drop('DENTIN31_M23', axis=1, inplace=True)

# transform private insurance with perscription drug coverage column
df['PRIVATE_WITH_PERSCRIPTION_DRUGS'] = (df['PMEDIN31'] == 1).astype(int)
df.drop('PMEDIN31', axis=1, inplace=True)

# inspect cleaned data
print(df.head())
print(df.info())
print(df.tail())

# save data to a new file
df.to_excel('cleaned_person_records.xlsx')
