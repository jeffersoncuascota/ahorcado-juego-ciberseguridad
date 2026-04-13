import random

# Lista de palabras (puedes agregar más)
palabras = [
    "python", "ahorcado", "computadora", "programacion", "desarrollo",
    "algoritmo", "variable", "funcion", "bucle", "condicional",
    "github", "seguridad", "ciberseguridad", "terminal", "teclado"
]

def dibujar_ahorcado(intentos):
    """Dibuja el ahorcado según los intentos restantes"""
    etapas = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========''',  # 6 intentos
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========='''   # 0 intentos
    ]
    return etapas[6 - intentos]


def jugar_ahorcado():
    # Inicializamos todas las variables aquí
    palabra_secreta = random.choice(palabras).upper()
    letras_adivinadas = set()
    letras_usadas = set()
    intentos_restantes = 6   # ← Aquí se define la variable (esto faltaba)

    print("¡Bienvenido al juego del Ahorcado!")
    print("Tema: Programación y Ciberseguridad")
    print("Tienes 6 intentos para adivinar la palabra.\n")

    while intentos_restantes > 0:
        # Mostrar progreso de la palabra
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("Palabra:  ", " ".join(progreso))
        print(dibujar_ahorcado(intentos_restantes))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Ninguna'}\n")

        # Pedir letra
        letra = input("Ingresa una letra: ").upper().strip()

        # Validaciones
        if len(letra) != 1 or not letra.isalpha():
            print(" Ingresa solo una letra válida.\n")
            continue

        if letra in letras_usadas:
            print("  Ya usaste esa letra.\n")
            continue

        letras_usadas.add(letra)

        # Comprobar si la letra está en la palabra
        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print(" ¡Correcto!\n")
        else:
            intentos_restantes -= 1
            print(" Incorrecto.\n")

        # Verificar victoria
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(" ¡FELICIDADES! ¡Ganaste!")
            print(f"La palabra era: {palabra_secreta}")
            break

    # Derrota
    if intentos_restantes == 0:
        print(dibujar_ahorcado(0))
        print("¡Perdiste! Se te acabaron los intentos.")
        print(f"La palabra secreta era: {palabra_secreta}")

    # Preguntar si quiere jugar otra vez
    while True:
        respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí']:
            print("\n" + "="*60 + "\n")
            jugar_ahorcado()
            break
        elif respuesta in ['n', 'no']:
            print("¡Gracias por jugar! ")
            break
        else:
            print("Por favor responde 's' o 'n'.")


# Iniciar el juego
if __name__ == "__main__":
    jugar_ahorcado()