lista_productos = [] # Lista para almacenar productos
dicc_clientes = {} # Diccionario para almacenar clientes (clave:id_cliente, valor: objeto Cliente)
lista_pedidos = [] # Lista para almacenar los pedidos
lista_reseñas = [] # Lista para almacenar las reseñas

import os
from productos import Producto
from clientes import Cliente
from producto_digital import ProductoDigital
from pedido import Pedido
from reseña import Reseña


def clean_screen():
    if os == 'nt':
        os.system('cls')
    else: 
        os.system('clear')


def push_enter():
    input(f'\nPulsa ENTER para continuar...')


def menu_principal():
    
    clean_screen()

    print(f'##################################')
    print(f'# 1.- Gestionar Productos        #')
    print(f'# 2.- Gestionar Clientes         #')
    print(f'# 3.- Gestionar Pedidos          #')
    print(f'# 4.- Gestionar Reseñas          #')
    print(f'# 5.- Salir                      #')
    print(f'##################################')


def menu_productos():
    
    trigger = True

    while trigger:

        clean_screen()

        print(f'############################')
        print(f'# 1.- Añadir Productos     #')
        print(f'# 2.- Listar Productos     #')
        print(f'# 3.- Actualizar Stock     #')
        print(f'# 4.- Volver al menu       #')
        print(f'############################')

        option = input(f'\nElige una opción: ')

        match option:

            case '1':

                tipo = input(f'\n¿Qué tipo de producto vas a añadir (digital o físico)?: ').lower()

                if tipo == 'fisico':

                    id_producto = input(f'Introduce el ID del producto (Pxxx): ').upper()
                    nombre = input(f'Introduce el nombre del producto: ').title()
                    precio = float(input(f'Introduce el precio unitario del producto: '))
                    stock = int(input(f'Introduce el stock inicial del producto: '))

                    producto = Producto(id_producto,nombre,precio,stock)
                    
                    lista_productos.append(producto)
                    print(f'\n¡¡¡Producto creado y añadido correctamente a la lista!!!')


                elif tipo == 'digital':
                    id_producto = input(f'Introduce el ID del producto (PDxxx): ').upper()
                    nombre = input(f'Introduce el nombre del producto: ').title()
                    precio = float(input(f'Introduce el precio unitario del producto: '))
                    stock = int(input(f'Introduce el stock inicial del producto: '))
                    formato = input(f'Introduzca el formato del archivo (PDF, MP3...): ').upper()
                    tamaño = input(f'Introduzca el tamaño del archivo (ej. 20MB): ').upper()

                    producto = ProductoDigital(id_producto,nombre,precio,stock,formato,tamaño)
                    
                    lista_productos.append(producto)
                    print(f'\n¡¡¡Producto creado y añadido correctamente a la lista!!!')
                
                else:
                    print(f'\n¡¡¡Debes introducir una de las opciones!!!')
                
                push_enter()                

            case '2':
                print(f'\n-----Lista de productos-----')
                for producto in lista_productos:
                    print(producto)

                push_enter()

            case '3':
                encontrado = False # Para saber si encuentra el producto

                id_producto = input(f'\nIntroduce el ID del producto a buscar (Pxxx): ').upper()

                for producto in lista_productos:
                    if producto.get_id_producto() == id_producto:
                        encontrado = True
                        stock = int(input(f'Introduzca el nuevo stock: '))
                        producto.actualizar_stock(stock)
                        print(f'\n¡¡¡Stock actualizado!!!')
                        break
                
                if encontrado == False:
                    print(f'\n¡¡¡Producto no encontrado!!!')

                push_enter()

            case '4':
                trigger = False

            case _:
                print(f'\n¡¡¡Opción incorrecta!!!')
                push_enter()


def menu_clientes():
    
    trigger = True

    while trigger:

        clean_screen()

        print(f'############################')
        print(f'# 1.- Añadir Clientes      #')
        print(f'# 2.- Listar Clientes      #')
        print(f'# 3.- Volver al menu       #')
        print(f'############################')

        option = input(f'\nIntroduce una opción del menu: ')

        match option:

            case '1':
                id_cliente = input(f'\nIntroduzca el ID del cliente (Cxxx): ').upper()
                nombre = input(f'Introduzca el nombre del cliente: ').title()
                email = input(f'Introduzca el email del cliente: ').lower()
                direccion = input(f'Introduzca la dirección del cliente: ').title()

                cliente = Cliente(id_cliente,nombre,email,direccion)

                dicc_clientes[id_cliente] = cliente
                print(f'\n¡¡¡Cliente creado y añadido correctamente al diccionario!!!')
                push_enter()

            case '2':
                print(f'\n-----Lista de clientes-----')
                for cliente in dicc_clientes.values():
                    print (cliente)

                push_enter()

            case '3':
                trigger = False

            case _:
                print(f'\n¡¡¡Opción incorrecta!!!')
                push_enter()


