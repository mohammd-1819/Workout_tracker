from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models.Progress import Progress
from workout.serializers.progress_serializer import ProgressSerializer
from workout.utility.pagination import StandardResultSetPagination
from workout.utility.permissions import IsProgressOwner, IsReadOnlyUser


class ProgressListView(APIView, StandardResultSetPagination):
    permission_classes = (IsAuthenticated, IsProgressOwner)

    def get(self, request):
        progresses = Progress.objects.filter(user=request.user)
        result = self.paginate_queryset(progresses, request)
        serializer = ProgressSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class ProgressDetailView(APIView):
    permission_classes = (IsAuthenticated, IsProgressOwner)

    def get(self, request, pk):
        progress = get_object_or_404(Progress, id=pk, user=request.user)
        serializer = ProgressSerializer(instance=progress)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProgressUpdateView(APIView):
    permission_classes = (IsAuthenticated, IsProgressOwner)

    def put(self, request, pk):
        progress = get_object_or_404(Progress, id=pk, user=request.user)
        serializer = ProgressSerializer(instance=progress, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgressDeleteView(APIView):
    permission_classes = (IsAuthenticated, IsProgressOwner)

    def delete(self, request, pk):
        progress = get_object_or_404(Progress, id=pk, user=request.user)
        progress.delete()
        return Response({'message': 'progress removed'})


