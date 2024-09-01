# Evaluaci-n-en-Contacto-con-el-Docente
Proyecto Final
Explicación del código:

Importar módulos: Importamos los módulos random y string para generar aleatoriedad y trabajar con cadenas de texto, respectivamente.
Función generar_contrasena: Esta función toma varios parámetros para personalizar la generación de contraseñas y devuelve una contraseña aleatoria.
Conjunto de caracteres: Se crea un conjunto con todos los caracteres posibles.
Eliminar caracteres: Se eliminan los caracteres que el usuario no desea incluir.
Crear la contraseña: Se genera una cadena aleatoria de la longitud especificada, seleccionando caracteres del conjunto válido.
Bloque if __name__ == "__main__":: Este bloque se ejecuta solo si el archivo se ejecuta directamente, no si se importa como módulo. Aquí solicitamos al usuario la longitud de la contraseña y llamamos a la función para generar y mostrar la contraseña.
Personalización:

Longitud: Puedes modificar el valor por defecto de longitud o solicitar al usuario que ingrese un valor diferente.
Caracteres excluidos: Puedes personalizar la cadena excluir_caracteres para evitar caracteres específicos.
Requisitos adicionales: Puedes agregar más lógica para cumplir con requisitos específicos de complejidad de contraseñas, como un mínimo de caracteres especiales o una combinación de mayúsculas y minúsculas.
Consideraciones adicionales:

Seguridad: Evita almacenar contraseñas en texto plano. Utiliza técnicas de hash o cifrado para protegerlas.
Usabilidad: Considera agregar opciones para guardar las contraseñas generadas en un archivo o copiarlas al portapapeles.
Entropía: Cuantos más caracteres aleatorios se incluyan, más fuerte será la contraseña.
