def validar_entero(mensaje):
    """
    Solicita un dato y asegura que sea un número entero.
    Maneja la excepción si el usuario ingresa letras o símbolos.
    """
    while True:
        try:
            # Intentamos convertir la entrada a entero
            valor = int(input(mensaje))
            return valor
        except ValueError:
            # Si ocurre un error de valor (como ingresar 'abc'), se ejecuta esto:
            print("❌ Error: Por favor, ingrese un número entero válido (no se permiten letras).")
    


def validar_cadena(mensaje):
    """Valida que la entrada sea una cadena no vacía."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: La entrada no puede estar vacía.")
            continue
        return valor
    

def validar_numero_positivo(mensaje):
    """Valida que la entrada sea un número entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Error: Por favor, ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
    
