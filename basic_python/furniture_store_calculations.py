## Furniture Project - CodeAcademy
###### Furniture ######
## Lovely Loveseat
## Description
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
## Price
lovely_loveseat_price = 254.00

## Stylish Settee
## Description
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
## Price
stylish_settee_price = 180.50

## Luxurious Lamp
## Description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
## Price
luxurious_lamp_price = 52.15

##### Sales Tax #####
sales_tax = 0.088

###### Customers ######
###### Customer 1 #####
## Total
customer_one_total = 0
## Items
customer_one_itemization = ""

## Purchases
## Item 1
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

## Item 2
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

## Sales Tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

## Receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
###### Customer 1 #####
###### Customer 2 #####
## Total
customer_two_total = 0
## Items
customer_two_itemization = ""

## Purchases
## Item 1
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

## Item 2
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

## Sales Tax
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

## Receipt
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)
###### Customer 2 #####