import pandas as pd

a = {'Name': 'Ankit Kothari','Designation': 'AE'}

#====================================
df = pd.DataFrame(a,index=['kirti'])

df.to_csv('Ankit.csv',mode='a',header=True)