import random

def mostrar_bienvenida():
    print("===================================")
    print("Bienvenido al juego Adivina el Número")
    print("===================================")
    print("Debes adivinar el número secreto.")
    print("Después de cada intento te diré si el número es más alto o más bajo.")
    print("¡Intenta hacerlo en la menor cantidad de intentos posible!\n")

def choose_difficulty():
    """Permite al usuario elegir el nivel de dificultad y retorna el rango."""
    print("Selecciona nivel de dificultad:")
    print("1. Fácil (1 - 10)")
    print("2. Medio (1 - 20)")
    print("3. Difícil (1 - 50)")

    while True:
        option = input("Elige una opción (1/2/3): ")

        if option == "1":
            return 1, 10
        elif option == "2":
            return 1, 20
        elif option == "3":
            return 1, 50
        else:
            print("Opción no válida. Intenta de nuevo.")

def generate_secret_number(min_val=1, max_val=20):
    """Genera y retorna un número aleatorio entre min_val y max_val."""
    return random.randint(min_val, max_val)


def get_user_guess(prompt="Ingresa tu intento: "):
    """Solicita al usuario un intento y retorna el número ingresado."""
    
    while True:
            try:
                prompt = int(input("Ingresa tu intento: "))
                break

            except ValueError:
                print("Error: ValueError not an int" )
                continue

    return int(input(prompt))


def evaluate_guess(guess, target):
    """Evalúa el intento del usuario y muestra un mensaje. Retorna True si acierta."""
    if guess < target:
        print("Muy bajo")
        return False
    elif guess > target:
        print("Muy alto")
        return False
    else:
        print("¡Correcto!")
        return True


def start_game():
    """Muestra el mensaje de bienvenida y las instrucciones al ejecutar el juego"""
    mostrar_bienvenida()
    min_val, max_val = choose_difficulty()
    """Función principal que controla el flujo del juego."""
    number = generate_secret_number(min_val, max_val)
    attempts = 0
    attempts_limit = 100

    print(f"Adivina el número entre {min_val} y {max_val}")

    while True:
        attempts_limit = int(input("Ingresa el numero de intentos maximo 1-100"))

        if(attempts_limit < 0 or attempts_limit > 100):
            print("Numero no valido")
            continue

        else: break


    while True:
        guess = get_user_guess()
        attempts += 1
        
        is_correct = evaluate_guess(guess, number)
        if is_correct:
            break

        if(attempts == attempts_limit):
            break

    print("Número de intentos:", attempts)


if __name__ == "__main__":
    start_game()
