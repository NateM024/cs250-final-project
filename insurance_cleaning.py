import pandas as pd

# import file, read only 2 columns
df = pd.read_excel('insurance_records.xlsx', usecols=['DUPERSID', 'OOPPREMX'])

# inspect dataframe
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.shape)

# remove rows with negative premiums
df = df[df['OOPPREMX'] >= 0] # change to oopx12x for full year

# remove duplicate rows
df.drop_duplicates(subset=['DUPERSID'], inplace=True)

# rename columns
df.rename(columns={'OOPPREMX' : 'MONTHLY_PREMIUM'})

# inspect dataframe
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.shape)

# save new file
df.to_excel('cleaned_insurance_records.xlsx')