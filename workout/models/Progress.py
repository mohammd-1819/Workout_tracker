from django.db import models
from account.models import User
from .WorkoutPlan import WorkoutPlan, Exercise


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='progress', blank=True,
                                     null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField(auto_now_add=True)
    sets_completed = models.PositiveIntegerField()
    repetition_per_set = models.PositiveIntegerField()
    weight_used = models.FloatField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'progress'
        verbose_name_plural = 'progresses'

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.date}"
