def generar_encabezado(titulo):
    ancho = 50
    print("\n" + "=" * ancho)
    print(f"{titulo.center(ancho)}")
    print("=" * ancho)

def mostrar_tabla(lista_elementos):
    """
    Muestra los datos en un formato de tabla organizada. 
    """
    if not lista_elementos:
        print("\n[!] No hay datos registrados para mostrar.")
        return

    # Se definen los encabezados en una tupla (datos inmutables) 
    cabecera = ("ID", "NOMBRE", "CATEGORÍA")
    
    print(f"\n{cabecera[0]:<10} | {cabecera[1]:<20} | {cabecera[2]:<15}")
    print("-" * 50)
    
    for item in lista_elementos:
        # Acceso a datos del diccionario 
        print(f"{item['id']:<10} | {item['nombre']:<20} | {item['categoria']:<15}")

def formatear_resultado_busqueda(item):
    """
    Devuelve una representación formateada de un solo objeto. 
    """
    return (f"Registro Encontrado:\n"
            f" > ID: {item['id']}\n"
            f" > Nombre: {item['nombre']}\n"
            f" > Categoría: {item['categoria']}")