import requests

class CountryData:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        # Fetch data from the provided URL
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the URL.")
            return []

    def display_country_info(self, data):
        # Iterate through each country's data
        for country in data:
            print(f"Country Name: {country.get('name', 'N/A')}")

            # Check if 'currencies' key exists
            if 'currencies' in country:
                currencies_info = []
                for currency_code, currency_data in country['currencies'].items():
                    currency_symbol = currency_data.get('symbol', 'N/A')
                    currencies_info.append(f"{currency_code} ({currency_symbol})")
                print(f"Currencies: {', '.join(currencies_info)}")
            else:
                print("Currencies: N/A (No data available)")

    def display_countries_with_dollar_currency(self, data):
        # Method to display countries with 'DOLLAR' as their currency
        pass

    def display_countries_with_euro_currency(self, data):
        # Method to display countries with 'EURO' as their currency
        pass

# Example usage:
# Instantiate CountryData class with the URL
country_data = CountryData("https://restcountries.com/v3.1/all")
# Fetch data
data = country_data.fetch_data()
# Display country information
country_data.display_country_info(data)

