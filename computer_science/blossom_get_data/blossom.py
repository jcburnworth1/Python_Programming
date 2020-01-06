## Blossom - CodeAcademy
## This import doesn't work so using the classes below
# from linked_list import Node, LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while (current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while (current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()

## This import doesn't work so using the flower_definitions list below
# from blossom_lib import flower_definitions
flower_definitions = [['begonia', 'cautiousness'],
                      ['chrysanthemum', 'cheerfulness'],
                      ['carnation', 'memories'],
                      ['daisy', 'innocence'],
                      ['hyacinth', 'playfulness'],
                      ['lavender', 'devotion'],
                      ['magnolia', 'dignity'],
                      ['morning glory', 'unrequited love'],
                      ['periwinkle', 'new friendship'],
                      ['poppy', 'rest'],
                      ['rose', 'love'],
                      ['snapdragon', 'grace'],
                      ['sunflower', 'longevity'],
                      ['wisteria', 'good luck']]

class HashMap():
    ## Constructor for the HashMap
    def __init__(self, size):
        self.array_size = size
        ## LinkedLists equal to the size passed
        self.array = [LinkedList() for i in range(size)]

    def hash(self, key):
        ## Convert key to bytecode
        return sum(key.encode())

    def compress(self, hash_code):
        ## Compress based on hash code % 4
        return hash_code % self.array_size

    def assign(self, key, value):
        ## Calculate the array_index
        array_index = self.compress(self.hash(key))

        ## Assign the key , value pair to a node
        payload = Node([key, value])

        ## Find the list at the array index
        list_at_array = self.array[array_index]

        ## Loop over items at list_at_array and find matching key
        for item in list_at_array:
            ## If key found, overwrite the value
            if key == item[0]:
                item[1] = value
                return

        ## Insert payload if key does not exist
        list_at_array.insert(payload)


    def retrieve(self, key):
        ## Calculate the array_index
        array_index = self.compress(self.hash(key))

        ## Retrieve the key, value at that array_index
        payload = self.array[array_index]

        ## Capture the list at the calculated array_index
        list_at_index = self.array[array_index]

        ## Loop over items at list_at_array and find matching key
        for item in list_at_index:
            ## If key found, return the value
            if key == item[0]:
                return item[1]
        ## If key not found, return None
        return None

## Craete HashMap for flower_definitions
blossom = HashMap(len(flower_definitions))

## Assign all elements of flower_definitions to blossom
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

## Let's retrieve data from the HashMap
print(blossom.retrieve('daisy'))