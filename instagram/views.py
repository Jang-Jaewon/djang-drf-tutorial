from django.shortcuts import get_object_or_404

from rest_framework            import generics
from rest_framework.viewsets   import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.views      import APIView
from rest_framework.response   import Response

from .serializers import PostSerializer
from .models      import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer     


# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

public_post_list = PostListAPIView.as_view()


class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = self.get_objects(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

public_post_detail = PostDetailAPIView.as_view()        