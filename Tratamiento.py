class tratamiento:
    codigoTratamiento=""
    tratamiento=""
    precio=""
    doctorEncargad0=""
    numeroCliente=""

    def __init__(self,codigoTratamiento,tratamiento,precio,doctorEncargado,numeroCliente):
        self.codigoTratamiento=codigoTratamiento
        self.tratamiento=tratamiento
        self.precio=precio
        self.doctorEncargado=doctorEncargado
        self.numeroCliente=numeroCliente

    def darCodigoTratamiento(self):
        print("El codigo del tratamiento es: ",self.codigoTratamiento)

    def darTratamiento(self):
        print("El tratamiento que se le va a realizar a la mascota es:",self.tratamiento)

    def darPrecio(self):
        print("El precio del tratamiento es: ",self.precio)

