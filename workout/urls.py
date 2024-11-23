from django.urls import path
from workout.views import WorkoutPlan
from workout.views import exercise
from workout.views import progress
from workout.views import review

app_name = 'workout'

urlpatterns = [
    path('plan/create', WorkoutPlan.WorkoutPlanCreateView.as_view(), name='plan-create'),
    path('plan/update/<int:pk>', WorkoutPlan.WorkoutPlanUpdateView.as_view(), name='plan-update'),
    path('plan/delete/<int:pk>', WorkoutPlan.WorkoutPlanDeleteView.as_view(), name='plan-delete'),
    path('plan/list', WorkoutPlan.WorkoutPlanListView.as_view(), name='plan-list'),
    path('plan/detail/<int:pk>', WorkoutPlan.WorkoutPlanDetailView.as_view(), name='plan-detail'),

    path('progress/list', progress.ProgressListView.as_view(), name='progress-list'),
    path('progress/detail/<int:pk>', progress.ProgressDetailView.as_view(), name='progress-detail'),
    path('progress/update/<int:pk>', progress.ProgressUpdateView.as_view(), name='progress-update'),
    path('progress/delete/<int:pk>', progress.ProgressDeleteView.as_view(), name='progress-delete'),

    path('exercise/list', exercise.ExerciseListView.as_view(), name='exercise-list'),
    path('exercise/detail', exercise.ExerciseDetailView.as_view(), name='exercise-detail'),

    path('review/list', review.ReviewListView.as_view(), name='review-list'),
    path('review/detail/<int:pk>', review.ReviewDetailView.as_view(), name='review-detail'),
    path('review/delete/<int:pk>', review.ReviewDeleteView.as_view(), name='review-delete'),


]
