# main.py
# -------------------------------------------------------------
# Archivo principal que controla el flujo de la aplicación.
# Importa los módulos de menú, pedidos e historial.
# -------------------------------------------------------------

from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:  # Bucle infinito controlado con break
        mostrar_menu()  # Mostramos las opciones del menú
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\nGracias por usar la Máquina de Café. ¡Hasta pronto! ☕")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
