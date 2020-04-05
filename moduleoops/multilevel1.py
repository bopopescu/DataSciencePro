class Vehicle:

    def speed(self,km,hr):
        self.km=km
        self.hr=hr
        print(" Speed is : ",(km/hr))

    def colour(self,colour):
        self.colour=colour
        print("Colour is :",colour)


class Car(Vehicle):
    def speed(self,km,hr):
        super().speed(15,2)
        self.km = km
        self.hr=hr
        print(" Speed is : ",(km/hr))


class Maruti(Car):
    def speed(self,km,hr):
        super().speed(6,3)
        self.km=km
        self.hr=hr
        print(" Speed is : ",(km/hr))


x = Maruti()
x.speed(12,2)
x.colour("Red")