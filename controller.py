from view import View

class Controller:
    def __init__(self):
        self.view = View()

    def start_game(self):
        self.view.run()

