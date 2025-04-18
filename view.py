import tkinter as tk
from functools import partial
import global_variables
from PIL import Image, ImageTk


class View:
    def __init__(self, controller):
        self.controller = controller

        # create the main application
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Guess Game")
        self.bg = Image.open("images/bg2.png")
        self.bg = self.bg.resize((1920, 1080))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.label_bg = tk.Label(self.root, image=self.bg)
        self.label_bg.place(x=0, y=0)

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

    def english_clicked(self, guess):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.bg = Image.open("images/bg2.png")
        self.bg = self.bg.resize((1920, 1080))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.label_bg = tk.Label(self.root, image=self.bg)
        self.label_bg.place(x=0, y=0)

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
            command=lambda: self.controller.get_entry_guess(self.entry.get()),
        )

        self.label_dica = tk.Label(
            self.root,
            text="Hint:",
            font=("Arial", 20),
        )

        self.listbox = tk.Listbox(
            self.root,
            bg=self.root.cget("bg"),
            fg="red",
            font=("Arial", 20),
        )

        self.listbox.insert(0, global_variables.words[guess]["hint1"])

        # Pack the widgets
        self.label.pack(pady=20)
        self.entry.pack(pady=20)
        self.button.pack(pady=20)
        self.label_dica.pack(pady=20)
        self.listbox.pack(
            pady=20,
            fill="both",
        )

    def portugues_clicked(self, guess):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.bg = Image.open("images/bg2.png")
        self.bg = self.bg.resize((1920, 1080))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.label_bg = tk.Label(self.root, image=self.bg)
        self.label_bg.place(x=0, y=0)

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
            command=lambda: self.controller.get_entry_guess(self.entry.get()),
        )

        self.label_dica = tk.Label(
            self.root,
            text="Dica:",
            font=("Arial", 20),
        )

        self.listbox = tk.Listbox(
            self.root,
            bg=self.root.cget("bg"),
            fg="red",
            font=("Arial", 20),
        )

        self.listbox.insert(0, global_variables.words[guess]["hint1"])

        self.label.pack(pady=20)
        self.entry.pack(pady=20)
        self.button.pack(pady=20)
        self.label_dica.pack(pady=20)
        self.listbox.pack(
            pady=20,
            fill="both",
        )

    def win_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.bg = Image.open("images/bg2.png")
        self.bg = self.bg.resize((1920, 1080))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.label_bg = tk.Label(self.root, image=self.bg)
        self.label_bg.place(x=0, y=0)

        self.label = tk.Label(
            self.root,
            text="You win!",
            font=("Arial", 20),
            bg="white",
            fg="black",
        )
        self.image = Image.open("images/win_image.png")
        self.image = self.image.resize((600, 434))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(
            self.root,
            image=self.image,
            bg="white",
        )

        self.button = tk.Button(
            self.root,
            text="try again",
            activebackground="gray",
            bg="white",
            fg="black",
            font=("Arial", 20),
            command=partial(self.controller.try_again),
        )

        self.label.pack(pady=20)
        self.image_label.pack(pady=20)
        self.button.pack(pady=20)   

    def lose_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.bg = Image.open("images/bg2.png")
        self.bg = self.bg.resize((1920, 1080))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.label_bg = tk.Label(self.root, image=self.bg)
        self.label_bg.place(x=0, y=0)

        self.label = tk.Label(
            self.root,
            text="You lose!",
            font=("Arial", 20),
            bg="white",
            fg="black",
        )

        self.image = tk.PhotoImage(file="images/lose_image.png")
        self.image_label = tk.Label(
            self.root,
            image=self.image,
            bg="white",
        )

        self.button = tk.Button(
            self.root,
            text="try again",
            activebackground="red",
            bg="white",
            fg="black",
            font=("Arial", 20),
            command=partial(self.controller.try_again),
        )

        self.label.pack(pady=20)
        self.image_label.pack(pady=20)
        self.button.pack(pady=20)

    def run(self):
        self.root.mainloop()
