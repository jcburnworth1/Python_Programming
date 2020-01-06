## Choose Your Own Adventure - CodeAcademy
##### Classes #####
## TreeNode Class
class TreeNode():
    ## TreeNode constructor
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    ## Add a child to the story
    def add_child(self, node):
        ## Add node argument to choices
        self.choices.append(node)

    ## Traverse the story
    def traverse(self):
        story_node = self

        print(story_node.story_piece)

        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")

            if choice not in ["1", "2"]:
                print("Invalid Choice. Try again.")
            else:
                chosen_index = int(choice) - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child




##### Story variables #####
## Start the story - Every Story begins with the below
story_beginning = """\nYou are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...\n"""

## Create TreeNode, story_root
story_root = TreeNode(story_beginning)

## Choices off story_root
## Choice A
option_a = """\nThe bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'\n"""

## Create TreeNode, choice_a and add to story_root
choice_a = TreeNode(option_a)
story_root.add_child(choice_a)

## Choice A 1
option_a_1 = """\nThe bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.\n"""

## Create TreeNode, choice_a_1 and add to choice_a
choice_a_1 = TreeNode(option_a_1)
choice_a.add_child(choice_a_1)

## Choice A 2
option_a_2 = """\nThe bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.\n"""

## Create TreeNode, choice_a_2 and add to choice_a
choice_a_2 = TreeNode(option_a_2)
choice_a.add_child(choice_a_2)

## Choice B
option_b = """\nYou come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.\n"""

## Create TreeNode, choice a and add to story_root
choice_b = TreeNode(option_b)
story_root.add_child(choice_b)

## Choice B 1
option_b_1 = """\nThe bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.\n"""

## Create TreeNode, choice_b_1 and add to choice_b
choice_b_1 = TreeNode(option_b_1)
choice_b.add_child(choice_b_1)

## Choice B 2
option_b_2 = """\nThe bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.\n"""

## Create TreeNode, choice_b_2 and add to choice_b
choice_b_2 = TreeNode(option_b_2)
choice_b.add_child(choice_b_2)

##### Story Happens Here #####
print("Once upon a time...\n")

## Run through the story
story_root.traverse()