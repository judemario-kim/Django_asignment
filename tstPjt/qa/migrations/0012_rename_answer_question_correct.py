# Generated by Django 4.0.4 on 2022-05-28 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0011_choice_answer_choice_selection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='correct',
        ),
    ]
