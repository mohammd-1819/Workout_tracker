# Generated by Django 5.1.2 on 2024-11-06 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='workout_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_sets', to='workout.workoutplan'),
        ),
    ]
