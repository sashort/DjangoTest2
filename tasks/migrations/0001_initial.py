# Generated by Django 4.0.3 on 2022-03-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('user_pk', models.IntegerField()),
                ('index', models.IntegerField()),
                ('description', models.CharField(max_length = 500)),
                ('complete', models.BooleanField()),
            ],
        ),
    ]