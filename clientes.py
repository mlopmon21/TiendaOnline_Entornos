class Cliente:
    """Clase objeto que representa al cliente.
    """    
    def __init__(self, id_cliente:str, nombre:str, email:str, direccion:str):
        """Crea un nuevo que cliente con los datos que nos proporciona

        :param id_cliente:Identificador único del cliente
        :type id_cliente: str
        :param nombre: Nombre completo del cliente
        :type nombre: str
        :param email: Dirección de correo del cliente
        :type email: str
        :param direccion: Dirección del domicilio del cliente
        :type direccion: str
        """        
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    ### GETTER y SETTER id_cliente ###

    def get_id_cliente(self):
        """Obtiene el identificador del cliente

        :return: El identificador del cliente
        :rtype: str
        """        
        return self.__id_cliente
    
    def set_id_cliente(self, id_cliente):
        """Asigna un nuevo identificador al cliente 

        :param id_cliente: str
        :type id_cliente:  El nuevo identificador del cliente
        """          
        self.__id_cliente = id_cliente

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        """Obtiene el nombre del cliente
        :return: El nombre del cliente
        :rtype: str:
        """            
        return self.__nombre
    
    def set_nombre(self, nombre):
        """Se encarga de asignar un nuevo nombre al cliente

        :param nombre: El nuevo nombre del cliente
        :type nombre: str
        """             
        self.__nombre = nombre

    ### GETTER y SETTER email ###

    def get_email(self):
        """Obtiene el correo electrónico del cliente

        :return: El correo electrónico del cliente
        :rtype: str
        """      
        return self.__email
    
    def set_email(self, email):
        """Asigna un nuevo correo electrónico al cliente

        :param email: El nuevo correo electrónico del cliente
        :type email: str
        """            
        self.__email = email

    ### GETTER y SETTER direccion ###

    def get_direccion(self):
        """Obtiene la dirección del domicilio de nuestro cliente 

        :return: La dirección del domicilio de nuestro cliente
        :rtype: str
        """        
        return self.__direccion
    
    def set_direccion(self, direccion):
        """Asigna una nueva dirección a nuestro cliente

        :param direccion: La nueva dirección del domicilio de nuestro cliente
        :type direccion: str
        """        
        self.__direccion = direccion

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        """Devuelve toda la información del cliente

        :return: Información detallada del cliente, incluyendo el id, nombre, email y dirección.
        :rtype: str
        """        
        return f'\n- Código: {self.__id_cliente}\n- Nombre: {self.__nombre}\n- Email: {self.__email}\n- Dirección: {self.__direccion}'