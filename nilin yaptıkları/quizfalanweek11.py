

import pandas as pd
import numpy as np


data=pd.read_excel("nilin yaptıkları/movies.xlsx")
df=pd.DataFrame(data)

print("Display rows with indexes 5 and 50, first and third columns")
print(df.iloc[[5,50],[0,2]])

print("\nDisplay all movies directed by Steven Spielberg")
directed_by_steven=df[df.director=="Steven Spielberg"]
print(directed_by_steven)

avg=np.mean(directed_by_steven.rating)
print("\nAverage rating of Spielberg movies: ", avg)

bw_eight=directed_by_steven[(directed_by_steven.rating>8)&(directed_by_steven.rating<8.5)]
print("\nDisplay all movies directed by Steven Spielberg with ratings between 8 and 8.5")
print(bw_eight)

directed_by_francis=df[df.director=="Francis Ford Coppola"]


# steven=directed_by_steven[(directed_by_steven.release_year>1970)|(directed_by_steven.release_year<1990)]
# francis=directed_by_francis[(directed_by_francis.release_year>1970)|(directed_by_francis.release_year<1990)]
print("Display all movies directed by Francis Ford Coppola or Steven Spielberg released in the 1970s or 1980s")
release=df[((df.director=="Francis Ford Coppola")|(df.director=="Steven Spielberg"))&((df.release_year>=1970)&(df.release_year<1990))]
print(release)


name = df.loc[df["rating"].idxmax(), "movie"]
director = df.loc[df["rating"].idxmax(), "director"]

print(f"The movie \"{name}\" is directed by {director} and has a rating of {df["rating"].max()}.")






















