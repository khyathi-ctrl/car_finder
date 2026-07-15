def show_results(cars):
    if len(cars) == 0:
        print("\nNo cars found matching your requirements.")
        return

    print(f"\n{len(cars)} car(s) found:\n")
    for car in cars:
        print(f"✓ {car.make} {car.model} ({car.year})")
        print(f"  Fuel: {car.fuel}")
        print(f"  Price: ₹{car.price:,}")
        print(f"  KM Driven: {int(car.km_driven):,} km")
        print(f"  Transmission: {car.transmission}")
        print(f"  Owner: {car.owner}")
        print("-" * 30)