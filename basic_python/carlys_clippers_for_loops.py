## Carly's Clippers - CodeAcademy
## Initial Variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

## Sum up prices
total_price = 0

## Loop over the prices add total up
for price in prices:
    total_price += price

## Print out total_price
print("Total Price: " + str(total_price))

## Calculate average price
average_price = total_price / len(prices)

## Print out average_price
print("Average Haircut Price: " + str(average_price))

## New Prices via list comprehension
new_prices = [price - 5 for price in prices]

## Print out the new prices
print(new_prices)

## Calculate revenue
total_revenue = 0

for i in range(0,len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

## Print total_revenue
print("Total Revenue: " + str(total_revenue))

## Calculate Average Revenue
average_daily_revenue = total_revenue / 7

## Print average_daily_revenue
print("Average Daily Revenue: " + str(average_daily_revenue))

## Cuts Under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

## Print cuts_under_30
print("Cuts Under $30: " + str(cuts_under_30))