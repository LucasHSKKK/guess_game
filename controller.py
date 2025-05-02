from view import View
from model import Model
import global_variables


class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)

    def start_game(self):
        self.view.run()

    def get_guess(self, language):
        if language == "english":
            guess = self.model.randon_guess("english")
            self.model.right_guess = guess
            self.model.tries = 0
            self.view.english_clicked(guess)
        elif language == "portugues":
            guess = self.model.randon_guess("portugues")
            self.model.right_guess = guess
            self.model.tries = 0
            self.view.portugues_clicked(guess)
        else:
            guess = self.model.randon_guess("deutsch")
            self.model.right_guess = guess
            self.model.tries = 0
            self.view.deutsch_clicked(guess)

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

    def try_again(self):
        if self.model.right_guess in global_variables.words_portugues:
            self.get_guess("portugues")
        elif self.model.right_guess in global_variables.words_english:
            self.get_guess("english")
        else:
            self.get_guess('deutsch')
