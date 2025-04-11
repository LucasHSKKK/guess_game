from view import View

class Controller:
    def __init__(self):
        self.view = View(self)

    def start_game(self):
        self.view.run()

    def portugues_button(self):
        self.view.portugues_clicked()

    def english_button(self):
        self.view.english_clicked()

