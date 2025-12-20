

import pandas as pd
import matplotlib.pyplot as plt


file_path = "your_file_name.xlsx"

df = pd.read_excel(file_path)

print(df)  

"""
name, value, frequency yazan yerlere tablomuzdaki variable'lari yazabiliriz. 
mesela barchart'ta value yerine year olabilir.
piechart'ta name yerine gorev ya da yil olabilir.
histogram'da ve plot'ta da keza ayni şekilde
"""

#barchart

plt.figure()
plt.bar(df["Name"], df["Value"])
plt.xlabel("Name")
plt.ylabel("Value")
plt.title("Bar Chart of ...")
plt.show()

#piechart

plt.figure()
plt.pie(df["Value"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Pie Chart of ...")
plt.show()

#histogram

plt.figure()
plt.hist(df["Value"])
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of ...")
plt.show()

#plot

plt.figure()
plt.plot(df["Date"], df["Value"], marker="o")
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Line Plot of ...")
plt.show()























