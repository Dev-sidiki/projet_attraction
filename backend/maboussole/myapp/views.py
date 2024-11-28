from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .services import search_location , get_nearby_locations , get_location_details 



class SearchLocationView(APIView):
    def get(self, request, query):
        cache_key = f"search_location_{query}"
        cached_data = cache.get(cache_key)

        if cached_data:
            print(f"[CACHE HIT] Data for {query} found in cache."),
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            print(f"[CACHE MISS] Data for {query} not found in cache. Calling API.")  # Log du cache miss


        try:
            # Appel de l'API pour rechercher une location
            data = search_location(query)
            # Stocker les données dans le cache pour 1 heure
            cache.set(cache_key, data, timeout=3600)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({'error': str(e)}, status=e.response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NearbyLocationsView(APIView):
    def get(self, request, lat, lng):
        lat_long = f"{lat},{lng}"
        cache_key = f"nearby_locations_{lat_long}"
        cached_data = cache.get(cache_key)

        if cached_data:
            print(f"[CACHE HIT] Nearby locations for {lat_long} found in cache.")  # Log du cache
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            print(f"[CACHE MISS] Nearby locations for {lat_long} not found in cache. Calling API.")  # Log du cache miss


        try:
            # Appel à l'API pour obtenir les lieux à proximité
            data = get_nearby_locations(lat_long)
            # Stocker les données dans le cache pour 1 heure
            cache.set(cache_key, data, timeout=3600)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({'error': str(e)}, status=e.response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LocationDetailsView(APIView):
    def get(self, request, location_id):
        cache_key = f"location_details_{location_id}"
        cached_data = cache.get(cache_key)

        if cached_data:
            print(f"[CACHE HIT] Location details for {location_id} found in cache.")
            return Response(cached_data, status=status.HTTP_200_OK)
        
        print(f"[CACHE MISS] Fetching location details for {location_id} from API.")

        try:
            # Appel à l'API pour récupérer les détails d'une location
            data = get_location_details(location_id)
            if not data:
                return Response({'error': 'Données non trouvées pour cette location'}, status=status.HTTP_404_NOT_FOUND)
            cache.set(cache_key, data, timeout=3600)  # Stockage dans le cache pour 1 heure
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({'error': str(e)}, status=e.response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)