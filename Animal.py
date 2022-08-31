class Animal:
    numeroCliente=""
    nombreAnimal=""
    tipoAnimal=""
    raza=""
    idAnimal=0

    def __init__(self,numeroCliente,nombreAnimal,tipoAnimal,raza,idAnimal):
        self.numeroCliente=numeroCliente
        self.nombreAnimal=nombreAnimal
        self.tipoAnimal=tipoAnimal
        self.raza=raza
        self.idAnimal=idAnimal

    def darNumeroCliente(self):
        print("El numero  del cliente dueño de la mascota es: ",self.numeroCliente)

    def darNombreAnimal(self):
        print("El nombre del animal es: ",self.nombreAnimal)

    def darTipoAnimal(self):
        print("El tipo del animal es: ",self.tipoAnimal)