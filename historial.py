# historial.py
# -------------------------------------------------------------
# Módulo que permite ver el historial de pedidos guardado.
# -------------------------------------------------------------

import os

ARCHIVO_PEDIDOS = "pedidos_cafe.txt"


def ver_historial():
    # Primero comprobamos si el archivo existe para evitar errores
    if os.path.exists(ARCHIVO_PEDIDOS):
        print("\n📜 Historial de pedidos:")

        # ---------------- LECTURA DE ARCHIVOS ----------------
        # Usamos el modo "r" (read) que significa "solo lectura".
        # El método readlines() devuelve una lista donde cada
        # elemento es una línea del archivo (un pedido).
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                # enumerate() nos da un índice (número de pedido)
                # y el contenido (el café pedido).
                for i, pedido in enumerate(pedidos, start=1):
                    # strip() elimina el salto de línea "\n"
                    print(f"{i}. {pedido.strip()}")
            else:
                print("No hay pedidos registrados todavía.")
    else:
        print("\nTodavía no existe un historial de pedidos.")
