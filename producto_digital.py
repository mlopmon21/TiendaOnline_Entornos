from productos import Producto

class ProductoDigital(Producto):
    """
    Representa un producto digital en la tienda.
    Hereda de la clase Producto e incluye atributos específicos de productos digitales.
    """
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        """
        Inicializa un producto digital con sus atributos.
        
        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param stock: Cantidad disponible en inventario.
        :param formato: Formato del producto digital (ej. PDF, MP3).
        :param tamano: Tamaño del archivo en MB o GB.
        """
        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamano = tamano

    def get_formato(self):
        """Devuelve el formato del producto digital."""
        return self.__formato
    
    def set_formato(self, formato):
        """Establece el formato del producto digital."""
        self.__formato = formato

    def get_tamano(self):
        """Devuelve el tamaño del archivo del producto digital."""
        return self.__tamano
    
    def set_tamano(self, tamano):
        """Establece el tamaño del archivo del producto digital."""
        self.__tamano = tamano

    def __str__(self):
        """Devuelve una representación en cadena del producto digital."""
        return f' {super().__str__()}\n- Formato: {self.__formato}\n- Tamaño: {self.__tamano}'
