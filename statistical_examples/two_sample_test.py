## Test if a the means of two sample datasets are significantly different
## Import libraries
from scipy.stats import ttest_ind
import numpy as np

## Store data
week1 = np.array([23.90506824,26.67631982,27.27433886,24.25757125,32.40423483,39.56919357,23.07010059,29.82068109,
                  27.59433809,28.05639569,27.06757262,30.41192979,25.71358554,24.94294823,28.23123807,24.95337555,
                  18.51231639,27.46234762,28.38016611,13.91205901,29.02615866,26.90746774,22.8677726, 24.8938289,
                  25.96947935,26.86869621,20.72676456,27.35988314,20.68408581,21.19846143,16.25800931,23.92517681,
                  24.47923229,29.47050863,27.28425372,26.93339272,28.61026924,18.88377042,33.65468651,25.69470077,
                  20.98291356,22.69700387,28.60278855,21.36000443,30.77685156,20.83415999,23.79367158,19.7556718,
                  29.54421084,20.1433138])

week2 = np.array([18.63431907,31.28788036,34.96797943,21.81678117,28.21619974,39.39313736,35.52223207,27.54222109,
                  33.64395433,25.31673581,28.81392191,30.7358016, 26.37241881,26.0945555, 26.34073477,19.42196017,
                  32.58797652,24.84001926,28.93348335,20.43667584,22.72495967,32.31728012,35.384306,29.66709637,
                  24.53512973,30.91406007,19.56117513,24.90816833,30.13163726,31.47466199,27.77683598,16.51307462,
                  35.0770162, 31.74818107,36.36053496,27.70500593,29.49869936,27.65575346,37.18504075,25.16055104,
                  29.26553553,38.22163057,28.92102091,24.8215439, 38.30155495,34.76020645,22.26869162,28.82593733,
                  32.00975127,36.46437665])

print(week1)
print(week2)

week1_mean = np.mean(week1)
week2_mean = np.mean(week2)

week1_std = np.std(week1)
week2_std = np.std(week2)

print("Week 1 Mean: {0}".format(str(week1_mean)))
print("Week 1 STD: {0}".format(str(week1_std)))
print("Week 2 Mean: {0}".format(str(week2_mean)))
print("Week 2 STD: {0}".format(str(week2_std)))

# The p-value is the probability that the difference between the sample means is at least as large as what has
# been observed, under the assumption that the population means are equal. The smaller the p-value, the
# more surprised we would be by the observed difference in sample means if there really was no difference
# between the population means. Therefore, the smaller the p-value, the stronger the evidence is that the
# two populations have different means.

tstat, pval = ttest_ind(week1, week2)

print("T-Stat: {0}".format(str(tstat)))
print("P-Value: {0}".format(str(pval)))