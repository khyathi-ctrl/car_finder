from cars import cars
from filter import CarFilter
from display import show_results

def get_user_requirements():
    print("\nWelcome to Car Finder!")
    print("-" * 30)
    
    budget = int(input("What is your budget? (in rupees): "))
    fuel = input("Fuel type? (Petrol/Diesel/Electric): ")
    min_mileage = int(input("Minimum mileage you want (km/l): "))
    
    return budget, fuel, min_mileage

def save_results(cars):
    choice = input("\nSave results to file? (yes/no): ")
    if choice.lower() == "yes":
        with open("saved_cars.txt", "a", encoding="utf-8") as file:
            for car in cars:
                file.write(f"{car.make} {car.model} ({car.year}) - ₹{car.price:,} - {car.fuel} - {car.mileage} km/l\n")
        print("Saved to saved_cars.txt!")

def main():
    budget, fuel, min_mileage = get_user_requirements()
    
    car_filter = CarFilter(cars)
    results = car_filter.filter(budget, fuel, min_mileage)
    
    show_results(results)
    
    if len(results) > 0:
        save_results(results)

main()