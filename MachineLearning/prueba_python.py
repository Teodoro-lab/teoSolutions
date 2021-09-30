import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("./data-sets/cleansingWine.csv")
print(df.head().T)
print(df["price"].describe())





def pieSweetGrade():
	def percentage(pct):
		return f'{round(pct, 2)}%'

	sweetCategories = df.groupby("sweet").size()
	sweetCategoriesCount = []
	for sweetGrade in sweetCategories.keys():
		sweetCategoriesCount.append(sweetCategories[f'{sweetGrade}'])

	sweetCategories = sweetCategories.keys().to_numpy()
	explodes = [.2] + [0]*(len(sweetCategoriesCount) - 1)
	plt.pie(sweetCategoriesCount, 
		labels=sweetCategories, 
		explode=explodes, 
		shadow=True,
		autopct=lambda pct: percentage(pct)
		)
	plt.legend(title="Wine sweet categories")
	plt.show()
