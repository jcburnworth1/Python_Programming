## Basta Fazoolin - CodeAcademy
## Create class Menu that will be the basis for multiple menus
class Menu():
    ## Menu Constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    ## Menu String Representation
    def __repr__(self):
        return '{name} menu available from {start_time} to {end_time}'.format(name = self.name,
                                                                              start_time = self.start_time,
                                                                              end_time = self.end_time)

    ## Calculate Bill method
    def calculate_bill(self, purchased_items):
        total_price = 0.0

        ## Loop over and order, find corresponding cost, and total up
        for food in purchased_items:
            total_price += self.items.get(food, 0)

        return total_price

## Create class Franchise as basis for the various locations
class Franchise():
    ## Franchise constructor
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    ## Franchise String Representation
    def __repr__(self):
        return 'Store is location at {address}'.format(address = self.address)

    ## Determine available menus based on time and return
    def available_menus(self, time):
        available_menus = []

        ## Loop over menus and return what is available
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)

        return available_menus

## Create class Business as basis for Franchises
class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

## Brunch menu
brunch = Menu('Brunch', {'pancakes': 7.50,
                         'waffles': 9.00,
                         'burger': 11.00,
                         'home fries': 4.50,
                         'coffee': 1.50,
                         'espresso': 3.00,
                         'tea': 1.00,
                         'mimosa': 10.50,
                         'orange juice': 3.50}, 1100, 1600)

## Ealy Bird Menu
early_bird = Menu('Early Bird', {'salumeria plate': 8.00,
                                 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00,
                                 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50,
                                 'coffee': 1.50,
                                 'espresso': 3.00}, 1500, 1800)

## Dinner menu
dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00,
                         'ceaser salad': 16.00,
                         'pizza with quattro formaggi': 11.00,
                         'duck ragu': 19.50,
                         'mushroom ravioli (vegan)': 13.50,
                         'coffee': 2.00,
                         'espresso': 3.00}, 1700, 2200)

## Kids Menu
kids = Menu('Kids', {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00,
                     'apple juice': 3.00}, 1100, 2100)

## Arepas Menu
arepas = Menu('Arepas', {'arepa pabellon': 7.00,
                         'pernil arepa': 8.50,
                         'guayanes arepa': 8.00,
                         'jamon arepa': 7.50}, 1000, 2000)

## Test string representation on the brunch menu
print(brunch)

## Test calculate_bill function
## Brunch Order
brunch_order = ['pancakes', 'home fries', 'coffee']
brunch_bill = brunch.calculate_bill(brunch_order)
print(brunch_bill)

## Test call to calculate_bill on early bird
## Early Bird Order
early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_bill = early_bird.calculate_bill(early_bird_order)
print(early_bird_bill)

## Flagship Store Location
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

## New Store Location
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

## Take a' Arepa
arepa_place = Franchise('189 Fitzgerald Avenue', [arepas])

## Test available_menus method
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))

## Business Class for Basta Fazoolin
basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

## Business Class for Take a' Arepa
arepa_business = Business("Take a' Arepa", [arepa_place])