## Import libraries
import statistical_examples.nosh_mish_mosh_minimum_effect.nosh_mish_mosh as nosh_mish_mosh
import numpy as np

## Load data
all_visitors = nosh_mish_mosh.get_data('Customer Visits')
paying_customers = nosh_mish_mosh.get_data('Purchasing Customers')
payment_history = nosh_mish_mosh.get_data('Money Spent')

## Calculate conversion rate
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_customers)
baseline_percent = (paying_visitor_count/ total_visitor_count) * 100

## Print
print("Total Visitors: {0}".format(total_visitor_count))
print("Paying Visitors: {0}".format(paying_visitor_count))
print("Baseline Conversion Rate: {0}%".format(baseline_percent))

## Determine Minimum Detectable Effect
## Average payment
average_payment = np.mean(payment_history)

## Dollars needed to clear $1240 cost for new vegetable offering
new_customers_needed = np.ceil(1240 / average_payment)

## Print
print("Total New Customers: {0}".format(new_customers_needed))

## Calculate lift needed
percentage_point_increase = (new_customers_needed * 100) / total_visitor_count

## Print
print("Life Needed: {0}%".format(percentage_point_increase))

## Minimum Detectable Effect
minimum_detetcable_effect = (percentage_point_increase / baseline_percent) * 100

## Print
print("Minimum Detectable Effect Needed: {0}%".format(round(minimum_detetcable_effect,2)))

## Calculate Sample Size
## Desire confidence interval
confidence_interval = 0.90

## Sample Size
ab_sample_size = 290

## Print
print("Sample Size Neded: {0}".format(ab_sample_size))
