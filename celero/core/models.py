from django.db import models


class GenderChoices:
    FEMALE = 'F'
    MALE = 'M'

    @classmethod
    def choices(cls):
        return (
            (cls.FEMALE, 'Female'),
            (cls.MALE, 'Male'),
        )


class MedalChoices:
    BRONZE = 'Bronze'
    SILVER = 'Silver'
    GOLD = 'Gold'
    NA = 'NA'

    @classmethod
    def choices(cls):
        return (
            (cls.BRONZE, 'Bronze'),
            (cls.SILVER, 'Silver'),
            (cls.GOLD, 'Gold'),
            (cls.NA, 'NA'),
        )


class SeasonChoices:
    SUMMER = 'Summer'
    WINTER = 'Winter'

    @classmethod
    def choices(cls):
        return (
            (cls.SUMMER, 'Summer'),
            (cls.WINTER, 'Winter'),
        )


class Region(models.Model):
    region = models.CharField(max_length=255, unique=True)


class NOC(models.Model):
    noc = models.CharField(max_length=3, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    notes = models.CharField(max_length=255, blank=True)


class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Cities'


class Sport(models.Model):
    name = models.CharField(max_length=255)


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices())
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField(help_text="Measurement Unit - centimeters")
    weight = models.PositiveSmallIntegerField(help_text="Measurement Unit - kilograms")
    noc = models.ForeignKey(NOC, on_delete=models.CASCADE)


class Olympics(models.Model):
    season = models.CharField(max_length=6, choices=SeasonChoices.choices())
    year = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Olympics'


class Result(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    olympics = models.ForeignKey(Olympics, on_delete=models.CASCADE)
    sport = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.CharField(max_length=6, choices=MedalChoices.choices())
