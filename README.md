# CO2 Emission Data Pipeline

This project is a simple pipeline for ingesting CO2 emission data from a Denmark public API, with data storage in a PostgreSQL database.

## 📦 Structure

- `ingestor.py` – Collects data from the API and filters relevant fields.
- `db.py` – Connects to the database and inserts data into PostgreSQL.
- `README.md` – Project documentation.

## 🌐 Data Source

- **API**: [CO2Emis - Energi Data Service](https://api.energidataservice.dk/dataset/CO2Emis?limit=5)
- **NOTE**: `In this example I have used only the first 5 results from the API, because it is a leraning project, but inside the API-URL, I could change that limiting query, in the "?limit=5" space in the final of the API-URL`
- **Fields used**:
  - `Minutes5UTC` → `minutes_utc`
  - `PriceArea` → `price_area`
  - `CO2Emission` → `co2_emission`

## 🗃️ Database

- **System**: PostgreSQL
- **Table**: `co2_emissions`
- **Schema**:

| Column        | Type      | Description                |
|--------------|-----------|--------------------------|
| minutes_utc     | timestamp | Emission UTC timestamp   |
| price_area      | text      | Bidding zone from Denmark (DK1-west Great Belt and DK2-east of the Great Belt)|
| co2_emission | real   | CO₂ emission (g/kWh)     |
