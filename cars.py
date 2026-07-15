import pandas as pd

def clean_price(price):
    try:
        price = str(price)
        price = price.replace("₹", "").replace(",", "").strip()
        return int(float(price))
    except:
        return None

def clean_km(km):
    try:
        km = str(km)
        km = km.replace(",", "").replace("km", "").strip()
        return int(float(km))
    except:
        return None

def load_cars():
    df1 = pd.read_csv("used_car_dataset.csv")
    df2 = pd.read_csv("used_cars_dataset_v2.csv")

    df = pd.concat([df1, df2], ignore_index=True)
    df = df.drop_duplicates()

    df = df.rename(columns={
        "Brand": "make",
        "model": "model",
        "Year": "year",
        "FuelType": "fuel",
        "AskPrice": "price",
        "kmDriven": "km_driven",
        "Transmission": "transmission",
        "Owner": "owner"
    })

    df["price"] = df["price"].apply(clean_price)
    df["km_driven"] = df["km_driven"].apply(clean_km)

    df = df[["make", "model", "year", "fuel", "price", "km_driven", "transmission", "owner"]]
    df = df.dropna()

    df = df[df["price"] > 0]
    df = df[df["km_driven"] > 0]

    return df.to_dict(orient="records")

cars = load_cars()