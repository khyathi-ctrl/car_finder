import streamlit as st
from cars import cars
from filter import CarFilter

st.title("🚗 Car Finder")
st.write("Find the perfect car based on your requirements!")
st.divider()

budget = st.number_input("What is your budget? (in rupees)", min_value=100000, max_value=10000000, step=50000, value=1000000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
min_mileage = st.slider("Minimum Mileage (km/l)", min_value=5, max_value=35, value=15)

if st.button("Find Cars"):
    car_filter = CarFilter(cars)
    results = car_filter.filter(budget, fuel, min_mileage)

    if len(results) == 0:
        st.warning("No cars found matching your requirements.")
    else:
        st.success(f"{len(results)} car(s) found!")
        for car in results:
            st.subheader(f"✓ {car.make} {car.model} ({car.year})")
            st.write(f"**Fuel:** {car.fuel}")
            st.write(f"**Price:** ₹{car.price:,}")
            st.write(f"**Mileage:** {car.mileage} km/l")
            st.divider()