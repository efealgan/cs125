

import pandas as pd
import matplotlib.pyplot as plt


file_path = "C:/Users/Niyil/projects/cs125/nilin yaptıkları/dataonspeeches.xlsx"

df = pd.read_excel(file_path)

print(df)  

"""
name, value, frequency yazan yerlere tablomuzdaki variable'lari yazabiliriz. 
mesela barchart'ta value yerine year olabilir.
piechart'ta name yerine gorev ya da yil olabilir.
histogram'da ve plot'ta da keza ayni şekilde
"""

#barchart

plt.figure(1)
plt.bar(df["Speaker"], df["Summary"])
plt.xlabel("Name")
plt.ylabel("Summary")
plt.title("Bar Chart of what people have said")
plt.show()

#piechart
"""
plt.figure(2)
plt.pie(df["Speaker"], labels=df["Summary"], autopct="%1.1f%%")
plt.title("Pie Chart of ...")
plt.show()
"""
#histogram

plt.figure(3)
plt.hist(df["Summary"])
plt.xlabel("Summary")
plt.ylabel("Frequency")
plt.title("Histogram of ...")
plt.show()

#plot

plt.figure(4)
plt.plot(df["Speaker"], df["Summary"], marker="o")
plt.xlabel("Name")
plt.ylabel("Summary")
plt.title("Line Plot of ...")
plt.show()
