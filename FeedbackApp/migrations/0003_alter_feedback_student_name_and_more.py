# Generated by Django 4.2.4 on 2023-09-01 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FeedbackApp', '0002_rename_couse_name_feedback_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='student_name',
            field=models.ForeignKey(limit_choices_to={'groups_name': 'Students'}, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='trainer_name',
            field=models.ForeignKey(limit_choices_to={'groups_name': 'Trainers'}, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL),
        ),
    ]