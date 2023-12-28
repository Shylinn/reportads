import os
import pandas as pd
import warnings
warnings.simplefilter("ignore")


# Đổi tên cột acc My
df = pd.read_excel('My-1-ngày.xlsx')
df = df.rename(columns={'Campaign Delivery': 'Campaign delivery'})
df.to_excel('My-1-ngày.xlsx', index=False)



df1 = pd.read_excel('My-1-ngày.xlsx')
df2 = pd.read_excel('TC-1-ngày.xlsx')
df3 = pd.read_excel('Yino-1-ngày.xlsx')
df4 = pd.read_excel('Yino-Tech-1-ngày.xlsx')
merged_df = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)
merged_df.to_excel('Chi-phí-1-ngày.xlsx', index=False)
newdf = pd.read_excel('Chi-phí-1-ngày.xlsx')
for index, row in newdf.iterrows():
    if row['Account name'] == 'Dike - Maximo - Wanderprints 1' or row['Account name'] == 'Dike - Maximo - Wanderprints 2' or row['Account name'] == 'Dike - Maximo - Wanderprints 3' or row['Account name'] == 'Kiet Pets 1' :
        newdf.at[index, 'Attribution setting'] = 1.05 * row['Amount spent (USD)']
    else:
        newdf.at[index, 'Attribution setting'] = row['Amount spent (USD)']
newdf.to_excel('Chi-phí-1-ngày.xlsx', index=False)