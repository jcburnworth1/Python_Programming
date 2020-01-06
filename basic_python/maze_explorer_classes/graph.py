from  Python_Programming.basic_python.maze_explorer_classes.vertex import Vertex

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    def explore(self):
        print("Exploring the graph....\n")
        # FILL IN EXPLORE METHOD BELOW
        current_room = 'Entrance'
        path_total = 0

        print("\nStarting off at the {0}\n".format(current_room))

        while current_room != 'Treasure Room':
            node = self.graph_dict[current_room]

            for connected_room, weight in node.edges.items():
                key = connected_room[:1]
                print("Enter {0} for {1}: {2} Cost".format(key, connected_room, weight))

            valid_choices = [room[:1] for room in node.edges.keys()]

            print("\nYou have accumulated: {0} cost".format(path_total))

            choice = input("\nWhich room do you move to? ")

            if choice not in valid_choices:
                print("Please select from there letters: {0}".format(valid_choices))
            else:
                for room in node.edges.keys():
                    if choice == room[0]:
                        current_room = room
                        path_total += node.edges[room]
                print("\n*** You have chosen: {0} ***\n".format(current_room))

        print("Made it to the treasure room with {0} cost".format(path_total))


    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dict:
            print("{0} connected to...".format(node_key))
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print("=> {0}: cost is {1}".format(adjacent_node, weight))
            print("")
        print("")


def build_graph():
    graph = Graph()

    # MAKE ROOMS INTO VERTICES BELOW...
    entrance = Vertex("Entrance")
    ante_chamber = Vertex("Ante-Chamber")
    kings_room = Vertex("King's Room")
    grand_gallery = Vertex("Grand Gallery")
    treasure_room = Vertex("Treasure Room")

    # ADD ROOMS TO GRAPH BELOW...
    graph.add_vertex(entrance)
    graph.add_vertex(ante_chamber)
    graph.add_vertex(kings_room)
    graph.add_vertex(grand_gallery)
    graph.add_vertex(treasure_room)

    # ADD EDGES BETWEEN ROOMS BELOW...
    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, kings_room, 3)
    graph.add_edge(ante_chamber, kings_room, 1)
    graph.add_edge(ante_chamber, grand_gallery, 2)
    graph.add_edge(kings_room, grand_gallery, 2)
    graph.add_edge(ante_chamber, treasure_room, 6)
    graph.add_edge(grand_gallery, treasure_room, 4)

    # DON'T CHANGE THIS CODE
    graph.print_map()
    return graph