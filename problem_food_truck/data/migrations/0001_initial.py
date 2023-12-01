# Generated by Django 3.2.23 on 2023-11-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationId', models.IntegerField()),
                ('applicant', models.CharField(max_length=100)),
                ('facilityType', models.CharField(max_length=100)),
                ('cnn', models.IntegerField()),
                ('locationDescription', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('blocklot', models.IntegerField()),
                ('block', models.IntegerField()),
                ('lot', models.IntegerField()),
                ('permit', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('foodItems', models.CharField(max_length=100)),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('schedule', models.URLField(max_length=100)),
                ('dayshours', models.CharField(max_length=100)),
                ('NOISent', models.CharField(max_length=10)),
                ('approved', models.DateTimeField()),
                ('received', models.IntegerField()),
                ('priorPermit', models.BooleanField()),
                ('expirationDate', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('firePreventionDistricts', models.IntegerField()),
                ('policeDistricts', models.IntegerField()),
                ('supervisorDistricts', models.IntegerField()),
                ('zipCodes', models.IntegerField()),
                ('neighborhoodsOld', models.IntegerField()),
            ],
        ),
    ]
