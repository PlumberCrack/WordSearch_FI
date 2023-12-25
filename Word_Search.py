import random

def create_word_search(words):
    # Convert words to uppercase
    words = [word.upper() for word in words]

    # Define the size of the grid
    rows = 10
    cols = 10

    # Initialize an empty grid
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    def can_place_word(word, row, col, dr, dc):
        for i in range(len(word)):
            r = row + i * dr
            c = col + i * dc
            if r < 0 or r >= rows or c < 0 or c >= cols or (grid[r][c] != ' ' and grid[r][c] != word[i]):
                return False
        return True

    def place_word(word, row, col, dr, dc):
        for i in range(len(word)):
            grid[row + i * dr][col + i * dc] = word[i]

    # Place words horizontally, vertically, or diagonally
    for word in words:
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])
        if direction == 'horizontal':
            placed = False
            while not placed:
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - len(word))
                if can_place_word(word, row, col, 0, 1):
                    place_word(word, row, col, 0, 1)
                    placed = True
        elif direction == 'vertical':
            placed = False
            while not placed:
                row = random.randint(0, rows - len(word))
                col = random.randint(0, cols - 1)
                if can_place_word(word, row, col, 1, 0):
                    place_word(word, row, col, 1, 0)
                    placed = True
        else:  # Diagonal
            placed = False
            while not placed:
                row = random.randint(0, rows - len(word))
                col = random.randint(0, cols - len(word))
                dr = random.choice([-1, 1])
                dc = random.choice([-1, 1])
                if can_place_word(word, row, col, dr, dc):
                    place_word(word, row, col, dr, dc)
                    placed = True

    # Fill the remaining spaces with random uppercase letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(letters)

    # Display the word search grid
    for row in grid:
        print(' '.join(row))

    # Return the words used
    return words

# Get words from the user
word_count = 10  
user_words = []
for i in range(word_count):
    word = input(f"Enter word {i + 1}: ")
    user_words.append(word)

# Create the word search and display the words used
used_words = create_word_search(user_words)
print("\nWords used in the word search:")
print(', '.join(used_words))