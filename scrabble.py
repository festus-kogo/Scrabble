letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# print(type(letters))
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1
letter_to_points = { letter: point for letter, point in zip(letters, points) }
# print(letter_to_points)
# print(type(letter_to_points))

# 2
letter_to_points[" "] = 0
# print(letter_to_points)

# 5
def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_points.keys():
            # print(letter + " was found")
            point_total += letter_to_points.get(letter)
        else:
            point_total += 0
    return point_total

# print(score_word("BROWNIE"))
# 15

# 7
brownie_points = score_word("BROWNIE")

# 8
# print(brownie_points)
# 15

# 9
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"], 
    "wordNerd": ["EARTH", "EYES", "MACHINE"], 
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
    }
# print(player_to_words)
# Output
# {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# 10
player_to_points = {}
# 11
for player, words in player_to_words.items():
    # print(player, words)
    # Output
    # player1 ['BLUE', 'TENNIS', 'EXIT']
    # ['BLUE', 'TENNIS', 'EXIT']
    # wordNerd ['EARTH', 'EYES', 'MACHINE']
    # ['EARTH', 'EYES', 'MACHINE']
    # Lexi Con ['ERASER', 'BELLY', 'HUSKY']
    # ['ERASER', 'BELLY', 'HUSKY']
    # Prof Reader ['ZAP', 'COMA', 'PERIOD']
    # ['ZAP', 'COMA', 'PERIOD']
    player_points = 0
    # print(words)
    # Output
    # ['BLUE', 'TENNIS', 'EXIT']
    # ['EARTH', 'EYES', 'MACHINE']
    # ['ERASER', 'BELLY', 'HUSKY']
    # ['ZAP', 'COMA', 'PERIOD']
    # 12
    for word in words:
        # print(word)
        # Output
        # BLUE
        # TENNIS
        # EXIT
        # EARTH
        # EYES
        # MACHINE
        # ERASER
        # BELLY
        # HUSKY
        # ZAP
        # COMA
        # PERIOD
        player_points += score_word(word)
     # 13   
    player_to_points[player] = player_points

# 14
# print(player_to_points)
# Output
# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# 15