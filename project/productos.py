class Producto:
    """
    Clase objeto que representa un producto.
    """    

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        """
        Inicializa un nuevo producto con los datos proporcionados.

        :param id_producto: Identificador único del producto.
        :type id_producto: str
        :param nombre: Nombre del producto.
        :type nombre: str
        :param precio: Precio del producto.
        :type precio: float
        :param stock: Cantidad disponible en stock.
        :type stock: int
        """        
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    ### GETTER y SETTER id_producto ###

    def get_id_producto(self):
        """
        Obtiene el identificador del producto.

        :return: El identificador del producto.
        :rtype: str
        """        
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        """
        Asigna un nuevo identificador al producto.

        :param id_producto: Nuevo identificador del producto.
        :type id_producto: str
        """        
        self.__id_producto = id_producto

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        """
        Obtiene el nombre del producto.

        :return: El nombre del producto.
        :rtype: str
        """        
        return self.__nombre
    
    def set_nombre(self, nombre):
        """
        Asigna un nuevo nombre al producto.

        :param nombre: Nuevo nombre del producto.
        :type nombre: str
        """        
        self.__nombre = nombre

    ### GETTER y SETTER precio ###

    def get_precio(self):
        """
        Obtiene el precio del producto.

        :return: El precio del producto.
        :rtype: float
        """        
        return self.__precio
    
    def set_precio(self, precio):
        """
        Asigna un nuevo precio al producto.

        :param precio: Nuevo precio del producto.
        :type precio: float
        """        
        self.__precio = precio

    ### GETTER y SETTER stock ###

    def get_stock(self):
        """
        Obtiene la cantidad disponible en stock del producto.

        :return: La cantidad en stock del producto.
        :rtype: int
        """        
        return self.__stock
    
    def set_stock(self, stock):
        """
        Asigna una nueva cantidad en stock al producto.

        :param stock: Nueva cantidad en stock del producto.
        :type stock: int
        """        
        self.__stock = stock

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        """
        Devuelve una representación en cadena de la información del producto.

        :return: Información detallada del producto, incluyendo su código, nombre, precio y stock.
        :rtype: str
        """        
        return f'\n- Código: {self.__id_producto}\n- Nombre: {self.__nombre}\n- Precio: {self.__precio} €\n- Stock: {self.__stock} unidades'
    
    ### Método para actualizar el stock ###

    def actualizar_stock(self, stock):
        """
        Actualiza la cantidad disponible en stock del producto.

        :param stock: Nueva cantidad en stock del producto.
        :type stock: int
        :return: Mensaje con la nueva cantidad de stock del producto.
        :rtype: str
        """        
        self.set_stock(stock)   
        return f'{self.__nombre} tiene de stock {self.__stock} unidades'
