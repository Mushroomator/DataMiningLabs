import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "US_births_2000-2014.csv")
births = pd.read_csv(path, dtype=int, header=0)

# filter by columns
filteredBirths = births.filter(items=["month", "date_of_month", "day_of_week"])

# show only selection of rows
#selectedRows = births.isin(range(0,50))

print(births[:20])


plt.plot()
#print(filteredBirths)
#print(selectedRows)

