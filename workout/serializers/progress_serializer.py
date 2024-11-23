from rest_framework import serializers
from workout.models.Progress import Progress


class ProgressSerializer(serializers.ModelSerializer):
    exercise_name = serializers.ReadOnlyField(source='exercise.name')
    workout_plan_name = serializers.ReadOnlyField(source='workout_plan.name')

    class Meta:
        model = Progress
        fields = [
            'id',
            'user',
            'workout_plan',
            'workout_plan_name',
            'exercise',
            'exercise_name',
            'date',
            'sets_completed',
            'repetition_per_set',
            'weight_used',
            'duration'
        ]
        read_only_fields = ['user', 'date']
