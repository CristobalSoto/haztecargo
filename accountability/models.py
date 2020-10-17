from django.db import models

# Create your models here.
class Deputy(models.Model):
    POLITICAL_PARTIES = [
        ('Independiente', 'Independiente'),
        ('Union Demócrata Independiente', 'unión democrata independiente'),
        ('Renovación Nacional', 'Renovación nacional'),
        ('Partido Socialista de Chile', 'PS'),
        ('Partido por la Democracia', 'PPD'),
        ('Partido Demócrata Cristiano', 'DC'),
        ('Revolución Democrática', 'RD'),
        ('Evolución Política', 'Evópoli'),
        ('Partido Progresista de Chile', 'PRO'),
        ('Partido Comunista de Chile', 'PC'),
        ('Partido Radical de Chile', 'PR'),
        ('Convergencia Social', 'CS'),
        ('Federación Regionalista Verde Social', 'FREVS'),
        ('Partido Humanista', 'PH'),
        ('Partido Liberal de Chile', 'Partido Liberal'),
        ('Comunes', 'Comunes'),
        ('Partido Ecologista Verde', 'PEV'),
        ('Partido Republicano de Chile', 'Partido Republicano'),
        
    ]
    name = models.CharField(max_length=100)
    politic_party = models.CharField(max_length=50, choices=POLITICAL_PARTIES)
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class District(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Commune(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'