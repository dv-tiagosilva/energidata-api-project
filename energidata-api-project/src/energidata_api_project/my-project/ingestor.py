import requests
import pandas as pd


# getting data from API
def get_filtered_data():
    URL = "https://api.energidataservice.dk/dataset/CO2Emis?limit=5"
    
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
        
        # Data cleaning: I will exclude the "Minutes5DK" from the ingestion, because I only want UTC time zone
        data_filtered = []
        for record in records:
            filtered = {
                "MinutesUTC": record["Minutes5UTC"],
                "Price_area": record["PriceArea"],
                "CO2_emission": record["CO2Emission"]
            }
            data_filtered.append(filtered)

        return data_filtered
        

    except requests.exceptions.Timeout:
        print("The request has expired. Try again later.")
        return []
        
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []

