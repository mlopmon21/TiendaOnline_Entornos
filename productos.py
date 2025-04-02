class Producto:
    def __init__(self, id_producto:str, nombre:str, precio:float, stock:int):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    ### GETTER y SETTER id_producto ###

    def get_id_producto(self):
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    ### GETTER y SETTER precio ###

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

    ### GETTER y SETTER stock ###

    def get_stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        return f'\n- Código: {self.__id_producto}\n- Nombre: {self.__nombre}\n- Precio: {self.__precio} €\n- Stock: {self.__stock} unidades'
    
    ### Método para actualizar el stock ###

    def actualizar_stock(self, stock):
        self.set_stock(stock)
        return f'{self.__nombre} tiene de stock {self.__stock} unidades'