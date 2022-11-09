# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric
# cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume
# of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of
# electric cars receives the registration number, maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car
# (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values
# of their kilometer counters.


class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0,travelled_distance=0):

        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance


    def accerelate(self,speed):
            self.current_speed=self.current_speed + speed

    def drive(self,hours=1):
            self.travelled_distance = self.travelled_distance + self.current_speed * hours


class race:
    def __init__(self,name,distance,car_list):
        self.name=name
        self.distance=distance
        self.car_list=car_list

    def hour_passes(self):
        for car_race in self.car_list:
            car_race.current_speed=random.randrange(-10,15)
            car_race.drive(1)

    def print_status(self):
        for car_race in self.car_list:
            print(f"name race is: {car_race.name},registration_number :{car_race.registration_number}, car speed is: {car_race.current_speed}"
                  f"travel distance is: {car_race.travelled_distance}")

    def race_finished(self):
        win_distance=0
        for car_race in self.car_list:
            win_distance=max(win_distance,car_race.travelled_distance)
            if win_distance>=self.distance:

                return  True


class electricCar(car):
    def __init__(self,registration_number,maximum_speed,battery_capacity,current_speed=0,travelled_distance=0):
        self.battery_capacity=battery_capacity
        super().__init__(registration_number,maximum_speed,current_speed=0,travelled_distance=0)


class gasolineCar(car):
    def __init__(self,registration_number,maximum_speed,tanker,current_speed=0,travelled_distance=0):
        self.tanker=tanker
        super().__init__(registration_number,maximum_speed,current_speed=0,travelled_distance=0)






import random
car_list=[]
#register_num_list=['ABC-1','ABC-2','ABC-3','ABC-4','ABC-5','ABC-6','ABC-7','ABC-8','ABC-9','ABC-10']

car_list.append(electricCar("ABC-15",180,52.5))
car_list.append(gasolineCar("ACD-123",165,32.3))
for i in car_list:
    i.accerelate(random.randrange(30,60))
    i.drive(3)
    print(f"car :{i.registration_number} distance travelled:{i.travelled_distance}")









