
import pandas as pd
import numpy as np
"""
fruits=["Apple", "Pear", "Cherry","Pineapple"]
quantities_1=[1,2,3,4]
s1=pd.Series([1,2,3,4], index=fruits)
s2=pd.Series([5,6,7,8],index=fruits)
s3=s1+s2
print(s3)
"""

"""

years=range(2021,2025)
product_1=pd.Series([1,2,3,4])
product_2=pd.Series([5,6,7,8])

fruits1=["Apples", "Pears"]
fruits_2=["Apples", "Cherries"]
s1=pd.Series([1,2], index=fruits1)
s2=pd.Series([5,6],index=fruits_2)
s3=s1+s2
print(s3)
s4=s3.dropna()
print(s4)
s5=s3.fillna(2)
print(s5)

print(s5["Cherries"])
"""
"""
years=range(2021,2025)
product_1=pd.Series([1,2,3,4],index=years)
product_2=pd.Series([5,6,7,8], index=years)
product_data=pd.DataFrame({"p1":product_1,"p2":product_2})
print(product_data)
product_data["p3"]=(15,99,88,83)
print(product_data)

product_data=product_data.drop(["p1"],axis=1)
print(product_data)
"""

"""
product_a = pd.Series(

    [150, 200, np.nan, 180, 220],

    index=["Mon", "Tue", "Wed", "Thu", "Fri"])

product_b = pd.Series(

    [100, np.nan, 160, 140, 200],

    index=["Mon", "Tue", "Wed", "Thu", "Fri"])


s3=product_a+product_b
s3=s3.dropna()
print(s3)
"""
"""
sales_2022 = pd.Series([500, 300, 450], index=["Laptop", "Phone", "Tablet"])
sales_2023 = pd.Series([550, 350, 400], index=["Laptop", "Phone", "Tablet"])
sales_2024 = pd.Series([600, 400, 500], index=["Laptop", "Phone", "Tablet"])

dfe=pd.DataFrame({"2022":sales_2022,"2023":sales_2023,"2024":sales_2024})
print(dfe)
dfe["avg"]=np.mean(dfe,axis=1)
dfe=dfe.sort_values("avg",ascending=False)
print(dfe)
"""

gdp=pd.DataFrame({"Germany": 4200, "France": 2900, "Italy": 2100, "Spain":1400},index=None)
pop=pd.DataFrame({"Germany": 83, "France": 67, "Spain": 47,"Netherlands": 17})
df=pd.merge(left=gdp,right=pop,left_on="Country", right_on="Country")
gpd_per_capita=gdp/pop
print(df)



























