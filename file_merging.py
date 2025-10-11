import pandas as pd

# load datasets
df1 = pd.read_excel('cleaned_insurance_records.xlsx')
df2 = pd.read_excel('cleaned_person_records.xlsx')

# rename premium column
df1.rename({'OOPPREMX' : 'MONTHLY_PREMIUM'}, inplace=True)

# merge datasets on DUPERSID, inner join
df3 = pd.merge(df1, df2, on='DUPERSID', how='inner')

# drop indexes added as variables
df3.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1, inplace=True)

# inspect new dataset
print(df3.head())
print(df3.info())
print(df3.tail())
print(df3.shape)

# save new dataset
df3.to_excel('merged_data.xlsx')