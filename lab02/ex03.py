import numpy as np
import pandas as pd

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

births = pd.read_csv("C:\\Users\\topi5\\Documents\\Studium\\07_Semester\\Data_Mining\\Kapitel_01\\US_births_2000-2014.csv")
# extract date components
dateVals = births[["year", "month", "date_of_month"]].copy()
# rename column so date can be created
dateVals.rename(columns={"date_of_month": "day"}, inplace=True)
# create new date column
birthsPerWeekday = births[["day_of_week", "births"]].copy()
result = birthsPerWeekday.groupby("day_of_week").sum()
# result["day_of_week_str"] = result.apply(lambda it: weekday(it))
print(result)

birthsPerWeekday["date"] = pd.to_datetime(dateVals)

idx = result.births.idxmax()
print(f'Max births per weekday are {result.iloc[idx].births} on a {weekday(result.iloc[idx].day_of_week)}')