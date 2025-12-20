

import pandas as pd
import numpy as np

df_athletes=pd.read_excel("nilin yaptıkları/olympic_athletes.xlsx")
df_athletes=df_athletes.dropna()
df_athletes=df_athletes.sort_values("Country")
df_athletes["medals"]=df_athletes["Gold"]+df_athletes["Silver"]+df_athletes["Bronze"]

#Find the maximum number of medals.
max_medals=np.max(df_athletes["medals"])
print(max_medals)
name_max=df_athletes[df_athletes["medals"]==max_medals]
print("name and sport")
print(name_max[["Athlete","Sport"]])

df_athletes.to_excel("olympic_new.xlsx",index=False)
df_gold=df_athletes[(df_athletes["Gold"]>1)|(df_athletes["Silver"]>1)]


df_china=df_athletes[df_athletes["Country"]=="China"]
df_japan=df_athletes[df_athletes["Country"]=="Japan"]
























