import streamlit as st
from cars import cars
from filter import CarFilter

# get unique values from real dataset
all_brands = sorted(set(car["make"] for car in cars))
all_fuels = sorted(set(car["fuel"] for car in cars))
all_transmissions = sorted(set(car["transmission"] for car in cars))
all_owners = sorted(set(car["owner"] for car in cars))

st.title("🚗 Car Finder India")
st.write("Find your perfect used car from 13,000+ real listings!")
st.divider()

# filters
budget = st.number_input("Maximum Budget (₹)", min_value=50000, max_value=10000000, step=50000, value=500000)
max_km = st.slider("Maximum KM Driven", min_value=5000, max_value=500000, step=5000, value=100000)

selected_brands = st.multiselect("Car Brand (choose one or more)", all_brands)
selected_fuels = st.multiselect("Fuel Type (choose one or more)", all_fuels)
selected_transmissions = st.multiselect("Transmission (choose one or more)", all_transmissions)
selected_owners = st.multiselect("Owner Type (choose one or more)", all_owners)

if st.button("Find Cars"):
    car_filter = CarFilter(cars)

    # if user didn't select anything, treat it as "all options"
    fuels = selected_fuels if selected_fuels else all_fuels
    brands = selected_brands if selected_brands else all_brands
    transmissions = selected_transmissions if selected_transmissions else all_transmissions
    owners = selected_owners if selected_owners else all_owners

    results = car_filter.filter(budget, max_km, brands, fuels, transmissions, owners)

    if len(results) == 0:
        st.warning("No cars found. Try adjusting your filters.")
    else:
        st.success(f"{len(results)} car(s) found!")
        for car in results:
            st.subheader(f"✓ {car.make} {car.model} ({car.year})")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Fuel:** {car.fuel}")
                st.write(f"**Price:** ₹{car.price:,}")
            with col2:
                st.write(f"**KM Driven:** {int(car.km_driven):,} km")
                st.write(f"**Transmission:** {car.transmission}")
                st.write(f"**Owner:** {car.owner}")
            st.divider()