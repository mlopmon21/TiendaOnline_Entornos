# TiendaOnline_Entornos

Aplicación desarrollada como proyecto para el módulo de **Entornos de Desarrollo** en el CFGS de **Desarrollo de Aplicaciones Web (DAW)** en el **IES Abdera (Almería)**.

Este proyecto simula una tienda online sencilla que permite gestionar productos físicos y digitales, clientes, pedidos y reseñas, todo desde una interfaz por consola.

---

## Funcionalidades

- Gestión de Clientes (alta, modificación, listado)
- Gestión de Productos:
  - Productos físicos
  - Productos digitales (formato y tamaño)
- Gestión de Pedidos
  - Relación cliente-productos
  - Cálculo del total
- Gestión de Reseñas
  - Comentarios sobre productos
  - Puntuaciones

---

## Estructura del proyecto
```plaintext
├── docs
│   ├── build
│   │   ├── doctrees
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   ├── modules.doctree
│   │   │   └── project.doctree
│   │   └── html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── _modules
│   │       │   ├── index.html
│   │       │   └── project
│   │       │       ├── clientes.html
│   │       │       └── productos.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── project.html
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       ├── _sources
│   │       │   ├── index.rst.txt
│   │       │   ├── modules.rst.txt
│   │       │   └── project.rst.txt
│   │       └── _static
│   │           ├── alabaster.css
│   │           ├── base-stemmer.js
│   │           ├── basic.css
│   │           ├── custom.css
│   │           ├── doctools.js
│   │           ├── documentation_options.js
│   │           ├── file.png
│   │           ├── forkme_right_darkblue_121621.png
│   │           ├── language_data.js
│   │           ├── minus.png
│   │           ├── plus.png
│   │           ├── pygments.css
│   │           ├── searchtools.js
│   │           ├── spanish-stemmer.js
│   │           ├── sphinx_highlight.js
│   │           └── translations.js
│   ├── make.bat
│   ├── Makefile
│   └── source
│       ├── conf.py
│       ├── index.rst
│       ├── modules.rst
│       ├── project.rst
│       ├── _static
│       └── _templates
├── ManualTecnico.md
├── ManualUsuario.md
├── project
│   ├── clientes.py
│   ├── __init__.py
│   ├── main.py
│   ├── menu.py
│   ├── pedido.py
│   ├── producto_digital.py
│   ├── productos.py
│   ├── __pycache__
│   │   ├── clientes.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── menu.cpython-312.pyc
│   │   ├── pedido.cpython-312.pyc
│   │   ├── producto_digital.cpython-312.pyc
│   │   ├── productos.cpython-312.pyc
│   │   └── reseña.cpython-312.pyc
│   └── reseña.py
└── README.md
```
---

## Ejecución del programa

1. Asegúrate de tener **Python 3.12 o más instalado.
2. Ejecuta el archivo principal:

```bash
python main.py
Navega por el menú utilizando los números del 1 al 5.

🛠️ Tecnologías utilizadas
Python (POO - Programación Orientada a Objetos)

Uso de menús y diccionarios para manejar datos

No requiere base de datos ni librerías externas

📌 Notas importantes
Los datos no se guardan en archivos ni bases de datos: se mantienen en memoria durante la ejecución.

Proyecto académico para aprendizaje de programación orientada a objetos.

👩‍🎓 Autor
Nombre: Maria del Mar Lopez Montoya
Curso: 1º DAW - IES Abdera
Proyecto: Módulo de Entornos de Desarrollo
Año: 2025

📄 Licencia
Este proyecto es de uso educativo y no tiene fines comerciales.
