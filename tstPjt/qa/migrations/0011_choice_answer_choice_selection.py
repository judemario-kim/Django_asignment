# Generated by Django 4.0.4 on 2022-05-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0010_rename_answer_choice_votes_remove_choice_selection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='choice',
            name='selection',
            field=models.IntegerField(default=0),
        ),
    ]