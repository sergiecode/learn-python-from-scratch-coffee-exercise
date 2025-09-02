# historial.py
# -------------------------------------------------------------
# Módulo que permite ver el historial de pedidos guardado.
# -------------------------------------------------------------

import os

ARCHIVO_PEDIDOS = "pedidos_cafe.txt"

def ver_historial():
    if os.path.exists(ARCHIVO_PEDIDOS):
        print("\n📜 Historial de pedidos:")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(f"{i}. {pedido.strip()}")
            else:
                print("No hay pedidos registrados todavía.")
    else:
        print("\nTodavía no existe un historial de pedidos.")
