import random

def mostrar_bienvenida():
    print("===================================")
    print("¡Bienvenido al juego Adivina el Número!")
    print("===================================")
    print("Debes adivinar el número secreto.")
    print("Después de cada intento te diré si el número es más alto o más bajo.")
    print("¡Intenta hacerlo en la menor cantidad de intentos posible!\n")

def startGame():
    mostrar_bienvenida()
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    while guess != number:
        guess = int(input("Ingresa tu intento: "))
        attempts += 1
        if guess < number:
            print("Muy bajo")
        elif guess > number:
            print("Muy alto")
        elif guess == number:
            print("¡Correcto!")
        else:
            print("Error")
    print("Número de intentos:", attempts)


startGame()