from django.db import models
from account.models import User
from workout.models.WorkoutPlan import Exercise


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
