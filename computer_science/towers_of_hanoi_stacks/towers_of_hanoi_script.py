## Towers of Hanoi - CodeAcademy
from computer_science.towers_of_hanoi_stacks.stack import Stack

## Start the game
print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
## Add each individual stack in a large list
stacks += [left_stack, middle_stack, right_stack]

# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

## If user enters < 3 disks, reprompt for a number
while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

## Number of disks from above on the left stack
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

## Calculate optimal moves and notify the user
num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))


# Get User Input
def get_input():
    ## Add towers first letter for moving
    choices = [stack.get_name()[0] for stack in stacks]

    ## Prompt for where you want the moves to be made
    while True:
        ## Print L, M, R for which stack you are selecting
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))

        ## Capture the user input
        user_input = input("")

        ## Return the index of the input letter
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Play the Game
num_user_moves = 0

## While right stack does not equal number of disk, play the game
while right_stack.get_size() != num_disks:
    ## Show user current layout of stacks
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

    ## Prompt user for a move
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()

        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        ## Determine if there is a valid move and either make of deny that move
        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try again!.")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try again!.")

## Once all disks are on the right, notify user of how well they did
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,
                                                                                               num_optimal_moves))