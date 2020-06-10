## Import Libraries
import pandas as pd

## Read in the data
visits = pd.read_csv('basic_python/cool_tshirts_pandas/visit.csv', parse_dates=[1])
cart = pd.read_csv('basic_python/cool_tshirts_pandas/cart.csv', parse_dates=[1])
checkout = pd.read_csv('basic_python/cool_tshirts_pandas/checkout.csv', parse_dates=[1])
purchase = pd.read_csv('basic_python/cool_tshirts_pandas/purchase.csv', parse_dates=[1])

## View head of each df
## Visits
print(visits.head(10))

## Cart
print(cart.head(10))

## Checkout
print(checkout.head(10))

## Purchase
print(purchase.head(10))

## Merge visits to cart
visit_carts = pd.merge(visits, cart, how='left')

## Print len of visit_carts
print(len(visit_carts))

## Number of NULL timestamps for cart_time
no_cart = visit_carts[visit_carts.cart_time.isnull()].user_id.count()

## Percentage with t-shirt added to cart
percentage_tshirt = 1 - (no_cart / float(len(visit_carts)))

## 19.4% of visitors add a shirt to the car

## Merge cart to checkout & see checkout percentage
carts_checkout = pd.merge(cart, checkout, how='left')

no_checkout = carts_checkout[carts_checkout.checkout_time.isnull()].user_id.count()

percentage_checkout = 1 - (no_checkout / float(len(carts_checkout)))

## 79.0% of users that add a t-shirt checkout

## Clean up
del(carts_checkout, no_cart, no_checkout, percentage_checkout, percentage_tshirt, visit_carts)

## Merge all the data
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

## Percentage of users that checked out that purchase
percentage_purchase = 1 - (all_data[all_data.purchase_time.isnull()].user_id.count() /
                           float(all_data[all_data.checkout_time.isnull()].user_id.count()))

## Average Purchase Time
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

## Print time to purchase
print(all_data.time_to_purchase)

## Calc Average Purchase Time
print(all_data.time_to_purchase.mean())