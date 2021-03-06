# Generated by Django 3.1.2 on 2020-10-15 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deputy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('politic_party', models.CharField(choices=[('Independiente', 'Independiente'), ('Union Demócrata Independiente', 'unión democrata independiente'), ('Renovación Nacional', 'Renovación nacional'), ('Partido Socialista de Chile', 'PS'), ('Partido por la Democracia', 'PPD'), ('Partido Demócrata Cristiano', 'DC'), ('Revolución Democrática', 'RD'), ('Evolución Política', 'Evópoli'), ('Partido Progresista de Chile', 'PRO'), ('Partido Comunista de Chile', 'PC'), ('Partido Radical de Chile', 'PR'), ('Convergencia Social', 'CS'), ('Federación Regionalista Verde Social', 'FREVS'), ('Partido Humanista', 'PH'), ('Partido Liberal de Chile', 'Partido Liberal'), ('Comunes', 'Comunes'), ('Partido Ecologista Verde', 'PEV'), ('Partido Republicano de Chile', 'Partido Republicano')], max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountability.district')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountability.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountability.region')),
            ],
        ),
    ]
