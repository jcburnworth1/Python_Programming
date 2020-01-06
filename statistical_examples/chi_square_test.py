## Testing outcomes of three or more categorical variables
## Import libraries
from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

x = [[30, 10],
     [35, 5],
     [28, 12]]
chi2, pval, dof, expected = chi2_contingency(x)

x2 = [[30, 10],
     [35, 5],
     [28, 12],
      [20,20]]
chi2_2, pval_2, dof_2, expected_2 = chi2_contingency(x2)

# In this case, the null hypothesis is that there’s no significant difference between the datasets.
# We reject that hypothesis, and state that there is a significant difference between two of the
# datasets if we get a p-value less than 0.05.
print(pval)
print(pval_2)