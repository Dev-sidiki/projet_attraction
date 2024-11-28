from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import search_location , get_nearby_locations , get_location_details 

class SearchLocationView(APIView):
    def get(self, request, query):
        try:
            data = search_location(query)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({'error': str(e)}, status=e.response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NearbyLocationsView(APIView):
    def get(self, request, lat, lng):
        try:
            lat_long = f"{lat},{lng}"
            data = get_nearby_locations(lat_long)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({'error': str(e)}, status=e.response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LocationDetailsView(APIView):
    def get(self, request, location_id):
        try:
            data = get_location_details(location_id)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)