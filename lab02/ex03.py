import numpy as np
import pandas as pd

births = pd.read_csv("C:\\Users\\topi5\\Documents\\Studium\\07_Semester\\Kapitel_01\\US_births_2000-2014.csv")

# extract date components
dateVals = births[["year", "month", "day_of_month"]]

birthsPerWeekday = births[["day_of_week", "births"]].groupby("day_of_week").sum()

# rename
#dateVals.rename(columns={"day_of_month": "day"})
# create new date column
# birthsPerWeekday["date"] = pd.to_datetime(dateVals)

print(birthsPerWeekday)

def weekday(iday):
    idx2day = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"
    }
    return idx2day[str(iday)]


idx = birthsPerWeekday.births.idxmax()
print(f'Max births per weekday are {birthsPerWeekday.births[idx]} on a {weekday(idx)}')