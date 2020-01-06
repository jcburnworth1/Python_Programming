## Test if a the mean of a sample dataset are significantly different from population mean
## Import libraries
from scipy.stats import ttest_1samp
import numpy as np

ages = np.array([32,34,29,29,22,39,38,37,38,36,30,26,22,22])

print(ages)

ages_mean = np.mean(ages)

print(ages_mean)

tstat, pval = ttest_1samp(ages, 30)

# If the P value is large, the data do not give you any reason to conclude
# that the population mean differs from the hypothetical value you entered.
# This is not the same as saying that the true mean equals the hypothetical value.
# You just don't have evidence of a difference.

# If the P value is small (usually defined to mean less than 0.05), then
# it is unlikely that the discrepancy you observed between sample mean and
# hypothetical mean is due to a coincidence arising from random sampling.
# You can reject the idea that the difference is a coincidence, and conclude
# instead that the population has a mean different than the hypothetical value you
# entered. The difference is statistically significant. But is the difference
# scientifically important? The confidence interval helps you decide.

print("T-State: {0}".format(str(tstat)))
print("P-Value: {0}".format(str(pval)))