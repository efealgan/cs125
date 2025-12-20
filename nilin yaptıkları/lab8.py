
import pandas as pd
import numpy as np

venue1 = ['Main Library', 'City Museum', 'Art Gallery', 'Cultural Center']
venue2 = ['Community Theater', 'Art Gallery', 'Online Event', 'Cultural Center', 'Main Library']
event1=pd.Series([210, 95, 180, 140],index=venue1)
event2=pd.Series([160, 120, 200, 130, 80],index=venue2)
total_participation=event1+event2
print("Total volunteers:")
print(total_participation)

total_participation=total_participation.fillna(0)
print("\nfirst four rows:")
print(total_participation[0:4])

print("\nvol bw com theatre and online event: ")
print(total_participation["Community Theater": "Online Event"])

print("\nvenues with vol only in one:" )
print(total_participation[total_participation==0].index)

print("\nselected events:")
selected_events=total_participation.drop(["Main Library", "Online Event", "City Museum"])
print(selected_events)



data_2014_2015=pd.read_excel("nilin yaptıkları/lab8888888/data2014_15.xlsx")
data_2013=pd.read_excel("nilin yaptıkları/lab8888888/data2013.xlsx")
merged_data=pd.merge(data_2013,data_2014_2015)
merged_data=merged_data.replace(-1, np.nan)
merged_data=merged_data.dropna()

merged_data["mean"]=np.mean(merged_data[[2013,2014,2015]],axis=1)
merged_data=merged_data.sort_values("mean")
merged_data.to_excel("avg_countries.xlsx",index=None)































