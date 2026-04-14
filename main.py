from gestion_datos import agregar_elemento
from validaciones import validar_entero
from utilidades import generar_encabezado, mostrar_tabla

def menu():
    while True: 
        print(f"\n{'='*20} SISTEMA DE GESTIÓN {'='*20}") # 
        print("1. Agregar Registro")
        print("2. Ver Todos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_in = validar_entero("Ingrese ID: ")
            nom = input("Nombre: ")
            cat = input("Categoría: ")
            exito, msg = agregar_elemento(id_in, nom, cat)
            print(f"Resultado: {msg}") 

        elif opcion == "2":
            from gestion_datos import registros 
            generar_encabezado("LISTADO DE REGISTROS")
            mostrar_tabla(registros)
            
        elif opcion == "3":
            print("Saliendo del sistema...")
            break 
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()