## Testing difference of categoricals
## Import libraries
from scipy.stats import binom_test

## Binomail Test - Probabality of success
pval = binom_test(510, n=10000, p=0.06)

print("Chance of Success: {0}%".format(str(round(pval * 100, 4))))

## Lowering the threshold
pval2 = binom_test(590, n=10000, p=0.06)

# The null hypothesis, in this case, would be that there is no difference between the observed behavior and
# the expected behavior. If we get a p-value of less than 0.05, we can reject that hypothesis and determine
# that there is a difference between the observation and expectation.
print("Chance of Success: {0}%".format(str(round(pval2 * 100, 4))))