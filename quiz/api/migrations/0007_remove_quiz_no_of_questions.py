# Generated by Django 5.0.7 on 2024-07-12 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_quiz_no_of_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='no_of_questions',
        ),
    ]
