
words_portugues = {
    'gato': {'dica1': 'animal de estimação.', 'dica2': 'adora dormir e caçar.', 'dica3': 'faz miau.'},
    'mesa': {'dica1': 'objeto de madeira.', 'dica2': 'Usamos para comer, estudar ou trabalhar.', 'dica3': 'Tem pernas, mas não anda.'},
    'carro': {'dica1': 'meio de transporte.', 'dica2': 'tem rodas.', 'dica3': 'usamos para viajar.'},
    'Relógio': {'dica1': 'Mostra as horas.', 'dica2': 'Pode ser de pulso ou de parede.', 'dica3': 'Faz "tic tac."'},
    'computador': {'dica1': 'Máquina eletrônica.', 'dica2': 'Usamos para trabalhar ou estudar.', 'dica3': 'Tem teclado e mouse.'},
    'Helicóptero': {'dica1': 'voa.', 'dica2': 'Possui hélices.', 'dica3': 'Usado por bombeiros e polícia.'},
}

words_english = {
    'cat': {'hint1': 'pet animal.', 'hint2': 'loves to sleep and hunt.', 'hint3': 'goes meow.'},
    'table': {'hint1': 'wooden object.', 'hint2': 'used for eating, studying or working.', 'hint3': 'has legs but doesn’t walk.'},
    'car': {'hint1': 'means of transportation.', 'hint2': 'has wheels.', 'hint3': 'we use it to travel.'},
    'watch': {'hint1': 'shows the time.', 'hint2': 'can be worn on the wrist or hung on the wall.', 'hint3': 'goes "tick tock".'},
    'computer': {'hint1': 'electronic machine.', 'hint2': 'used for work or study.', 'hint3': 'has a keyboard and mouse.'},
    'helicopter': {'hint1': 'flies.', 'hint2': 'has rotors.', 'hint3': 'used by firefighters and police.'}
}

import random 

class Model:
    def __init__(self, controller):
        self.controller = controller

    def get_english_guess():
        guess = random.choice(list(words_english.keys()))

    def get_portugues_guess():
        guess = random.choice(list(words_portugues.keys()))


