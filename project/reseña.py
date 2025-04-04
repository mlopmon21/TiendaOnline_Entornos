from clientes import Cliente
from productos import Producto

class Reseña(Producto, Cliente):
    """
    Clase que representa una reseña realizada por un cliente sobre un producto.
    Hereda de Producto y Cliente para obtener sus atributos y métodos.
    """
    def __init__(self, id_reseña: str, producto: Producto, cliente: Cliente, comentario: str):
        """
        Inicializa una reseña con un identificador, el producto reseñado, el cliente que la realiza y un comentario.

        :param id_reseña: Identificador único de la reseña.
        :type id_reseña: str
        :param producto: Producto al que se le realiza la reseña.
        :type producto: Producto
        :param cliente: Cliente que realiza la reseña.
        :type cliente: Cliente
        :param comentario: Comentario descriptivo de la reseña.
        :type comentario: str
        """        
        Producto.__init__(self, producto.get_id_producto(), producto.get_nombre(), producto.get_precio(), producto.get_stock())
        Cliente.__init__(self, cliente.get_id_cliente(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())
        self.__id_reseña = id_reseña
        self.__comentario = comentario
        self.__puntuacion = None

    def get_id_reseña(self):
        """Obtiene el identificador de la reseña."""
        return self.__id_reseña
    
    def set_id_reseña(self, id_reseña):
        """Establece el identificador de la reseña."""
        self.__id_reseña = id_reseña

    def get_comentario(self):
        """Obtiene el comentario de la reseña."""
        return self.__comentario
    
    def set_comentario(self, comentario):
        """Establece el comentario de la reseña."""
        self.__comentario = comentario

    def get_puntuacion(self):
        """Obtiene la puntuación asignada al producto en la reseña."""
        return self.__puntuacion
    
    def set_puntuacion(self, puntuacion):
        """Establece la puntuación del producto en la reseña."""
        self.__puntuacion = puntuacion

    def __str__(self):
        """Devuelve una representación en cadena de la reseña."""
        return (f'\n- ID_Reseña: {self.__id_reseña}'
                f'\n- Producto: {self.get_id_producto()}'
                f'\n- ID_Cliente: {self.get_id_cliente()}'
                f'\n- Puntuación: {self.__puntuacion}'
                f'\n- Comentario: {self.__comentario}')
