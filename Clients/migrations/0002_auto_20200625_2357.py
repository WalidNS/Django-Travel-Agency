# Generated by Django 3.0.7 on 2020-06-25 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure', models.CharField(max_length=20)),
                ('Arrival', models.CharField(max_length=20)),
                ('FlightDate', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Flight')),
                ('clients', models.ManyToManyField(to='Clients.Client')),
            ],
        ),
    ]
