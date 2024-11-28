import requests
from django.conf import settings

API_KEY = settings.TRIPADVISOR_API_KEY 


def get_nearby_locations(lat_long):
    url = "https://api.content.tripadvisor.com/api/v1/location/nearby_search"
    params = {
        "latLong": lat_long,
        "key": API_KEY,
        "language": "fr"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def search_location(query):
    url = "https://api.content.tripadvisor.com/api/v1/location/search"
    params = {
        "key": API_KEY,
        "searchQuery": query,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_location_details(location_id):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details"
    params = {
        "key": API_KEY,
        "language": "fr",
        "currency": "EUR"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        raise
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        raise
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        raise
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
        raise