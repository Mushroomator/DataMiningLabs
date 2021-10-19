import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



births = pd.read_csv("C:\\Users\\topi5\\Documents\\Studium\\07_Semester\\Kapitel_01\\US_births_2000-2014.csv", dtype=int, header=0)

# filter by columns
filteredBirths = births.filter(items=["month", "date_of_month", "day_of_week"])

# show only selection of rows
#selectedRows = births.isin(range(0,50))

print(births[:20])



#print(filteredBirths)
#print(selectedRows)

