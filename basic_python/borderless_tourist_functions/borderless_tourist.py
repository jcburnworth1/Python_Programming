## Borderless Tourist - CodeAcademy
## Possible Destinations
destinations = ["Paris, France",
                "Shanghai, China",
                "Los Angeles, USA",
                "São Paulo, Brazil",
                "Cairo, Egypt"]

## Attractions
attractions = [[], [], [], [], []]

## Test Traveler
test_traveler = ['Erin Wilkes',
                 'Shanghai, China',
                 ['historical site',
                  'art']]

## Retrieve the destinations index
def get_destination_index(destination):
    ## Find the index of a city from the destinations list
    destination_index = destinations.index(destination)

    return destination_index

## Test get_destination_index with "Los Angeles, USA" and "Paris, France"
# print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris, France"))
## The below will not work since this city is not in the destinations list
# print(get_destination_index("Hyderabad, India"))

## Retrieve the traveler's current location
def get_traveler_location(traveler):
    ## Pull the current city for the traveler - Index 1
    traveler_destination = test_traveler[1]

    ## Using the current city, find the index from destinations
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

## Test get_traveler_location and save to test_destination_index
test_destination_index = get_traveler_location(test_traveler)

## Print test_destination_index
# print(test_destination_index)

## Add attractions for a given destination
def add_attraction(destination, attraction):
    ## Try to add an attraction to a give city
    try:
        ## Find the index from destinations
        destination_index = get_destination_index(destination)

        ## Select the proper list for attractions based on the destination
        attractions_for_destination = attractions[destination_index]

        ## Add the supplied attraction to the a
        attractions_for_destination.append(attraction)

    ## If city not in destinations, return nothing and continue
    except ValueError:
        return

    return

## Test add_attraction()
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

## Print attractions to test add_attraction function
# print(attractions)

## Add a few more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

## Print attractions to test add_attraction function
# print(attractions)

## Find attractions for a given destination & interest
def find_attractions(destination, interests):
    ## Get the city's destination index
    destination_index = get_destination_index(destination)

    ## Pull the attractions in a city based on the destination index
    attractions_in_city = attractions[destination_index]

    ## Create empty list for attractions including their interests
    attractions_with_interest = []

    ## Loop over attractions in city
    for attraction in attractions_in_city:
        ## Save the attractions name
        possible_attraction = attraction

        ## Save the attractions tags
        attraction_tags = attraction[1]

        ## While looking at various attractions, add them to attractions_with_interest
        ## if the interest matches what the traveler is interested in
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest

## Test find_attractions() functon
la_arts = find_attractions("Los Angeles, USA", ['art'])

## Print la_arts
# print(la_arts)

## Find attractions for a given traveler
def get_attractions_for_traveler(traveler):
    ## Capture the destination and interests
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    ## Find relevant attractions
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    ## Output string
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "

    ## Loop over attractions and append to interests_string
    for attraction in traveler_attractions:
        interests_string = interests_string + attraction + ", "

    return interests_string

## Testing get_attractions_for_traveler()
## Test traveler
dereck_smill = ['Dereck Smill', 'Paris, France', ['monument']]
smills_france = get_attractions_for_traveler(dereck_smill)

## Print out smills_france
print(smills_france)