import requests
import pandas as pd

URL = "https://api.energidataservice.dk/dataset/CO2Emis?limit=5"

# URL do site com o dataset https://www.energidataservice.dk/tso-electricity/CO2Emis#metadata-info


# getting data from API
try:
    response = requests.get(URL, timeout=(3.05, 10))
    response.raise_for_status()

    result = response.json()

    # Display JSON primary keys
    print("Data:")
    for key, value in result.items():
        print(f"{key}: {type(value)}")

    # Extract specific records
    records = result.get("records", [])
    print("\nRecords found:")

    for i, record in enumerate(records, start=1):
        print(f" {i}. {record}")

except requests.exceptions.Timeout:
    print("The request has expired. Try again later.")
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")


# Data cleaning: I will exclude the "Minutes5DK" from the ingestion, because I only want UTC time zone

df = pd.DataFrame(data=records)

df = df.drop(columns="Minutes5DK")
print(df)
