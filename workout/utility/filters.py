import django_filters
from workout.models.WorkoutPlan import WorkoutPlan, Exercise


class ExerciseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Exercise
        fields = ['name', 'category']


class WorkoutPlanFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    user = django_filters.CharFilter(field_name='user__username',
                                     lookup_expr='icontains')

    class Meta:
        model = WorkoutPlan
        fields = ['name', 'user']
