# Generated by Django 4.0.4 on 2022-05-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]