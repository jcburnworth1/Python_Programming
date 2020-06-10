## Import libraries
import statistical_examples.familiar_sample_tests.familiar as familiar
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

## Results output
def result_output(pval, package):
    if pval < 0.05:
        print("The {0} Pack Is Proven To Make You Live Longer!".format(package))
    else:
        print("The {0} Pack Is Probably Good For You Somehow!".format(package))

## 1 Sample Tests against the population mean
## Import the Vein data
vein_pack_lifespans = familiar.lifespans(package='vein')

## Determine if average age of users of vein data is different from population average of 71
## Calculate average of the sample
vein_pack_lifespans_average = np.mean(vein_pack_lifespans)

## Test significance of difference
tstat_vein, pval_vein = ttest_1samp(vein_pack_lifespans, 71)

## Print
print("Vein Pack User Average Life Expectancy: {0}".format(str(vein_pack_lifespans_average)))
print("Vein Pack Significance T-Stat: {0}".format(str(tstat_vein)))
print("Vein Pack Significance P-Value: {0}".format(str(pval_vein)))

## Run pval through result_output to determine product value
result_output(pval_vein, "Vein")

## Import the Artery data
artery_pack_lifespans = familiar.lifespans(package='artery')

## Determine if average age of users of artery data is different from population average of 71
## Calculate average of the sample
artery_pack_lifespans_average = np.mean(artery_pack_lifespans)

## Test significance of difference
tstat_artery, pval_artery = ttest_1samp(artery_pack_lifespans, 71)

## Print
print("Artery Pack User Average Life Expectancy: {0}".format(str(artery_pack_lifespans_average)))
print("Artery Pack Significance T-Stat: {0}".format(str(tstat_artery)))
print("Artery Pack Significance P-Value: {0}".format(str(pval_artery)))

## Run pval through result_output to determine product value
result_output(pval_artery, "Artery")

##### 2 Sample Test between Vein & Artery #####
## Calculate vein STD
vein_pack_lifespans_std = np.std(vein_pack_lifespans)

## Calculate artery STD
artery_pack_lifespans_std = np.std(artery_pack_lifespans)

## Print
print("Vein Pack User Average Life Expectancy: {0}".format(str(vein_pack_lifespans_average)))
print("Vein Pack User STD Life Expectancy: {0}".format(str(vein_pack_lifespans_std)))
print("Artery Pack User Average Life Expectancy: {0}".format(str(artery_pack_lifespans_average)))
print("Artery Pack User STD Life Expectancy: {0}".format(str(artery_pack_lifespans_std)))

## Run the two sample test to see if artery is significantly better
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

## Print results
print("Two Sample T-Stat: {0}".format(str(package_comparison_results[0])))
print("Two Sample P-Value: {0}".format(str(package_comparison_results[1])))

## Test if artery pack is better than vein
if package_comparison_results[1] < 0.05:
    print("The Artery Package guarantees even stronger results!")
else:
    print("The Artery Package is also a great product!")

## ## Analyze artery package impact on iron
iron_contingency_table = familiar.iron_counts_for_package()

## Run Chi-Square to see if artery package impacted iron count materially
artery_chi2, artery_pval, artery_dof, artery_expected = chi2_contingency(iron_contingency_table)

## Print
print("Chi Square T-Stat: {0}".format(str(artery_chi2)))
print("Chi Square P-Value: {0}".format(str(artery_pval)))
print("Chi Square Degrees of Freedom: {0}".format(str(artery_dof)))
print("Chi Square Expected: {0}".format(str(artery_expected)))

## Test p-value for iron signifiance
if artery_pval < 0.05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("While We Can’t Say The Artery Package Will Help You, I Bet It’s Nice!")