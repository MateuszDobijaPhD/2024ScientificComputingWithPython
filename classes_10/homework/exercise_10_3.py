# EXERCISE 10.3 (DATAFRAME)
#
# Create pd.DataFrame for the periodic table (ten elements). Column names are 'Name', 'Symbol', 'Weight'. 'index' starts from 1 for hydrogen.
import pandas as pd

startId = 1
endId = 10
step = 1
indices = range(startId, endId +1, step)
names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
symbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
weights = [1.0080, 4.00260, 6.94, 9.012183, 10.81, 12.011, 14.007, 15.999, 18.99840316, 20.180]

periodicElementsDict = {"Names": names, "Symbols": symbols, "Weights": weights}
periodicTableDataFrame = pd.DataFrame(data=periodicElementsDict, index = indices)

print("10 first elements from periodic table:")
print(periodicTableDataFrame)