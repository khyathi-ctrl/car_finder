class Car:
    def __init__(self, make, model, year, fuel, price, km_driven, transmission, owner):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
        self.price = price
        self.km_driven = km_driven
        self.transmission = transmission
        self.owner = owner


class CarFilter:
    def __init__(self, cars):
        self.cars = [Car(**c) for c in cars]

    def filter(self, budget, max_km, brands, fuels, transmissions, owners):
     results = []
     for car in self.cars:
        if (car.price <= budget and
            car.km_driven <= max_km and
            car.make in brands and
            car.fuel in fuels and
            car.transmission in transmissions and
            car.owner in owners):
            results.append(car)
     return results