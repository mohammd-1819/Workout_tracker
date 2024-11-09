from rest_framework import serializers
from .models.WorkoutPlan import Exercise, ExerciseSet, WorkoutPlan
from .models.session import Session
from .models.category import Category
from account.models import User


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('name', 'description', 'category')


class ExerciseSetSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = ExerciseSet
        fields = ('exercise_name', 'sets', 'repetitions')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('date', 'day', 'duration')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class WorkoutPlanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    exercise_sets = ExerciseSetSerializer(many=True, read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ('user', 'name', 'exercise_sets', 'sessions', 'description', 'created_at')
        read_only_fields = ('user', 'created_at')
