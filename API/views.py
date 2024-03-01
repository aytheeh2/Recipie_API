from django.shortcuts import render
from Recipie.models import Recipie, Review_or_Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import RecipieSerializer, Review_or_Comment_Serializer, UserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny


class recipie_ListCreate(generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer


class recipie_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer
    lookup_field = 'pk'


class Review_or_Comment_view(generics.ListCreateAPIView):

    # if reviews are to be filtered by user who wrote review. since all reviews should be public , commenting out below.
    # def get_queryset(self):
    #     user = self.request.user
    #     return Review_or_Comment.objects.filter(user=user)

    queryset = Review_or_Comment.objects.all()
    serializer_class = Review_or_Comment_Serializer
    permission_classes = [IsAuthenticated]
from rest_framework.exceptions import PermissionDenied

class Review_or_Comment_view_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    # def get_queryset(self):
    #     user = self.request.user
    #     return Review_or_Comment.objects.filter(user=user)

    # def perform_update(self, serializer):
    #     review_object = self.get_object()
    #     if review_object.user.id == self.request.user.id:
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)

    # def perform_destroy(self, instance):
    #     if self.request.user.id == instance.user.id:
    #         instance.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)

    def perform_update(self, serializer):
        review_object = self.get_object()
        if review_object.user != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        instance.delete()

    queryset = Review_or_Comment.objects.all()
    serializer_class = Review_or_Comment_Serializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def search_recipies(request, q):
    if len(q) > 0:
        results = Recipie.objects.filter(name__icontains=q)
        if results:
            sr_results = RecipieSerializer(results, many=True)
            return Response(data=sr_results.data, status=status.HTTP_200_OK)
    else:
        pass
    return Response(status=status.HTTP_404_NOT_FOUND)
