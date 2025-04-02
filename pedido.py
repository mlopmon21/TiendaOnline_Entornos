from clientes import Cliente

class Pedido:
    """
    Clase que representa un pedido en el sistema de tienda online.
    """

    def __init__(self, id_pedido: str, cliente: Cliente, fecha: str):
        """
        Inicializa un nuevo pedido con los datos proporcionados.

        :param id_pedido: Identificador único del pedido.
        :type id_pedido: str
        :param cliente: Cliente asociado al pedido.
        :type cliente: Cliente
        :param fecha: Fecha en la que se realizó el pedido.
        :type fecha: str
        """
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha

    ### GETTER y SETTER para id_pedido ###
    
    def get_id_pedido(self):
        """
        Obtiene el identificador del pedido.

        :return: El identificador del pedido.
        :rtype: str
        """
        return self.__id_pedido
    
    def set_id_pedido(self, id_pedido):
        """
        Asigna un nuevo identificador al pedido.

        :param id_pedido: Nuevo identificador del pedido.
        :type id_pedido: str
        """
        self.__id_pedido = id_pedido

    ### GETTER y SETTER para cliente ###
    
    def get_cliente(self):
        """
        Obtiene el cliente asociado al pedido.

        :return: Cliente asociado al pedido.
        :rtype: Cliente
        """
        return self.__cliente
    
    def set_cliente(self, cliente):
        """
        Asigna un nuevo cliente al pedido.

        :param cliente: Nuevo cliente asociado al pedido.
        :type cliente: Cliente
        """
        self.__cliente = cliente

    ### GETTER y SETTER para fecha ###
    
    def get_fecha(self):
        """
        Obtiene la fecha del pedido.

        :return: Fecha en la que se realizó el pedido.
        :rtype: str
        """
        return self.__fecha
    
    def set_fecha(self, fecha):
        """
        Asigna una nueva fecha al pedido.

        :param fecha: Nueva fecha del pedido.
        :type fecha: str
        """
        self.__fecha = fecha

    ### GETTER para lista de productos ###
    
    def get_lista_productos(self):
        """
        Obtiene la lista de productos en el pedido.

        :return: Lista de productos agregados al pedido.
        :rtype: list
        """
        return self.__productos

    ### Agregar productos ###
    
    def agregar_producto(self, producto: object):
        """
        Agrega un producto al pedido.

        :param producto: Producto a agregar en el pedido.
        :type producto: object
        """
        self.__productos.append(producto)

    ### Calcular el total del pedido ###
    
    def calcular_total(self):
        """
        Calcula el costo total del pedido sumando los precios de los productos.

        :return: Suma total del pedido.
        :rtype: float
        """
        suma = 0.0
        for producto in self.__productos:
            suma += producto.get_precio()
        return suma

    ### Construimos el str ###
    
    def __str__(self):
        """
        Devuelve una representación en cadena del pedido.

        :return: Información detallada del pedido, incluyendo el ID, cliente, fecha y lista de productos.
        :rtype: str
        """
        return f'\n- Pedido: {self.__id_pedido}\n- Cliente: {self.__cliente.get_nombre()}\n- Fecha: {self.__fecha}\n- Lista Productos: {self.__productos}'
   