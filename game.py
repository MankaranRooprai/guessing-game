# Implement a word guessing game initialized with a dictionary and a target word. The user will enter guesses, and the system will indicate whether the guess is correct, providing hints to guide the user. We will begin with a basic version and gradually introduce new requirements to add complexity. Aim to design your game for easy extension and refactor as you learn more.

# Please note that the full problem is challenging. We do not expect you to complete all of it during this session.
# Maxence Haltel
# 09:33
# ### Milestone One: Data Structures and Basic Functionality

# 1. Define a dictionary consisting of valid four-letter words. Store the following list:
#    ```ruby
#    ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]
#    ```

# 2. Implement a method to randomly select a word from this list.
# 3. Implement a method to accept a guess and check if it matches the selected word.

# Run this logic to ensure it works as expected.

### Milestone Two: User Interface

# Develop a terminal user interface for the game. Start by welcoming the user, explaining the game rules, and then proceeding with the game. Sample prompts might include:

# ```
# Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:
# ```
# ```
# Wrong guess! Try again:
# ```
# ```
# You got it! Amazing!
# ```
# ```
# You're out of turns, game over!
# ```

import random

class Game:
    def __init__(self):
        self.words = ["able"]
        self.correct_word = self.choose_word()

    def get_input(self, turn_num):
        if turn_num == 0:
            guess = input("Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:")
        elif turn_num > 0 and turn_num < 5:
            guess = input("Wrong guess! Try again:")
        return self.check_word(guess)

    def choose_word(self):
        return random.choice(self.words)
    
    def check_word(self, guess):
        if guess == self.correct_word:
            return True
        return False

    def run(self):
        won = False
        self.choose_word()
        for i in range(5):
            if self.get_input(i):
                print("You got it! Amazing!")
                won = True
                break
        
        if not won:
            print("You're out of turns, game over!")

if __name__ == "__main__":
    game = Game()
    game.run()