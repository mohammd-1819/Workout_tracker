from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models.WorkoutPlan import WorkoutPlan
from workout.serializers import WorkoutPlanSerializer
from workout.utility.permissions import IsWorkoutPlanOwner
from workout.utility.pagination import StandardResultSetPagination


class WorkoutPlanCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutPlanUpdateView(APIView):
    permission_classes = (IsWorkoutPlanOwner, IsAuthenticated)

    def put(self, request, pk):
        workout_plan = get_object_or_404(WorkoutPlan, id=pk, user=request.user)
        serializer = WorkoutPlanSerializer(instance=workout_plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutPlanDeleteView(APIView):
    permission_classes = (IsWorkoutPlanOwner, IsAuthenticated)

    def delete(self, request, pk):
        workout_plan = get_object_or_404(WorkoutPlan, id=pk, user=request.user)
        workout_plan.delete()
        return Response({'message': 'Plan Deleted'}, status=status.HTTP_204_NO_CONTENT)


class WorkoutPlanListView(APIView, StandardResultSetPagination):
    permission_classes = (IsWorkoutPlanOwner, IsAuthenticated)

    def get(self, request):
        workout_plans = WorkoutPlan.objects.filter(user=request.user)
        result = self.paginate_queryset(workout_plans, request)
        serializer = WorkoutPlanSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
