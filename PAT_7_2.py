import requests

def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    breweries = response.json()
    return breweries

def get_brewery_count_by_state(state):
    breweries = get_breweries_by_state(state)
    return len(breweries)

def count_brewery_types_by_city(state):
    breweries = get_breweries_by_state(state)
    city_types_count = {}
    for brewery in breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']
        if city in city_types_count:
            if brewery_type in city_types_count[city]:
                city_types_count[city][brewery_type] += 1
            else:
                city_types_count[city][brewery_type] = 1
        else:
            city_types_count[city] = {brewery_type: 1}
    return city_types_count

def count_breweries_with_websites_by_state(state):
    breweries = get_breweries_by_state(state)
    breweries_with_website_count = 0
    for brewery in breweries:
        if brewery['website_url'] is not None:
            breweries_with_website_count += 1
    return breweries_with_website_count

# List names of breweries in Alaska, Maine, and New York
states = ['Alaska', 'Maine', 'New York']
for state in states:
    breweries = get_breweries_by_state(state)
    print(f"\nBreweries in {state}:")
    for brewery in breweries:
        print(brewery['name'])

# Count of breweries in each state
for state in states:
    count = get_brewery_count_by_state(state)
    print(f"\nNumber of breweries in {state}: {count}")

# Count of brewery types by city in each state
for state in states:
    print(f"\nBrewery types by city in {state}:")
    city_types_count = count_brewery_types_by_city(state)
    for city, types_count in city_types_count.items():
        print(f"{city}: {types_count}")

# Count and list how many breweries have websites in each state
for state in states:
    count = count_breweries_with_websites_by_state(state)
    print(f"\nNumber of breweries with websites in {state}: {count}")
