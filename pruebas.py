import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np

nombres = pd.Series(["Samuel", "Teo", "Rodro", "Willy", "Jorge", "Kary"])
age = pd.Series([19, 20, 19, 19, 19, 18])

df = pd.DataFrame({
        "Nombres": nombres,
        "Ages": age
    })

df["Carrera"] = "SoftwareEng"
df.at[1, "Ages"] = 19
numFilas = len(df)
df.loc[numFilas] = ["Cambra", 21, "Dr.CS"]
dfSorted = df.sort_values("Ages", ascending=False)
#print(dfSorted,"\n"*2)
#print(df)
df[ df["Ages"] <=20 ]
#print(df[ df["Nombres"].str.len() <= 3 ])
df["Number"] = np.nan
df["Experience"] = np.nan
#print(df)
df["Ages"].sum() # mean - mode - meadian
#print(df.head())
df = df.drop(["Number", "Experience"], axis=1)
#df = df.dropna(axis=0)

#print(df[df["Nombres"] == "Teo"]["Nombres"])
df["Experience"] = [2, 4, 3, 1, 6, 1, 9]
df["numberWorks"] = [1, 3, 4, 2, 3, 1, 2]

# number of works per year of experience
df["Works/Year"] = round((df["Experience"] / df["numberWorks"]).astype(float),2)
#print("Mean Experience Years", round(df["Experience"].mean(), 2) )
print(df.head())

print("Trabajos que ha tenido por cada año de experience: ", df[ df["Nombres"]=="Teo"]["Works/Year"])

df.at[df[ df["Nombres"]=="Rodro" ].index, "numberWorks"] = 0
print(df[ df["Nombres"]=="Rodro" ])
"""plt.plot(dfplt.show()
"""


"""
find(
	{
		{"prop":2}{"$":10}
	}
)
	
{
	"$and":[{"prop":2}, {"prop":3}]
}

"""
