# Desarrolla un programa en Python que solicite una frase y calcule el número total de vocales y de palabras que contiene.

VOCALES: str = "aeiouüáéíóú"


def analizar_texto(frase: str) -> tuple[int, int]:
    """
    Calcula el número de vocales y el número de palabras introducidas.

    Args:
    frase: Frase dada por el usuario

    Returns:
    tuple[int, int] = Número de vocales, Número de palabras

    """

    numero_vocales: int = 0

    for letra in frase.lower():
        if letra in VOCALES:
            numero_vocales += 1

    palabra: list[str] = frase.split()
    numero_palabras: int = len(palabra)

    return numero_vocales, numero_palabras



def main():
    """
    Función principal
    
    Args:
    Frase introducida por el usuario
    
    Returns:
    Número de vocales
    Númer de palabras
    
    """

    # Entrada
    
    frase: str = input("Introduzca una frase: ")

    # Salida

    numero_vocales, numero_palabras = analizar_texto(frase)

    print(f"Vocales: {numero_vocales}")
    print(f"Palabras: {numero_palabras}")

if __name__ == "__main__":
    main()