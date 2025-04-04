import os
from productos import Producto
from clientes import Cliente
from producto_digital import ProductoDigital
from pedido import Pedido
from reseña import Reseña

# Listas y diccionarios para almacenar los objetos
lista_productos = []  # Lista para almacenar productos



dicc_clientes = {}  # Diccionario para almacenar clientes (clave:id_cliente, valor: objeto Cliente)
lista_pedidos = []  # Lista para almacenar los pedidos
lista_reseñas = []  # Lista para almacenar las reseñas

def clean_screen():
    """
    Limpia la pantalla de la terminal dependiendo del sistema operativo.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def push_enter():
    """
    Pausa la ejecución del programa hasta que el usuario presione ENTER.
    """
    input(f'\nPulsa ENTER para continuar...')

def menu_principal():
    """
    Muestra el menú principal de la tienda online.
    """
    clean_screen()
    print(f'##################################')
    print(f'# 1.- Gestionar Productos        #')
    print(f'# 2.- Gestionar Clientes         #')
    print(f'# 3.- Gestionar Pedidos          #')
    print(f'# 4.- Gestionar Reseñas          #')
    print(f'# 5.- Salir                      #')
    print(f'##################################')

def menu_productos():
    """
    Muestra el menú de gestión de productos y permite al usuario:
    - Añadir productos (físicos o digitales).
    - Listar los productos existentes.
    - Actualizar el stock de un producto.
    """
    trigger = True
    while trigger:
        clean_screen()
        print(f'############################')
        print(f'# 1.- Añadir Productos     #')
        print(f'# 2.- Listar Productos     #')
        print(f'# 3.- Actualizar Stock     #')
        print(f'# 4.- Volver al menú       #')
        print(f'############################')

        option = input(f'\nElige una opción: ')

        match option:
            case '1':
                tipo = input(f'\n¿Qué tipo de producto vas a añadir (digital o físico)?: ').lower()
                
                if tipo == 'fisico':
                    """
                    Agrega un producto físico a la lista de productos.
                    """
                    id_producto = input(f'Introduce el ID del producto (Pxxx): ').upper()
                    nombre = input(f'Introduce el nombre del producto: ').title()
                    precio = float(input(f'Introduce el precio unitario del producto: '))
                    stock = int(input(f'Introduce el stock inicial del producto: '))
                    producto = Producto(id_producto, nombre, precio, stock)
                    lista_productos.append(producto)
                    print(f'\n¡¡¡Producto creado y añadido correctamente a la lista!!!')

                elif tipo == 'digital':
                    """
                    Agrega un producto digital a la lista de productos.
                    """
                    id_producto = input(f'Introduce el ID del producto (PDxxx): ').upper()
                    nombre = input(f'Introduce el nombre del producto: ').title()
                    precio = float(input(f'Introduce el precio unitario del producto: '))
                    stock = int(input(f'Introduce el stock inicial del producto: '))
                    formato = input(f'Introduzca el formato del archivo (PDF, MP3...): ').upper()
                    tamaño = input(f'Introduzca el tamaño del archivo (ej. 20MB): ').upper()
                    producto = ProductoDigital(id_producto, nombre, precio, stock, formato, tamaño)
                    lista_productos.append(producto)
                    print(f'\n¡¡¡Producto creado y añadido correctamente a la lista!!!')
                else:
                    print(f'\n¡¡¡Debes introducir una de las opciones!!!')
                push_enter()
            case '2':
                """
                Lista todos los productos disponibles en la tienda.
                """
                print(f'\n-----Lista de productos-----')
                for producto in lista_productos:
                    print(producto)
                push_enter()
            case '3':
                """
                Permite actualizar el stock de un producto.
                """
                encontrado = False  # Para saber si encuentra el producto
                id_producto = input(f'\nIntroduce el ID del producto a buscar (Pxxx o PDxxx): ').upper()
                for producto in lista_productos:
                    if producto.get_id_producto() == id_producto:
                        encontrado = True
                        stock = int(input(f'Introduzca el nuevo stock: '))
                        producto.actualizar_stock(stock)
                        print(f'\n¡¡¡Stock actualizado!!!')
                        break
                if not encontrado:
                    print(f'\n¡¡¡Producto no encontrado!!!')
                push_enter()
            case '4':
                """
                Vuelve al menú principal.
                """
                trigger = False
            case _:
                """
                Maneja opciones incorrectas.
                """
                print(f'\n¡¡¡Opción incorrecta!!!')
                push_enter()

