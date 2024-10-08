# Generated by Django 5.0.7 on 2024-09-02 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_quiz_no_of_questions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
