from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bpshapi.models import Comment, Product, User
from bpshapi.serializers import CommentSerializer

class CommentView(ViewSet):
    
    def retrieve(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        comments = Comment.objects.all()
        product_id = request.query_params.get('product_id', None)
        
        if product_id is not None:
            comments = comments.filter(product_id=product_id)
            
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        product = Product.objects.get(pk=request.data["product_id"])
        user = User.objects.get(pk=request.data["user_id"])

        comment = Comment(
            product=product,
            user=user,
            content=request.data["content"]
        )
        comment.save()

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)

        comment.content = request.data.get("content", comment.content)
        
        product_id = request.data.get("product_id", comment.product.id)
        comment.product = Product.objects.get(pk=product_id)

        user_id = request.data.get("user_id", comment.user.id)
        comment.user = User.objects.get(pk=user_id)

        comment.save()

        return Response({'message': 'Comment Updated'}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({'message': 'Comment Deleted'}, status=status.HTTP_204_NO_CONTENT)
