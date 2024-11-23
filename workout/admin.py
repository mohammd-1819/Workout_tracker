from django.contrib import admin
from .models.category import Category
from .models.WorkoutPlan import WorkoutPlan, ExerciseSet, Exercise
from .models.session import Session
from .models.Progress import Progress
from .models.review import Review


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'sets')


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'duration')


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_plan')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise')


admin.site.register(Category)
