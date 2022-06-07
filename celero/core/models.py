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

    def __str__(self):
        return f'{self.region}'


class NOC(models.Model):
    noc = models.CharField(max_length=3, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.noc}'


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Cities'


class Sport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices())
    date_of_birth = models.CharField(max_length=4, default='NA')
    height = models.CharField(max_length=5, default='NA', help_text='Measurement Unit - centimeters')
    weight = models.CharField(max_length=5, default='NA', help_text='Measurement Unit - kilograms')
    noc = models.ForeignKey(NOC, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}, {self.date_of_birth}, {self.noc}'


class Olympics(models.Model):
    season = models.CharField(max_length=6, choices=SeasonChoices.choices())
    year = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city} - {self.year}, {self.season}'

    class Meta:
        verbose_name_plural = 'Olympics'


class Result(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    olympics = models.ForeignKey(Olympics, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.CharField(max_length=6, choices=MedalChoices.choices())

    def __str__(self):
        return f'{self.athlete.name}, {self.olympics}, {self.event}, {self.medal}'


class CSV(models.Model):
    file_name = models.FileField(upload_to='core/uploads')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File ID: {self.id}'
