from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)

    def start_game(self):
        self.view.run()

    def portugues_button(self):
        guess = self.model.get_portugues_guess()
        self.view.portugues_clicked(guess)

    def english_button(self):
        guess = self.model.get_english_guess()
        self.view.english_clicked(guess)

    def get_entry_guess(self, guess_entry):
        self.model.check_guess(guess_entry)

