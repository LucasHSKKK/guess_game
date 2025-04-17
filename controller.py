from view import View
from model import Model
import global_variables


class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)

    def start_game(self):
        self.view.run()

    def portugues_button(self):
        guess = self.model.get_portugues_guess()
        self.model.right_guess = guess
        self.view.portugues_clicked(guess)

    def english_button(self):
        guess = self.model.get_english_guess()
        self.model.right_guess = guess
        self.view.english_clicked(guess)

    def get_entry_guess(self, guess_entry):
        self.model.check_guess(guess_entry)

    def controller_win(self):
        self.view.win_screen()

    def update_hint(self):
        if self.model.tries == 1:
            self.view.listbox.insert(
                1,
                global_variables.words[self.model.right_guess]["hint2"],
            )
        elif self.model.tries == 2:
            self.view.listbox.insert(
                2,
                global_variables.words[self.model.right_guess]["hint3"],
            )
        else:
            self.view.lose_screen()
