# Generated by Django 2.0.6 on 2018-06-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trinkets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('year', models.DateField()),
                ('picture', models.CharField(max_length=30)),
            ],
        ),
    ]
