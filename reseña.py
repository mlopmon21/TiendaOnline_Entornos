from clientes import Cliente
from productos import Producto

class Reseña(Producto, Cliente):
    def __init__(self, id_reseña:str, producto:Producto, cliente:Cliente, comentario:str):
        Producto.__init__(self, producto.get_id_producto(), producto.get_nombre(), producto.get_precio(), producto.get_stock())
        Cliente.__init__(self, cliente.get_id_cliente(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())
        self.__id_reseña = id_reseña
        self.__comentario = comentario
        self.__puntuacion = None

    ### GETTER y SETTER para id_reseña ###

    def get_id_reseña(self):
        return self.__id_reseña
    
    def set_id_reseña(self, id_reseña):
        self.__id_reseña = id_reseña

    ### GETTER y SETTER para comentario ###

    def get_comentario(self):
        return self.__comentario
    
    def set_comentario(self, comentario):
        self.__comentario = comentario

    ### GETTER y SETTER para puntuacion ###

    def get_puntuacion(self):
        return self.__puntuacion
    
    def set_puntuacion(self, puntuacion):
        self.__puntuacion = puntuacion

    ### Construimos el str ###

    def __str__(self):
        return f'\n- ID_Reseña: {self.__id_reseña}\n- Producto: {self.get_id_producto()}\n- ID_Cliente: {self.get_id_cliente()}\n- Puntuación: {self.__puntuacion}\n- Comentario: {self.__comentario}' 