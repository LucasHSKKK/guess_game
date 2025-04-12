import tkinter as tk
from functools import partial
import random
import global_variables


class View:
    def __init__(self, controller):
        self.controller = controller

        # create the main application
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Guess Game")
        self.button1 = tk.Button(
            self.root,
            text="portugues",
            font=("Arial", 20),
            bg="white",
            fg="black",
            command=partial(self.controller.portugues_button),
        )
        self.button2 = tk.Button(
            self.root,
            text="english",
            font=("Arial", 20),
            bg="white",
            fg="black",
            command=partial(self.controller.english_button),
        )
        self.button1.pack(pady=20)
        self.button2.pack(pady=20)

    def english_clicked(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = tk.Label(
            self.root,
            text="Enter your guess:",
            font=("Arial", 20),
            bg="white",
            fg="black",
        )
        self.entry = tk.Entry(
            self.root,
            bg="white",
            fg="black",
            bd=3,
            font=("Arial", 20),
        )
        self.button = tk.Button(
            self.root,
            text="Submit",
            activebackground="red",
            bg="white",
            fg="black",
            font=("Arial", 20),
        )

        self.label_dica = tk.Label(
            self.root,
            text="Hint:",
            font=("Arial", 20),
        )

        guess = random.choice(list(global_variables.words_english.keys()))

        self.listbox = tk.Listbox(
            self.root,
            bg=self.root.cget("bg"),
            fg="red",
            font=("Arial", 20),
        )

        self.listbox.insert(0, global_variables.words_english[guess]["hint1"])

        # Pack the widgets
        self.label.pack(pady=20)
        self.entry.pack(pady=20)
        self.button.pack(pady=20)
        self.label_dica.pack(pady=20)
        self.listbox.pack(pady=20)

    def portugues_clicked(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = tk.Label(
            self.root,
            text="digite seu palpite:",
            font=("Arial", 20),
            bg="white",
            fg="black",
        )
        self.entry = tk.Entry(
            self.root,
            bg="white",
            fg="black",
            bd=3,
            font=("Arial", 20),
        )
        self.button = tk.Button(
            self.root,
            text="enviar",
            activebackground="red",
            bg="white",
            fg="black",
            font=("Arial", 20),
        )

        self.label_dica = tk.Label(
            self.root,
            text="Dica:",
            font=("Arial", 20),
        )

        guess = random.choice(list(global_variables.words_portugues.keys()))

        self.listbox = tk.Listbox(
            self.root,
            bg=self.root.cget("bg"),
            fg="red",
            font=("Arial", 20),
        )

        self.listbox.insert(0, global_variables.words_portugues[guess]["dica1"])

        self.label.pack(pady=20)
        self.entry.pack(pady=20)
        self.button.pack(pady=20)
        self.label_dica.pack(pady=20)
        self.listbox.pack(pady=20)

    def run(self):
        self.root.mainloop()
