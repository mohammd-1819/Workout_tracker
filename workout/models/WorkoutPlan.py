from django.db import models
from account.models import User
from .category import Category
from .session import Session


class Exercise(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='exercises')

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workoutplans')
    name = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Exercise, through='ExerciseSet', related_name='workoutplans')
    sessions = models.ManyToManyField(Session, related_name='workoutplans', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise_sets')
    workout_plan = models.ForeignKey('WorkoutPlan', on_delete=models.CASCADE, related_name='exercise_sets', blank=True,
                                     null=True)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sets} sets of {self.repetitions} reps for {self.exercise.name}"
