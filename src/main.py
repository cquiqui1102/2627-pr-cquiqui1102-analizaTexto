# Desarrolla un programa en Python que solicite una frase y calcule el número total de vocales y de palabras que contiene.

def analizar_texto(frase: str) -> tuple[int, int]:
    """
    Cuenta el número de vocales y el número de palabras introducidas

    Args:
    Una frase dadad por el usuario

    Returns:
    Número de vocales (incluidas acentuadas, mayúsculas y ü)
    Número de palabras

    """

    VOCALES: str = "aeiouüáéíóú"

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
    El número de vocales y el número de palabras
    
    """

    # Entrada
    frase: str = input("Introduzca una frase: ")

    # Salida
    numero_vocales, numero_palabras = analizar_texto(frase)

    print(f"Vocales: {numero_vocales}")
    print(f"Palabras: {numero_palabras}")

if __name__ == "__main__":
    main()