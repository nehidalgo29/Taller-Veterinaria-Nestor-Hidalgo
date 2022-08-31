class Veterinario:
    idVeterinario=0
    especialidad=""
    sede=""
    ciudad=""
    cargo=""

    def __init__(self,idVeterinario,especialidad,sede,ciudad,cargo):
        self.idVeterinario=idVeterinario
        self.especialidad=especialidad
        self.sede=sede
        self.ciudad=ciudad
        self.cargo=cargo

    def darIdVeterinario (self):
        print("El Id del medico veterinario es: ",self.idVeterinario)

    def darEspecialidad (self):
        print("La especialidad del medico veterinario es: ",self.especialidad)

    def darSede(self):
        print("La sede donde trabaja el medico veterinario es: ",self.sede)

    