# Generated by Django 4.0.4 on 2022-05-29 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0016_question_correct_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='selection',
        ),
    ]
