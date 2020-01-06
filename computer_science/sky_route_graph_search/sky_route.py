## Sky Route - CodeAcademy
## Import needed files
from Python_Programming.computer_science.sky_route_graph_search.graph_search import bfs, dfs
from Python_Programming.computer_science.sky_route_graph_search.vc_metro import vc_metro
from Python_Programming.computer_science.sky_route_graph_search.vc_landmarks import vc_landmarks
from Python_Programming.computer_science.sky_route_graph_search.landmark_choices import landmark_choices

# Build your program below:
## Put together all landmark choices in a giant string
landmark_string = ""

## Loop over landmark_choices and add to the string formatted below
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)

## Stations under construction
stations_under_construction = []

## Greet Function
def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" +
          landmark_string)

## Goodbye Function
def goodbye():
    print("Thanks for using SkyRoute!")

## Get active stations
def get_active_stations():
    ## Get the usual metro network
    updated_metro = vc_metro

    ## Loop over vc_metro stations and check for closed stations
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_station in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            ## If station closed, empty the station of data
            else:
                updated_metro[current_station] = set([])
    return updated_metro


## New Route Function
def new_route(start_point = None, end_point = None):
    ## Set the start and ending landmarks
    start_point, end_point = set_start_and_end(start_point, end_point)

    ## Determine the shortest route
    shortest_route = get_route(start_point, end_point)

    ## Check for closed stations
    if shortest_route:
        ## Make shortest route easier to read
        shortest_route_string = '\n'.join(shortest_route)

        ## Print route information out
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point,
                                                                         end_point,
                                                                         shortest_route_string))
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point,
                                                                                                         end_point))

    ## Option to view other routes
    again = input("Would you like to see another route? Enter y/n: ")

    ## Logic to handle user input
    if again.lower() == "y":
        ## Option to see landmarks list again
        show_landmarks()

        ## Show other routes
        new_route(start_point, end_point)
    else:
        return

## Show Landmarks Function
def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")

    if see_landmarks.lower() == "y":
        print(landmark_string)
    else:
        return

## Set Start & End Function
def set_start_and_end(start_point, end_point):
    ## Check if start_point is None
    ## If not, prompt to change start and end
    if start_point is not None:
        ## Capture the input
        change_point = input("What would you like to change?\n"
                             "You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

        ## Handle the user input
        ## b = Change both start and end
        if change_point.lower() == "b":
            start_point = get_start()
            end_point = get_end()
        ## o = Change origin
        elif change_point.lower() == "o":
            start_point = get_start()
        ## d = Change destination
        elif change_point.lower() == "d":
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            set_start_and_end(start_point, end_point)

    ## If start_point is none, call get_start() and get_end()
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point

## Get Start Function
def get_start():
    ## Capture current location
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")

    ## Check to ensure start_point_letter corresponds to valid landmark
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()


## Get End Function
def get_end():
    ## Capture desired destination
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")

    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()

## Get Route Function
def get_route(start_point, end_point):
    ## Get possible start and end stations between landmarks
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    ## Collect possible routes
    routes = []

    ## Find all possible routes
    for start_station in start_stations:
        for end_station in end_stations:
            ## Get current state of VC stations
            metro_system = get_active_stations() if stations_under_construction else vc_metro

            ## Check if a route exists
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)

                if not possible_route:
                    return None
                else:
                    return possible_route

            ## Call to graph_search.bfs()
            route = bfs(metro_system, start_station, end_station)

            ## If route found, add it to the routes list
            if route:
                routes.append(route)

    ## Find the shortest route based on number of stops (len)
    shortest_route = min(routes, key = len)
    return shortest_route

## Skyroute Function
def sky_route():
    greet()
    new_route()
    goodbye()

## Call skyroute Function
sky_route()