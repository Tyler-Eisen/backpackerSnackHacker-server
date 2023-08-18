from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bpshapi.models import Shop, City, UserFavorite
from bpshapi.serializers import ShopSerializer
from rest_framework.decorators import action

class ShopView(ViewSet):
    
    def retrieve(self, request, pk=None):
        """Retrieve a specific shop using its primary key."""
        try:
            shop = Shop.objects.get(pk=pk)
            serializer = ShopSerializer(shop)
            return Response(serializer.data)
        except Shop.DoesNotExist:
            return Response({'message': 'Shop not found.'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """List all shops or filter by city_id."""
        shops = Shop.objects.all()
        city_id = request.query_params.get('city_id', None)
        
        if city_id is not None:
            shops = shops.filter(city_id=city_id)
            
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    
    def create(self, request):
      city = City.objects.get(pk=request.data["city_id"])

      shop = Shop(
          city_id=city,
          name=request.data["name"],
          address=request.data["address"],
          image_url=request.data["image_url"]
      )
      shop.save()

      serializer = ShopSerializer(shop)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
      shop = Shop.objects.get(pk=pk)

      city_id = request.data.get("city_id", shop.city_id.id)  
      city = City.objects.get(pk=city_id)

      shop.name = request.data.get("name", shop.name)  
      shop.address = request.data.get("address", shop.address)
      shop.image_url = request.data.get("image_url", shop.image_url)
      shop.city_id = city

      shop.save()

      return Response({'message': 'Shop Updated'}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        shop = Shop.objects.get(pk=pk)
        shop.delete()
        return Response({'message': 'Shop Destroyed'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        """Favorite a shop."""
        shop = Shop.objects.get(pk=pk)
        user = request.user  # Assuming you have authentication set up


        favoritedShop = UserFavorite.objects.create(shop=shop, user=user)
        return Response({'message': 'Shop favorited successfully!'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'])
    def unfavorite(self, request, pk=None):
        """Unfavorite a shop."""
        shop = Shop.objects.get(pk=pk)
        user = request.user

        favorite = UserFavorite.objects.filter(shop=shop, user_id=user).first()

        if not favorite:
            return Response({'message': 'Shop not in favorites.'}, status=status.HTTP_404_NOT_FOUND)

        favorite.delete()
        return Response({'message': 'Shop unfavorited successfully!'}, status=status.HTTP_204_NO_CONTENT)
