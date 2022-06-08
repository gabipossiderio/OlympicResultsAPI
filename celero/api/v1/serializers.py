from rest_framework import serializers
from api.models import (
    Athlete,
    City,
    CSV,
    Event,
    NOC,
    Olympics,
    Region,
    Result,
    Sport,
    Team,
)


class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = ('file_name',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'region',)


class NOCSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = NOC
        fields = ('id', 'noc', 'region', 'notes',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name',)


class EventSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = Event
        fields = ('id', 'name', 'sport',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name',)


class AthleteSerializer(serializers.ModelSerializer):
    noc = NOCSerializer()
    team = TeamSerializer()

    class Meta:
        model = Athlete
        fields = ('id', 'name', 'gender', 'date_of_birth', 'height', 'weight', 'noc', 'team',)


class OlympicsSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Olympics
        fields = ('id', 'season', 'year', 'city',)


class ResultSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer()
    olympics = OlympicsSerializer()
    event = EventSerializer()

    class Meta:
        model = Result
        fields = ('id', 'athlete', 'olympics', 'event', 'medal',)
