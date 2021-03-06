# Generated by Django 2.2.24 on 2021-11-10 12:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mame', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('question', models.CharField(max_length=500)),
                ('a1', models.CharField(max_length=200)),
                ('a2', models.CharField(max_length=200)),
                ('a3', models.CharField(max_length=200)),
                ('a4', models.CharField(max_length=200)),
                ('ctegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 11, 10, 12, 38, 49, 317038, tzinfo=utc))),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.QuizQuestion')),
            ],
        ),
    ]
