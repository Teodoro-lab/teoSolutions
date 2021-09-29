
"-----------central metrics calculations-----------"

import numpy as np 
from scipy import stats

data = np.array([4, 6, 2, 7, 1, 2, 3, 2, 3, 3, 3, 3])
 
# calculate mean

dataMean = np.mean(data)
print("mean is: ", dataMean)

# calculate meadian

dataMedian = np.median(data)
print("median is: ", dataMedian)

# calculate mode

dataMode = stats.mode(data)
print("mode is: ", dataMode[0][0])
print(dataMode[0])
print(dataMode)

"-----------dispersion metrics calculations-----------"

from statistics import variance, stdev

game_points = np.array([35, 65, 23, 75, 12, 42, 64, 11, 23, 24])

# calculate variance

gmVar = variance(game_points)
print("Sample variance: ", round(gmVar, 2))

# calculate standard deviation

gmDev = stdev(game_points)
print("Sample standard deviation: ", round(gmDev, 2))

# calculate range

gmTopRange = np.max(game_points, axis=0)
gmBottomRange = np.min(game_points, axis=0)
print("Game points range: ", gmBottomRange, "-", gmTopRange)

# calculate percentiles

print("Quantiles")
for val in [20, 80, 100]:
	dt_qntls = np.percentile(game_points, val)
	print(str(val)+"%", dt_qntls)

# calculate IQR (interquantile range)

q75, q25 = np.percentile(game_points, [75, 25])
print("interquantile range: ", q75, q25)

"-----------hypothesis and significant values-----------"
#----------chocolate factory example--------#

xbar = 990; mu0 = 1000; s = 12.5; n = 30

# statistic

t_smple = (xbar-mu0)/(s/np.sqrt(float(n)))

# critical value from t-table

alpha = .05	
t_alpha = stats.t.ppf(alpha, n-1);
print("critical value from t-table: ", t_alpha)

# lower tail p-value from t-table

p_val = stats.t.sf(np.abs(t_smple), n-1)
print("Lower tail p-value from t-table: ", p_val)

"-----------normal distribution-----------"

xbar = 67; mu0 = 52; s = 16.3

# calculating z-score

z = (67-52)/16.3

# calculating probability under the curve

p_val = 1 - stats.norm.cdf(z)
print("Probability to score more than 67 is", round(p_val*100, 2), "%")	

"-----------chi-square independence test-----------"

import pandas as pd 

survey = pd.read_csv("survey.csv")

# Tabulating 2 variables with row and column variables

survey_tab = pd.crosstab(survey.Smoke, survey.Exer, margins = True)

# Creating observed table for analysis

observed = survey_tab.ix[0:4, 0:3]