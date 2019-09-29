from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Museum

latitude = 43.676899
longitude = -79.407158

user_location = Point(longitude, latitude, srid=4326)

# Create your views here.
class Home(generic.ListView):
    model = Museum
    context_object_name = "museums"
    queryset = Museum.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "museums/index.html"
