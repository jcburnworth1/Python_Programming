## Len's Slice Project - CodeAcademy
## Pizza Toppings
toppings = ["pepperoni",
            "pineapple",
            "cheese",
            "sausage",
            "olives",
            "anchovies",
            "mushrooms"]

## Topping Prices
prices = [2, 6, 1, 3, 2, 7, 2]

## Number of Toppings
num_pizzas = len(toppings)

## Print toppings count
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

## Combine toppings & prices
pizzas = list(zip(prices, toppings))

## Print pizzas
print(pizzas)

## Sort by price
pizzas.sort()

## Print pizzas
print(pizzas)

## Find the cheapest pizza
cheapest_pizza = pizzas[0]

## Print cheapest_pizza
print(cheapest_pizza)

## Find the most expensive pizza
priciest_pizza = pizzas[-1]

## Print priciest_pizza
print(priciest_pizza)

## Three cheapest pizzas
three_cheapest = pizzas[:3]

## Print three_cheapest
print(three_cheapest)

## Two dollar slices
num_two_dollar_slices = prices.count(2)

## Print num_two_dollar_slices
print(num_two_dollar_slices)