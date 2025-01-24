import random

class Game:
    def __init__(self):
        self.words = ["able", "coke"]
        self.correct_word = self.choose_word()
        self.first_try = True

    def get_input(self):
        # get user input
        guess = ""
        if self.first_try == True:
            guess = input("Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:")
            self.first_try = False
        else:
            guess = input("Try again:")

        return self.check_word(guess)

    def choose_word(self):
        return random.choice(self.words)
    
    def check_word(self, guess):

        # return the response type of the guess
        if guess == self.correct_word:
            return "correct"
        elif guess not in self.words:
            return "tie"
        elif not guess:
            return "tie"
        else:
            return "wrong"

    def run(self):
        won = False
        self.choose_word()

        # run the game 5 times
        i = 5
        while i > 0:
            result = self.get_input()
            if result == "correct":
                print("You got it! Amazing!")
                won = True
                break
            elif result == "tie":
                print(f"This is wrong but you still have {i} turns remaining!")
            elif result == "wrong":
                i -= 1
                print(f"WRONG! You have {i} turns remaining!")
        
        if not won:
            print("You're out of turns, game over!")

if __name__ == "__main__":
    game = Game()
    game.run()