def menu_pedidos():
    
    trigger = True
    
    while trigger:

        clean_screen()

        print(f'###################################')
        print(f'# 1.- Crear Pedido                #')
        print(f'# 2.- Añadir producto a pedido    #')
        print(f'# 3.- Listar Pedidos              #')
        print(f'# 4.- Calcular total del pedido   #')
        print(f'# 5.- Volver al menu              #')
        print(f'###################################')

        option = input(f'\nIntroduce una opción del menu: ')

        match option:

            case '1':
                
                if len(lista_productos) == 0:
                    print(f'\n¡¡¡No hay productos disponibles en tienda!!!')
                    push_enter()

                else:
                    id_pedido = input(f'\nIntroduce el ID del pedido (PEDxxx): ').upper()
                    id_cliente = input(f'Introduce el ID del cliente (Cxxx): ').upper()
                    fecha = input(f'Introduce la fecha del pedido (dd/mm/aaaa): ')

                    if id_cliente in dicc_clientes:
                        cliente = dicc_clientes[id_cliente]

                        pedido = Pedido(id_pedido, cliente, fecha)

                        lista_pedidos.append(pedido)
                        print(f'\n¡¡¡Pedido creado y añadido a la lista correctamente!!!')
                        push_enter()

                    else:
                        print(f'\n¡¡¡Cliente no encontrado!!!')
                        push_enter()

            case '2':
                encuentra_pedido = False
                encuentra_producto = False

                id_pedido = input(f'\nIntroduce el ID del pedido (PEDxxx): ').upper()
                id_producto = input(f'Introduce el ID del producto (Pxxx) o (PDxxx): ').upper()

                for pedido in lista_pedidos:
                    if pedido.get_id_pedido() == id_pedido:

                        for producto in lista_productos:
                            if producto.get_id_producto() == id_producto:

                                pedido.agregar_producto(producto)
                                encuentra_producto = True
                                break
                            
                        encuentra_pedido = True
                        break
                
                if encuentra_pedido and encuentra_producto:
                    print(f'\n¡¡¡Producto añadido correctamente a la lista de pedidos!!!')
                    push_enter()

                else:
                    print(f'\n¡¡¡Producto o pedido no encontrados!!!')
                    push_enter()     

            case '3':
                print(f'\n-----Lista de pedidos-----')
                for pedido in lista_pedidos:
                    print (pedido)

                push_enter()

            case '4':
                encuentra_pedido = False

                id_pedido = input(f'\nIntroduce el ID del pedido (PEDxxx): ').upper()

                for pedido in lista_pedidos:
                    if pedido.get_id_pedido() == id_pedido:
                        print(f'\nEl total del pedido {id_pedido} es {pedido.calcular_total()} €')
                        encuentra_pedido = True
                        break
                
                if encuentra_pedido == False:
                    print(f'\n¡¡¡No existe un pedido con ese código!!!')

                push_enter()

            case '5':
                trigger = False

            case _:
                print(f'\n¡¡¡Opción incorrecta!!!')
                push_enter()

def menu_reseñas():

    trigger = True

    while trigger:
    
        clean_screen()

        print(f'############################')
        print(f'# 1.- Añadir Reseña        #')
        print(f'# 2.- Listar Reseñas       #')
        print(f'# 3.- Volver al menu       #')
        print(f'############################')

        option = input(f'\nIntroduce una opción del menu: ')

        match option:

            case '1':
                encuentra_pedido = False
                encuentra_producto = False

                id_pedido = input(f'\nIntroduce el ID del pedido (PEDxxx): ').upper()
                id_producto = input(f'Introduce el ID del producto (Pxxx) o (PDxxx): ').upper()

                for pedido in lista_pedidos:
                    if pedido.get_id_pedido() == id_pedido:
                        encuentra_pedido = True

                        for producto in pedido.get_lista_productos():
                            if producto.get_id_producto() == id_producto:
                                encuentra_producto = True

                                id_reseña = input(f'\nIntroduce el código para la reseña (RESxxx): ')
                                puntuacion = int(input(f'Introduce una puntuación (1-5): '))
                                
                                comentario = input(f'Introduce un comentario del producto: ')

                                reseña = Reseña(id_reseña, producto, pedido.get_cliente(),comentario)

                                if puntuacion < 1:
                                    reseña.set_puntuacion(1)

                                elif puntuacion > 5:
                                    reseña.set_puntuacion(5)

                                else:
                                    reseña.set_puntuacion(puntuacion)

                                lista_reseñas.append(reseña)                                
                                break

                        encuentra_pedido = True
                        break

                if encuentra_pedido and encuentra_producto:
                    print(f'\n¡¡¡Reseña registrada correctamente en la lista!!!')
                    push_enter()

                else:
                    print(f'\n¡¡¡Producto o pedido no encontrados!!!')
                    push_enter()

            case '2':
                print(f'\n-----Lista de reseñas-----')
                for reseña in lista_reseñas:
                    print (reseña)

                push_enter()

            case '3':
                trigger = False

            case _:
                print(f'\n¡¡¡Opción incorrecta!!!')
                push_enter()
