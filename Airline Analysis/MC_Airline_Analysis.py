import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import statsmodels

airline_data = pd.read_csv("F:/Codecademy/Exercises/Airline Analysis/flight.csv")
print(airline_data.head())
print(airline_data.info())


flight_price = airline_data.coach_price

#task 1: entender a distribuição dos preços de passagens
np.mean(flight_price)
print("25% dos preços de passagens: " + str(np.percentile(flight_price, 25)))
print("50% dos preços de passagens: " + str(np.percentile(flight_price, 50)))
print("75% dos preços de passagens: " + str(np.percentile(flight_price, 75)))

np.min(flight_price)
np.max(flight_price)
np.median(flight_price)

sns.boxplot(x = "coach_price", data = airline_data)
plt.show()
plt.clf()

#task 2
sns.histplot(airline_data.coach_price[airline_data.hours == 8])
plt.show()

print(np.mean(airline_data.coach_price[airline_data.hours == 8]))
np.min(airline_data.coach_price[airline_data.hours == 8])
np.max(airline_data.coach_price[airline_data.hours == 8])

#sns.scatterplot("coach_price", "hours", data = airline_data)
#plt.show()

#sns.boxenplot(airline_data.hours, airline_data.coach_price)



