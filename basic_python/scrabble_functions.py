## Scrabble - CodeAcademy
## Initial Variables
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4,
          1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

## Combine letters and points into a list
letters_to_points = {letter:point for letter, point in zip(letters, points)}

## Add the blank tile to the letter_to_points dictionary
letters_to_points.update({" ": 0})

## Update point totals
def update_point_totals(dictionary):
    ## Loop over player_to_words and score
    for player, words in player_to_words.items():
        ## Initialize player_points to score and total words
        player_points = 0

        ## Loop over that players words and add to player_points
        for word in words:
            player_points += score_word(word)

        ## Update the proper players points
        player_to_points.update({player: player_points})

## Play a word
def play_word(player, word):
    ## Update word list for a given player
    player_to_words[player].append(word)
    ## Run update to player scores
    update_point_totals(player_to_words)

## Score the words
def score_word(word):
    ## Initialize variable to total score of a word
    word_score = 0

    ## Loop over the word and total up the points
    ## Throw in an upper just in case
    for letter in word.upper():
        word_score += letters_to_points.get(letter, 0)

    return word_score

## Test score_word function
brownie_points = score_word("brownie")
print("Brownie Score: " + str(brownie_points))

## player_to_words dictionary will capture the words played by each player
player_to_words = {"player1": ["blue", "tennis", "exit"],
                   "wordNerd": ["earth", "eyes", "machine"],
                   "Lexi Con": ["eraser", "belly", "husky"],
                   "Prof Reader": ["zap", "coma", "period"]}

## player_to_points dictionary will score the words by each player
player_to_points = {}

## Loop over player_to_words and score
for player, words in player_to_words.items():
    ## Initialize player_points to score and total words
    player_points = 0

    ## Loop over that players words and add to player_points
    for word in words:
        player_points += score_word(word)

    ## Initial loop to score players
    player_to_points.update({player: player_points})

## Print current scores from players_to_points
for player, score in player_to_points.items():
    print("{player}'s current score: {score}".format(player = player, score = score))