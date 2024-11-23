from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models.category import Category
from workout.serializers.exercise_serializer import CategorySerializer
from workout.utility.pagination import StandardResultSetPagination
from workout.utility.permissions import IsReadOnlyUser


class CategoryListView(APIView, StandardResultSetPagination):
    permission_classes = (IsReadOnlyUser,)

    def get(self, request):
        categories = Category.objects.all()
        result = self.paginate_queryset(categories, request)
        serializer = CategorySerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryCreateView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteView(APIView):

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response({"message": "category deleted"}, status=status.HTTP_204_NO_CONTENT)


