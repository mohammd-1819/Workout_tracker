from rest_framework import serializers
from workout.models.WorkoutPlan import Exercise, ExerciseSet
from workout.models.session import Session
from workout.models.category import Category


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
