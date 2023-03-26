
#Data Pre-processing-------------------------------
import pandas as pd
import pandas_profiling as pp
filedata=pd.read_csv('merc.csv')
print(filedata.info())

print(filedata.describe())

#Building Profile Reports---------------------------------

profilereport=pp.ProfileReport(filedata)
profilereport.to_file('index.html')

#Extracting Duplicate Values------------------------------------
dupdf=filedata[filedata.duplicated()]
print(dupdf)
dupdf.to_excel('duplicate values.xlsx')

