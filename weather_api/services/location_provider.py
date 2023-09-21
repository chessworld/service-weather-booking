from ..models import Location

class LocationProvider:
    
    def search_locations(self, query: str):
        pass


    def create_location(self, **kwargs):
        try:
            return Location.get(**kwargs)
        except Location.DoesNotExist:
            return Location.objects.create(**kwargs)