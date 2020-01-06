## Sal's Shipping Project - CodeAcademy
## Ground Shipping Function
def standard_ground_shipping(weight):
    ## Standard Ground Shipping Flat Fee
    standard_ground = 20.00

    ## Shipping Cost
    shipping_cost = standard_ground

    ## Determine Shipping Cost
    if weight > 10:
        shipping_cost += weight * 4.75
    elif weight > 6:
        shipping_cost += weight * 4.0
    elif weight > 2:
        shipping_cost += weight * 3.0
    else:
        shipping_cost += weight * 1.5

    ## Return the cost
    return shipping_cost

## Test ground_shipping function
## 8.4lb. standard shipping should equal $53.60
# print(standard_ground_shipping(8.4))

## Premium Ground Shipping
def premium_ground_shipping(weight):
    ## Premium Ground Shipping Flat Fee
    premium_ground = 125.00

    ## Shipping Cost
    shipping_cost = premium_ground

    ## Return the cost
    return shipping_cost

## Test ground_shipping function
## 8.4lb. premium shipping should equal $158.60
# print(premium_ground_shipping(8.4))

## Drone Shipping Function
def drone_shipping(weight):
    ## Standard Ground Shipping Flat Fee
    # standard_ground = 0.00

    ## Shipping Cost
    shipping_cost = 0.0

    ## Determine Shipping Cost
    if weight > 10:
        shipping_cost += weight * 14.25
    elif weight > 6:
        shipping_cost += weight * 12.00
    elif weight > 2:
        shipping_cost += weight * 9.00
    else:
        shipping_cost += weight * 4.50

    ## Return the cost
    return shipping_cost

## Test drone_shipping function
## 1.5lb. drone shipping should equal $6.75
print(drone_shipping(1.5))

## Final Shipping Cost Function
def min_shipping_cost(weight):
    ## Run ground & drone shipping
    standard_ground_cost = standard_ground_shipping(weight)
    premium_ground_cost = premium_ground_shipping(weight)
    drone_cost = drone_shipping(weight)

    ## Cheapest Method
    cheapest_method = ""

    ## Determine cheapest shipping method
    if standard_ground_cost < premium_ground_cost and standard_ground_cost < drone_cost:
        cheapest_method = "Standard Ground: $" + str(standard_ground_cost)
    elif premium_ground_cost <standard_ground_cost and premium_ground_cost < drone_cost:
        cheapest_method = "Premium Ground: $" + str(premium_ground_cost)
    elif drone_cost < standard_ground_cost and drone_cost < premium_ground_cost:
        cheapest_method = "Drone: $" + str(drone_cost)

    return cheapest_method

## Test min_shipping_cost function
## 4.8lb package
print("The cheapest shipping method is: " + min_shipping_cost(4.8))
## 41.5lb package
print("The cheapest shipping method is: " + min_shipping_cost(41.5))