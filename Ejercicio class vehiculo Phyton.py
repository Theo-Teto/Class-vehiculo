# Class-vehiculo
Clase de phyton

class vehicle():
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model
       
class cotxe(vehicle):
    def __init__(self, marca, model, maleter, num_portes):
        super().__init__(marca, model)
        self.maleter = maleter
        self.num_portes = num_portes

    def caracteristiques(self):
        print ("Marca:", self.marca, "Model:", self.model, "Maleter:", self.maleter)

class moto(vehicle):
    def __init__(self, marca, model, tipus):
        super().__init__(marca, model)
        self.tipus = tipus
       
    def caracteristiques(self):
        print ("Marca:", self.marca, "Model:", self.model, "Tipus:", self.tipus)

cotxe1 = cotxe("Seat","Arona","450 l","4 portes")
print (cotxe1.caracteristiques())

moto1 = moto ("Yamaha","Tmax","Maxi scooter")
print (moto1.caracteristiques())
