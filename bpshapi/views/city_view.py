from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bpshapi.models import City
from bpshapi.serializers import CitySerializer

class CityView(ViewSet):
    def retrieve(self, request, pk):
        # Retrieve the Order instance
        city = City.objects.get(pk=pk)

        # Serialize the Order instance
        serializer = CitySerializer(city)
        data = serializer.data

        return Response(data)
      
    def list(self,request):
         
         cities = City.objects.all()
         city = request.query_params.get('city', None)
         if city is not None:
             cities = cities.filter(city_id = city)
                  
         serializer = CitySerializer(cities, many=True)
         return Response(serializer.data)
       
    def create(self, request):
        """POST request to create a rare user"""
        serializer = CitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
      
    def update(self, request, pk):
      """PUT request to update a city"""
      city = City.objects.get(pk=pk)
      
      # Fields from your ERD for City
      name = request.data.get("name", city.name)
      image_url = request.data.get("imageUrl", city.image_url)

      # Set updated values to the city instance
      city.name = name
      city.image_url = image_url

      # Save the updated city instance
      city.save()

      return Response({'message': 'City Updated'}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        city = City.objects.get(pk=pk)
        city.delete()
        return Response({'message': 'User Destroyed'}, status=status.HTTP_204_NO_CONTENT)
