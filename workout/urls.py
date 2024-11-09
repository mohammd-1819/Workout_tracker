from django.urls import path
from workout.views import WorkoutPlan
from workout.views import exercise

app_name = 'workout'

urlpatterns = [
    path('plan/create', WorkoutPlan.WorkoutPlanCreateView.as_view(), name='plan-create'),
    path('plan/update/<int:pk>', WorkoutPlan.WorkoutPlanUpdateView.as_view(), name='plan-update'),
    path('plan/delete/<int:pk>', WorkoutPlan.WorkoutPlanDeleteView.as_view(), name='plan-delete'),
    path('plan/list', WorkoutPlan.WorkoutPlanListView.as_view(), name='plan-list')

]
