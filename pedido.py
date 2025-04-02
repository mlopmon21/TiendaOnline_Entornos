from clientes import Cliente

class Pedido:
    def __init__(self, id_pedido:str, cliente: Cliente, fecha:str):
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha

    ### GETTER y SETTER para id_pedido ###
    def get_id_pedido(self):
        return self.__id_pedido
    
    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    ### GETTER y SETTER para cliente ###
    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self, cliente):
        self.__cliente = cliente

    ### GETTER y SETTER para fecha ###
    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self, fecha):
        self.__fecha = fecha

    ### GETTER para lista productos ###
    def get_lista_productos(self):
        return self.__productos

    ### Agregar productos ###
    def agregar_producto(self, producto:object):
        self.__productos.append(producto)

    ### Calcular el total del pedido ###
    def calcular_total(self):
        suma = 0.0
        for producto in self.__productos:
            suma += producto.get_precio()

        return suma

    ### Construimos el str ###

    def __str__(self):
        return f'\n- Pedido: {self.__id_pedido}\n- Cliente: {self.__cliente.get_nombre()}\n- Fecha: {self.__fecha}\n- Lista Productos: {self.__productos}'    