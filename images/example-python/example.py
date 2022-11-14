### Import Libraries

import pandas as pd
from pathlib import Path
import json
####End of importing libraries


pathCurrrent = Path.cwd()


pathCurrrent = str(pathCurrrent).replace("\\", '/')


dfPe = pd.read_csv("people.csv")
dfPl = pd.read_csv("places.csv" )


#####################################################Creat JSON file
a=pd.concat([dfPl.iloc[:,0], dfPl.iloc[:,1]], ignore_index=True,axis=0)#city1 + city2
b=pd.concat([dfPl.iloc[:,2], dfPl.iloc[:,2]], ignore_index=True,axis=0)#country

dfPl=pd.concat([a,b],axis=1)


dfPl.rename(columns={dfPl.columns[0]: 'city'}, inplace=True)
dfPe.rename(columns={dfPe.columns[-1]: 'city'}, inplace=True)


dfPedfPl=pd.merge(dfPe,dfPl, on='city')

dfG=dfPedfPl.groupby(by=["country"])["country"].count()

with open('example_python.json', 'w') as f:
   row = {dfG.index[0]: dfG[0], dfG.index[1]: dfG[1]}
   json.dump(row, f, default=str)

print("\nName and number of each country is saved in example_python.json file!!!")

#####################################################


#####################################################Save CSVs in Database
from sqlalchemy import create_engine

dfPe = pd.read_csv("people.csv")
dfPl = pd.read_csv("places.csv" )

engine = create_engine('mysql+pymysql://root:1333@localhost/codetest') # enter your password and database names here


dfPl.to_sql('places',con=engine,index=False,if_exists='append') # Rep
print("\nData is saved in table dfPl")



dfPe.to_sql('people',con=engine,index=False,if_exists='append') # Rep
print("\nData is saved in table dfPe")




