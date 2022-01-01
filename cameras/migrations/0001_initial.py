# Generated by Django 3.2.10 on 2022-01-01 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CID', models.IntegerField(default=0, unique=True)),
                ('Status', models.BooleanField(default=0)),
                ('OperationType', models.CharField(default='No OperationType', max_length=10)),
                ('Model', models.IntegerField(default=0)),
                ('ManCountry', models.CharField(default='No ManCountry', max_length=20)),
                ('Range', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Moving_camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plate', models.CharField(max_length=8)),
                ('CameraID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.camera', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fixed_camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=500)),
                ('CameraID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.camera', unique=True)),
            ],
        ),
    ]
