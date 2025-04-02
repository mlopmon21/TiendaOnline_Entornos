from productos import Producto

class ProductoDigital(Producto):
    def __init__(self, id_producto:str, nombre:str, precio:float, stock:int, formato:str, tamano:float):

        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamano = tamano

    ### GETTER y SETTER formato ###

    def get_formato(self):
        return self.__formato
    
    def set_formato(self, formato):
        self.__formato = formato

    ### GETTER y SETTER tamaño ###

    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self, tamano):
        self.__tamano = tamano

    ### Construir el str (Se reconstruye el del padre porque nos vale) ###

    def __str__(self):
        return f' {super().__str__()}\n- Formato: {self.__formato}\n- Tamaño: {self.__tamano}' 
