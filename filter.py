class Car:
    def __init__(self, make, model, year, fuel, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
        self.price = price
        self.mileage = mileage


class CarFilter:
    def __init__(self, cars):
        self.cars = [Car(**c) for c in cars]

    def filter(self, budget, fuel, min_mileage):
        results = []
        for car in self.cars:
            if car.price <= budget and car.fuel.lower() == fuel.lower() and car.mileage >= min_mileage:
                results.append(car)
        return results