from rest_framework import serializers
from workout.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'exercise', 'text')
        read_only_fields = ('created_at',)
