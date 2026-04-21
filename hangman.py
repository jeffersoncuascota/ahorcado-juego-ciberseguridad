import random
from typing import Tuple, List, Set

# ====================== DATOS DEL JUEGO ======================
# Usamos tuplas para datos inmutables (buena práctica)
TEMAS: Tuple[str, ...] = (
    "Programación", 
    "Inteligencia Artificial", 
    "Ciberseguridad", 
    "Tecnologías Emergentes", 
    "Impacto Social de la Tecnología"
)

# Lista de palabras relacionadas con el tema del proyecto
palabras: List[str] = [
    "PYTHON", "ALGORITMO", "INTELIGENCIA", "ARTIFICIAL", "BLOCKCHAIN",
    "AUTOMATIZACION", "PRIVACIDAD", "CIBERSEGURIDAD", "GITHUB", "STREAMLIT",
    "VISUALIZACION", "FUTURO", "IMPACTO", "ETICA", "ROBOTICA", "CUANTICA",
    "REALIDAD", "AUMENTADA", "SOCIEDAD", "DESARROLLO", "FUNCIONAL"
]

# Etapas del ahorcado como tupla de strings (inmutable)
ETAPAS_AHORCADO: Tuple[str, ...] = (
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
    ========='''   # 0 intentos (derrota)
)

# ====================== FUNCIONES ======================

def obtener_palabra_secreta() -> str:
    """Selecciona una palabra aleatoria y retorna en mayúsculas"""
    return random.choice(palabras)


def dibujar_ahorcado(intentos: int) -> str:
    """Retorna el dibujo del ahorcado según los intentos restantes"""
    indice = 6 - intentos
    if indice < 0:
        indice = 0
    elif indice >= len(ETAPAS_AHORCADO):
        indice = len(ETAPAS_AHORCADO) - 1
    return ETAPAS_AHORCADO[indice]


def mostrar_progreso(palabra: str, letras_adivinadas: Set[str]) -> str:
    """Retorna la palabra con guiones en las letras no adivinadas"""
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def jugar_ahorcado() -> None:
    """Función principal del juego"""
    palabra_secreta: str = obtener_palabra_secreta()
    letras_adivinadas: Set[str] = set()
    letras_usadas: Set[str] = set()
    intentos_restantes: int = 6

    print("=" * 60)
    print("     ¡BIENVENIDO AL AHORCADO - VISUALIZACIÓN DEL FUTURO!")
    print(f"     Tema: {random.choice(TEMAS)}")
    print("=" * 60)
    print("Tienes 6 intentos para adivinar la palabra relacionada con tecnología.\n")

    while intentos_restantes > 0:
        print(f"\nPalabra:  {mostrar_progreso(palabra_secreta, letras_adivinadas)}")
        print(dibujar_ahorcado(intentos_restantes))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Ninguna'}")

        letra = input("\nIngresa una letra: ").upper().strip()

        # Validaciones
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa solo una letra válida.\n")
            continue

        if letra in letras_usadas:
            print("Ya usaste esa letra.\n")
            continue

        letras_usadas.add(letra)

        # Comprobar letra
        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Correcto!\n")
        else:
            intentos_restantes -= 1
            print("Incorrecto.\n")

        # Verificar victoria
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡FELICIDADES! ¡Ganaste!")
            print(f"La palabra era: {palabra_secreta}")
            break

    # Derrota
    if intentos_restantes == 0:
        print(dibujar_ahorcado(0))
        print("¡Perdiste! Se te acabaron los intentos.")
        print(f"La palabra secreta era: {palabra_secreta}")

    # Preguntar si quiere jugar de nuevo
    while True:
        respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí']:
            print("\n" + "="*60 + "\n")
            jugar_ahorcado()
            break
        elif respuesta in ['n', 'no']:
            print("\n¡Gracias por jugar! Reflexiona sobre cómo la tecnología está cambiando nuestra sociedad.")
            break
        else:
            print("Por favor responde 's' o 'n'.")


# ====================== EJECUCIÓN ======================
if __name__ == "__main__":
    jugar_ahorcado()