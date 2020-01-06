## Add fetchmaker folder to sys.path
import sys
sys.path.insert(0, '/Users/jc.burnworth/Documents/Code/Python/Code_Academy/fetchmaker')

## Import libraries
import fetchmaker
import numpy as np
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

## Load Rottweiler tail lengths
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')

## Get mean and standard deviation for rottweiler tails
rottweiler_tail_mean = np.mean(rottweiler_tl)
rottweiler_tail_std = np.std(rottweiler_tl)

## Print
print('Rottweiler Tail Mean: {0}'.format(str(rottweiler_tail_mean)))
print('Rottweiler Tail STD: {0}'.format(str(rottweiler_tail_std)))

## Get whippet rescue data
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescue = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

## Print
print('Whipper Rescues: {0}'.format(str(num_whippet_rescue)))
print('Total Whippets: {0}'.format(str(num_whippets)))

## Binomial test of whippet rescue rate
whippet_pval = binom_test(6, n=100, p=0.08)

## Print
print('Whippet Rescue P-Value: {0}'.format(str(whippet_pval)))
if whippet_pval < 0.05:
    print('It is unlikely that whippet rescue rate is 8%')
else:
    print('It is likely that whippet rescue rate is 8%')

## Comparison of whippets, terriers, pitbulls
## Load data for each
whippets = fetchmaker.get_weight('whippet')
terriers = fetchmaker.get_weight('terrier')
pitbulls = fetchmaker.get_weight('pitbull')

## ANOVA comparing weight between the three dog types
fstat_weight, pval_weight = f_oneway(whippets, terriers, pitbulls)

## Low P-Value indicates not a significant difference between stores
print('F-Stat: {0}'.format(str(fstat_weight)))
print('P-Value: {0}'.format(str(pval_weight)))
if pval_weight < 0.05:
    print('Significant difference between breeds when looking at weight')
else:
    print('No significant difference between breeds when looking at weight')

## Tukey test to determine which breeds are different
# Using our data from ANOVA, we create v and l
v = np.concatenate([whippets,terriers, pitbulls])
labels = ['whippet'] * len(whippets) + ['terrier'] * len(terriers) + ['pitbull'] * len(pitbulls)

## Run Tukey Analysis
tukey_results = pairwise_tukeyhsd(v, labels, alpha=0.05)

## Print
print(tukey_results)

## Color breakdown of poodles vs. shihtzus
poodle_coloring = fetchmaker.get_color('poodle')
shihtzu_coloring = fetchmaker.get_color('shihtzu')

## Count up colors for the dog breeds
## Contingency table layout
##         poodle |  shihtzu
## ----+------------------+------------
## black    | n | n
## brown    | n | n
## gold     | n | n
## grey     | n | n
## white    | n | n

color_table = [[17, 10],
               [13, 36],
               [8, 6],
               [52, 41],
               [10, 7]]

## Run Chi-Square test
chi2_poodle_shihtzu, pval_poodle_shihtzu, dof_poodle_shihtzu, expected_poodle_shihtzu = chi2_contingency(color_table)

## A p-value of < 0.05 (generally) would suggest significant difference between the datasets
print("Poodle-Shihtzu Chi-Sqaure P-Value: {0}".format(pval_poodle_shihtzu))