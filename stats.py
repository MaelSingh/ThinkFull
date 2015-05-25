import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
data = data.splitlines()
data = [i.split(', ') for i in data]

column_names = data[0]
data_rows = data[1:]
df = pd.DataFrame(data=data_rows,columns=column_names)

df.Alcohol = df.Alcohol.astype(float)
df.Tobacco = df.Tobacco.astype(float)

print "The mean for Alcohol and Tobacco datasets are %f and %f respectively" % (df.Alcohol.mean(),df.Tobacco.mean())
print "The median for Alcohol and Tobacco datasets are %f and %f respectively" % (df.Alcohol.median(),df.Tobacco.median())
print "The mode for Alcohol and Tobacco datasets are %f and %f respectively" % (stats.mode(df.Alcohol)[0][0],
stats.mode(df.Tobacco)[0][0])
print "The range for Alcohol and Tobacco datasets are %f and %f respectively" % (max(df.Alcohol)-min(df.Alcohol),max(df.Tobacco)-min(df.Tobacco))
print "The variance for Alcohol and Tobacco datasets are %f and %f respectively" % (df.Alcohol.var()
,df.Tobacco.var())
print "The std dev for Alcohol and Tobacco datasets are %f and %f respectively" % (df.Alcohol.std()
,df.Tobacco.std())


