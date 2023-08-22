from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bpshapi.models import Shop, User, Product
from bpshapi.serializers import ProductSerializer

class ProductView(ViewSet):
    
    def retrieve(self, request, pk=None):
        """Retrieve a specific shop using its primary key."""
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """List all shops or filter by city_id."""
        products = Product.objects.all()
        shop = request.query_params.get('shop_id', None)
        user = request.query_params.get('user_id')
        
        if shop is not None:
            products = products.filter(shop = shop )
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
      shop = Shop.objects.get(pk=request.data["shop"])
      user = User.objects.get(pk=request.data["userId"])

      product = Product(
          shop=shop,
          user=user,
          name=request.data["name"],
          price=request.data["price"],
          image_url=request.data["image_url"]
      )
      product.save()

      serializer = ProductSerializer(product)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
      product = Product.objects.get(pk=pk)

      shop_id = request.data.get("shop_id", product.shop.id)
      shop = Shop.objects.get(pk=shop_id)

      user_id = request.data.get("user_id", product.user.id)
      user = User.objects.get(pk=user_id)

      product.name = request.data.get("name", product.name)
      product.price = request.data.get("price", product.price)
      product.image_url = request.data.get("image_url", product.image_url)
      product.shop = shop
      product.user = user

      product.save()
      serializer = ProductSerializer(product)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'message': 'Product Destroyed'}, status=status.HTTP_204_NO_CONTENT)
