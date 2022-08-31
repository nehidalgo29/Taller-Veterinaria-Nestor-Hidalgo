from mimetypes import init


class clinica:
    nombreClinica=""
    direccion=""
    ciudad=""
    telefono=0
    gerente=""

    def __init__(self,nombreClinica,direccion,ciudad,telefono,gerente):
        self.nombreClinica=nombreClinica
        self.direccion=direccion
        self.ciudad=ciudad
        self.telefono=telefono
        self.gerente=gerente

    def darNombreClinica(self):
        print("El nombre de la clinica es: ",self.nombreClinica)
    
    def darDireccion(self):
        print("La direccion de la clinica es: ",self.direccion)

    def darCiudad(self):
        print("La ciudad de la clinica es: ",self.ciudad)
