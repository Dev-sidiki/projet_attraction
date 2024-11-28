from django.urls import path
from .views import SearchLocationView,NearbyLocationsView,LocationDetailsView

urlpatterns = [
    path('search/<str:query>/', SearchLocationView.as_view(), name='search_location'),
    path('nearby/<str:lat>/<str:lng>/', NearbyLocationsView.as_view(), name='nearby_locations'),
    path('location/details/<str:location_id>/', LocationDetailsView.as_view(), name='location_details')
]
