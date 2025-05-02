import global_variables
import random


class Model:
    def __init__(self, controller=None):
        self.controller = controller
        self.right_guess = ""
        self.tries = 0

    def randon_guess(self, language):
        if language == "english":
            return random.choice(list(global_variables.words_english.keys()))
        elif language == 'portugues':
            return random.choice(list(global_variables.words_portugues.keys()))
        else:
            return random.choice(list(global_variables.words_german.keys()))

    def check_guess(self, guess_entry):
        if guess_entry.lower() == self.right_guess.lower():
            self.controller.controller_win()
        else:
            self.tries += 1
            self.controller.update_hint()
