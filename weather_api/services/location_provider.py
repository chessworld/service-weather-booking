from ..models import Location

class LocationProvider:

    def search_locations(self, query: str):
        pass


    def get_location(self, **kwargs):
        return Location.objects.get_or_create(**kwargs)
