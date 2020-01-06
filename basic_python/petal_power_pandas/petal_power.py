## Import libraries
import pandas as pd

## Import data for Petal powers inventory
inventory = pd.read_csv('Python_Programming/basic_python/petal_power_pandas/inventory.csv')

## Print first ten rows
print(inventory.head(10))

## Save staten_island to a seperate df
staten_island = inventory[inventory.location == 'Staten Island']

## Staten Island Products
product_request = staten_island.product_description

## Brooklyn seeds available
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

## In-Stock
in_stock = lambda qty: True if qty > 0 else False

inventory['in_stock'] = inventory.quantity.apply(in_stock)

## Inventory Value
inventory['total_value'] = inventory.price * inventory.quantity

## Product Description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory[['product_type','product_description']].apply(combine_lambda, axis=1)

