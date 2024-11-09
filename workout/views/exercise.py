from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models.WorkoutPlan import Exercise
from workout.serializers import ExerciseSerializer
from workout.utility.pagination import StandardResultSetPagination
from workout.utility.permissions import IsReadOnlyUser


class ExerciseListView(APIView, StandardResultSetPagination):
    permission_classes = (IsReadOnlyUser,)

    def get(self, request):
        exercises = Exercise.objects.all()
        result = self.paginate_queryset(exercises, request)
        serializer = ExerciseSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class ExerciseDetail(APIView):
    permission_classes = (IsReadOnlyUser,)

    def get(self, request, pk):
        exercise = get_object_or_404(Exercise, id=pk)
        serializer = ExerciseSerializer(instance=exercise)
        return Response(serializer.data, status=status.HTTP_200_OK)


