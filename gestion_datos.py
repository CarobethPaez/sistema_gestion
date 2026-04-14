# Estructuras de datos 
registros = [] 
identificadores_unicos = set() 

def agregar_elemento(id_item, nombre, categoria):
    if id_item in identificadores_unicos:
        return False, "El ID ya existe."
    
    # Uso de diccionarios para pares clave-valor 
    nuevo_item = {
        "id": id_item,
        "nombre": nombre,
        "categoria": categoria
    }
    registros.append(nuevo_item)
    identificadores_unicos.add(id_item)
    return True, "Elemento agregado con éxito."

def calcular_total_recursivo(lista_precios):
    """Ejemplo de función recursiva para cálculos específicos."""
    if not lista_precios:
        return 0
    return lista_precios[0] + calcular_total_recursivo(lista_precios[1:])