import global_variables
import random


class Model:
    def __init__(self, controller=None):
        self.controller = controller

    def get_english_guess(self):
        guess = random.choice(list(global_variables.words_english.keys()))
        return guess

    def get_portugues_guess(self):
        guess = random.choice(list(global_variables.words_portugues.keys()))
        return guess

    def check_guess(self, guess_entry):
        if guess_entry == right_guess:
            print("correct")
        else:
            print("incorrect")

    right_guess = get_english_guess()
    tries = 0
