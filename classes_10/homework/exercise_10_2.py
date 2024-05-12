# EXERCISE 10.2 (SERIES)
#
# Create pd.Series where 'index' contains days of the current month (numpy.datetime64 instances or pandas.DatetimeIndex)
# and 'data' contains some numbers (temperatures at noon, currency rates, ...).
import pandas as pd

dates = pd.date_range('2024-05-01', '2024-05-31', freq='D')
temperaturesAtNoon = [30,31,28,25,26,43,21,24,25,26,35,30,31,28,25,26,43,21,24,25,26,35,30,31,28,25,26,43,21,24,25]

daysDataSeries = pd.Series(data=temperaturesAtNoon, index=dates, name="daysAndTemperaturesAtNoon")

print("Days and temperatures at noon:")
print(daysDataSeries)