from rest_framework import serializers
from workout.models.WorkoutPlan import WorkoutPlan
from account.models import User
from workout.serializers.exercise_serializer import ExerciseSetSerializer, SessionSerializer


class WorkoutPlanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    exercise_sets = ExerciseSetSerializer(many=True, read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ('user', 'name', 'exercise_sets', 'sessions', 'description', 'created_at')
        read_only_fields = ('user', 'created_at')
