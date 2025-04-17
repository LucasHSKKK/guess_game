import global_variables
import random


class Model:
    def __init__(self, controller=None):
        self.controller = controller
        self.right_guess = ""
        self.tries = 0

    def get_english_guess(self):
        return random.choice(list(global_variables.words_english.keys()))

    def get_portugues_guess(self):
        return random.choice(list(global_variables.words_portugues.keys()))

    def check_guess(self, guess_entry):
        if guess_entry.lower() == self.right_guess.lower():
            self.controller.controller_win()
        else:
            self.tries += 1
            self.controller.update_hint()
