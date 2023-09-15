# Generated by Django 4.2.4 on 2023-09-06 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FeedbackApp', '0004_alter_feedback_student_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='trainer_name',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Trainers'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
