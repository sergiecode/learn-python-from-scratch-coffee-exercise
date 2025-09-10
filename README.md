# ☕ Máquina de Café - Simulador en Python

Un proyecto educativo que simula una máquina de café interactiva desarrollado en Python. Este proyecto está diseñado para enseñar conceptos fundamentales de programación como manejo de archivos, modularización, bucles y control de flujo.

## 📋 Descripción

La **Máquina de Café** es una aplicación de consola que permite a los usuarios:
- Elegir entre diferentes tipos de café
- Hacer pedidos y guardarlos automáticamente 
- Ver el historial completo de pedidos realizados
- Navegar por un menú interactivo intuitivo

## ✨ Características

- **Interfaz de consola amigable** con emojis y mensajes claros
- **4 tipos de café disponibles**: Espresso, Cappuccino, Latte y Americano
- **Persistencia de datos**: Los pedidos se guardan en un archivo de texto
- **Historial de pedidos**: Visualización de todos los cafés pedidos anteriormente
- **Arquitectura modular**: Código organizado en módulos separados para mejor mantenimiento

## 🏗️ Estructura del Proyecto

```
📦 learn-python-from-scratch-practica-cafe
├── 📄 main.py          # Archivo principal - controla el flujo de la aplicación
├── 📄 menu.py          # Módulo del menú principal 
├── 📄 pedidos.py       # Gestión de pedidos y guardado en archivo
├── 📄 historial.py     # Visualización del historial de pedidos
├── 📄 README.md        # Documentación del proyecto
└── 📄 pedidos_cafe.txt # Archivo generado automáticamente para guardar pedidos
```

## 🚀 Cómo usar

1. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

2. **Navegar por el menú**:
   - Opción 1: Pedir un café
   - Opción 2: Ver historial de pedidos
   - Opción 3: Salir de la aplicación

3. **Hacer un pedido**:
   - Selecciona el tipo de café deseado (1-4)
   - El pedido se guarda automáticamente en `pedidos_cafe.txt`

4. **Ver historial**:
   - Muestra todos los cafés pedidos hasta el momento
   - Los pedidos están numerados y ordenados cronológicamente

## 🎯 Conceptos de Programación Demostrados

- **Modularización**: Separación de funcionalidades en archivos diferentes
- **Manejo de archivos**: Escritura y lectura de archivos de texto
- **Bucles y control de flujo**: Uso de `while`, `if/elif/else`
- **Diccionarios**: Mapeo de opciones de menú
- **Manejo de excepciones**: Validación de entradas del usuario
- **Encoding UTF-8**: Soporte para caracteres especiales y emojis

## 📚 Requisitos

- Python 3.6 o superior
- No se requieren librerías externas (solo módulos estándar de Python)

## 🎓 Propósito Educativo

Este proyecto es ideal para:
- **Principiantes** que están aprendiendo Python desde cero
- **Estudiantes** que quieren practicar conceptos básicos de programación
- **Personas** que desean entender la modularización de código
- **Desarrolladores** que buscan ejemplos simples de manejo de archivos

## 🔧 Posibles Mejoras

- Agregar precios a los cafés y calcular totales
- Implementar un sistema de usuarios
- Añadir fecha y hora a los pedidos
- Crear una interfaz gráfica con tkinter
- Agregar validación de stock de ingredientes

---

## 👨‍💻 Autor

**Sergie Code** - Software Engineer y Educador de Programación

### 🌐 Sígueme en mis redes sociales:

- 📸 **Instagram**: https://www.instagram.com/sergiecode
- 🧑🏼‍💻 **LinkedIn**: https://www.linkedin.com/in/sergiecode/
- 📽️ **YouTube**: https://www.youtube.com/@SergieCode
- 😺 **GitHub**: https://github.com/sergiecode
- 👤 **Facebook**: https://www.facebook.com/sergiecodeok
- 🎞️ **TikTok**: https://www.tiktok.com/@sergiecode
- 🕊️ **Twitter**: https://twitter.com/sergiecode
- 🧵 **Threads**: https://www.threads.net/@sergiecode

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto o encuentras algún bug, no dudes en:
- Abrir un issue
- Enviar un pull request
- Contactarme en mis redes sociales


¡Gracias por tu interés en aprender programación! ☕💻
