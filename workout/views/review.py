from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models.review import Review
from workout.serializers.review_serializer import ReviewSerializer
from workout.utility.pagination import StandardResultSetPagination
from workout.utility.permissions import IsReadOnlyUser


class ReviewListView(APIView, StandardResultSetPagination):
    permission_classes = (IsAuthenticated, IsReadOnlyUser)

    def get(self, request):
        reviews = Review.objects.all()
        result = self.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class ReviewDetailView(APIView):
    permission_classes = (IsAuthenticated, IsReadOnlyUser)

    def get(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        serializer = ReviewSerializer(instance=review)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewDeleteView(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    def delete(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        review.delete()
        return Response({'message': 'review removed'})
