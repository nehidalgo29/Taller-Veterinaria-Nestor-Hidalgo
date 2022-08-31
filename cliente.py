class cliente:
    numeroCliente=""
    nombreCliente=""
    direccionCliente=""
    telefonoCelular=""
    saldo=""

    def __init__(self,numeroCliente,nombreCliente,direccionCliente,telefonoCelular,saldo):
        self.numeroCliente=numeroCliente
        self.nombreCliente=nombreCliente
        self.direccionCliente=direccionCliente
        self.telefonoCelular=telefonoCelular
        self.saldo=saldo

    def darNumeroCliente(self):
        print("El numero  del cliente dueño de la mascota es: ",self.numeroCliente)

    def darNombreCliente(self):
        print("El nombre del cliente es: ",self.nombreCliente)

    def  darDireccionCliente(self):
        print("La direccion del cliente es: ",self.direccionCliente)
        