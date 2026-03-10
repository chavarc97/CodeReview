import random


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
    """Función principal que controla el flujo del juego."""
    number = generate_secret_number(1, 20)
    attempts = 0
    attempts_limit = 100

    print("Adivina el número entre 1 y 20")
    
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
