# Generated by Django 3.2.10 on 2022-01-04 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_owner',
            fields=[
                ('NID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Sex', models.CharField(max_length=1)),
                ('BirthDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('MobilePhone', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NationalID', models.CharField(max_length=10)),
                ('CarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'unique_together': {('NationalID', 'CarID')},
            },
        ),
    ]
