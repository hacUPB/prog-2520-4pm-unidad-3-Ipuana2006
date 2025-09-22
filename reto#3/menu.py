from moduloreto import *   # Importa todas las funciones del módulo

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. (Problema pendiente)")
        print("2. Simulación de vuelo")
        print("3. Compra de boletos")
        print("4. Salir")

        try:
            opcion = int(input("Elija una opción >> "))
        except ValueError:
            print("Opción inválida, ingrese un número.")
            continue

        match opcion:
            case 1:
                print(" Aquí podrías poner el primer problema cuando lo tengas listo")
            case 2:
                simulacion_vuelo()   # Llamada directa, sin "moduloreto."
            case 3:
                main()               # Igual, directa
            case 4:
                print(" Saliendo del programa...")
                break
            case _:
                print(" Opción no válida. Intente de nuevo.")

# Ejecutar
if __name__ == "__main__":
    menu_principal()


