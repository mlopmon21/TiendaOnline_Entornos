### Variables globales y constantes ###

### Librerías ###

import menu

### Funciones ###

### Variables locales ###

trigger = True
option = ''

### Programa Principal ###

while trigger:
    menu.menu_principal()

    option = input(f'\nIntroduce una opción del menu: ')

    match option:

        case '1': 
            menu.menu_productos()

        case '2': 
            menu.menu_clientes()

        case '3': 
            menu.menu_pedidos()

        case '4': 
            menu.menu_reseñas()

        case '5': 
            print(f'\n¡¡¡GRACIAS POR UTILIZAR NUESTRO PROGRAMA!!!')
            trigger = False

        case _: 
            input(f'\n¡¡¡Opción incorrecta!!!\nPulsa ENTER para continuar...')

""" id_producto = input(f'\nIntroduce un ID para el producto: ').upper()
nombre_cliente = input(f'Introduce el nombre del producto: ') """

""" producto1 = Producto('P001', 'Disco Duro', 100.00, 10)
producto2 = Producto('P002', 'Monitor', 250.00, 5)
producto3 = ProductoDigital('PD001', 'Netflix Anual', 50.00, 25, 'PDF', '100 KB')
lista_productos.append(producto1)
lista_productos.append(producto2)
lista_productos.append(producto3)

for producto in lista_productos:
    print(producto)

cliente1 = Cliente('C001', 'Jaime', 'jaime@jaime.es', 'C/Maravillas nº 23, Adra')
cliente2 = Cliente('C002', 'Lolo', 'lolo@lolo.es', 'C/Presa nª1 El Ejido')

dicc_clientes[cliente1.get_id_cliente()] = cliente1
dicc_clientes[cliente2.get_id_cliente()] = cliente2

for cliente in dicc_clientes.values():
    print(cliente)

print()

pedido1 = Pedido('PED001', dicc_clientes['C001'], '14-03-2025')
pedido1.agregar_producto(lista_productos[0])
pedido1.agregar_producto(lista_productos[1])
print(pedido1)

lista_pedidos.append(pedido1) # Lo añadimos a la lista de pedidos

print()
reseña = Reseña('R001', lista_productos[0], dicc_clientes['C001'], 'Todo perfecto')
print(reseña)

reseña.set_puntuacion(4)
print(reseña)

lista_reseñas.append(reseña) """


