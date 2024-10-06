import pandas as pd

temp_arr = [12.21, 12.43, 13.06, 13.98, 14.94, 15.65, 15.92, 15.75, 15.18, 14.25, 13.23, 12.48]

df = pd.read_csv('temperature.csv')

df.drop('Anomaly.1', axis=1, inplace=True)
df.drop('Unc..1', axis=1, inplace=True)

abs_temp = []

for(i) in range(df.shape[0]):
    abs_temp.append(temp_arr[df['Month'][i] - 1] + df['Anomaly'][i])

df['Abs_Temp'] = abs_temp

df1=df[['Year', 'Month','Abs_Temp']]

df1.to_csv('abs_temperature.csv', index=False)