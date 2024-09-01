import random
import string

def generar_contrasena(longitud=12, incluir_minusculas=True, incluir_mayusculas=True,
                       incluir_numeros=True, incluir_simbolos=True,
                       excluir_caracteres=""):
    """
    Genera una contraseña aleatoria y segura.

    Args:
        longitud (int, opcional): Longitud de la contraseña. Por defecto, 12.
        incluir_minusculas (bool, opcional): Incluir letras minúsculas. Por defecto, True.
        incluir_mayusculas (bool, opcional): Incluir letras mayúsculas. Por defecto, True.
        incluir_numeros (bool, opcional): Incluir números. Por defecto, True.
        incluir_simbolos (bool, opcional): Incluir símbolos. Por defecto, True.
        excluir_caracteres (str, opcional): Caracteres a excluir. Por defecto, "".

    Returns:
        str: Contraseña generada.
    """

    # Conjunto de todos los caracteres posibles
    todos_los_caracteres = string.ascii_letters + string.digits + string.punctuation

    # Eliminar caracteres a excluir
    caracteres_validos = set(todos_los_caracteres) - set(excluir_caracteres)

    # Crear la contraseña
    contrasena = ''.join(random.choice(list(caracteres_validos)) for _ in range(longitud))

    return contrasena

if __name__ == "__main__":
    # Obtener la longitud de la contraseña desde el usuario
    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))

    # Generar y mostrar la contraseña
    contrasena = generar_contrasena(longitud)
    print("Contraseña generada:", contrasena)