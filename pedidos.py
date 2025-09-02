# pedidos.py
# -------------------------------------------------------------
# Módulo que gestiona la acción de pedir café y guardar en archivo.
# -------------------------------------------------------------

ARCHIVO_PEDIDOS = "pedidos_cafe.txt"


def pedir_cafe():
    print("\nElige el café que deseas:")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Opción: ")

    cafes = {"1": "Espresso", "2": "Cappuccino", "3": "Latte", "4": "Americano"}

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print(f"Has pedido un {cafe_elegido}. ¡Preparando tu café! ☕")

        # ---------------- ESCRITURA DE ARCHIVOS ----------------
        # Usamos el modo "a" (append) que significa "agregar".
        # Si el archivo no existe, Python lo crea automáticamente.
        # Si ya existe, NO borra lo anterior, solo agrega al final.
        # El "\n" es para que cada pedido quede en una nueva línea.
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción no válida, por favor intenta de nuevo.")
