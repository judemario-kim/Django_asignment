# Generated by Django 4.0.4 on 2022-05-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0015_remove_question_answer_sheet_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_rate',
            field=models.FloatField(default=100.0),
        ),
    ]
