import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

start = datetime.now()

# load in data
in_bloom = pd.read_csv('Python_Programming/plotting/acadia_travel/inbloom.csv')
flights = pd.read_csv('Python_Programming/plotting/acadia_travel/flights.csv')

# Plot the histograms
plt.figure(1)
plt.subplot(211)
## Flights
plt.hist(flights, range=(0,365), bins=365)
plt.xlabel('Day')
plt.ylabel("Flights")
plt.title("Histogram of Flights")

plt.subplot(212)
plt.hist(in_bloom, range=(0,365), bins=365)
plt.tight_layout()
plt.show()
plt.savefig('Python_Programming/plotting/acadia_travel/histogram.png')
# plt.close('all')

end = datetime.now()

print("Start Time: " + str(start))
print("End Time: " + str(end))
print("Elapsed Time: " + str((end - start)))
