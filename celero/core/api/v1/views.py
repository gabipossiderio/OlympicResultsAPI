import numpy as np
import pandas as pd
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.api.v1.serializers import CsvReaderSerializer
from core.models import (
    Athlete,
    City,
    Event,
    NOC,
    Olympics,
    Region,
    Result,
    Sport,
    Team,
)


class UploadRegionCsvView(GenericAPIView):
    serializer_class = CsvReaderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            with open(object.file_name.path, 'r') as f:
                df = pd.read_csv(f, usecols=[
                    'NOC', 'region', 'notes',
                ])
                cleaned_df = df.replace(np.nan, '', regex=True)

            for value in cleaned_df.to_dict('records'):
                region_instance, _ = Region.objects.get_or_create(
                    region=value['region']
                )
                noc_instance = NOC.objects.filter(noc=value['NOC']).first()
                if not noc_instance:
                    NOC.objects.create(
                        noc=value['NOC'],
                        region=region_instance,
                        notes=value['notes'],
                    )

        return Response(status=status.HTTP_201_CREATED)


class UploadResultsCsvView(GenericAPIView):
    serializer_class = CsvReaderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            with open(object.file_name.path, 'r') as f:
                df = pd.read_csv(f, usecols=[
                    'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight',
                    'Team', 'NOC', 'Year', 'Season', 'City',
                    'Sport', 'Event', 'Medal',
                ])
                cleaned_df = df.replace(np.nan, '', regex=True)

            memo_dict = {
                'team': {},
                'noc': {},
                'city': {},
                'sport': {},
                'event': {},
                'athlete_id': {},
                'olympics': {},
                'result': {},
            }

            for value in cleaned_df.to_dict('records'):
                team_value = value['Team']
                year = value['Year']
                season = value['Season']
                medal = value['Medal']

                if not memo_dict['team'].get(team_value):
                    team_instance, _ = Team.objects.get_or_create(
                        name=team_value
                    )
                    memo_dict['team'][team_value] = team_instance
                else:
                    team_instance = memo_dict['team'][team_value]

                noc_value = value['NOC']
                if not memo_dict['noc'].get(noc_value):
                    noc_instance = NOC.objects.filter(noc=noc_value).first()
                    if not noc_instance:
                        noc_instance = NOC.objects.create(
                            noc=noc_value,
                        )
                    memo_dict['noc'][noc_value] = noc_instance
                else:
                    noc_instance = memo_dict['noc'][noc_value]

                city_value = value['City']
                if not memo_dict['city'].get(city_value):
                    city_instance, _ = City.objects.get_or_create(
                        name=city_value,
                    )
                    memo_dict['city'][city_value] = city_instance
                else:
                    city_instance = memo_dict['city'][city_value]

                sport_value = value['Sport']
                if not memo_dict['sport'].get(sport_value):
                    sport_instance, _ = Sport.objects.get_or_create(
                        name=sport_value,
                    )
                    memo_dict['sport'][sport_value] = sport_instance
                else:
                    sport_instance = memo_dict['sport'][sport_value]

                event_value = value['Event']
                if not memo_dict['event'].get(event_value):
                    event_instance = Event.objects.filter(
                        name=event_value,
                        sport=sport_instance,
                    ).first()
                    if not event_instance:
                        event_instance = Event.objects.create(
                            name=event_value,
                            sport=sport_instance,
                        )
                    memo_dict['event'][event_value] = event_instance
                else:
                    event_instance = memo_dict['event'][event_value]

                athlete_id = value['ID']
                if not memo_dict['athlete_id'].get(athlete_id):
                    name = value['Name']
                    gender = value['Sex']
                    height = value['Height']
                    weight = value['Weight']
                    try:
                        date_of_birth = int(value['Year']) - int(value['Age'])
                    except ValueError:
                        date_of_birth = 'NA'

                    athlete_instance = Athlete.objects.filter(
                        name=name,
                        gender=gender,
                        noc__id=noc_instance.id,
                    ).first()
                    if not athlete_instance:
                        athlete_instance = Athlete.objects.create(
                            name=name,
                            gender=gender,
                            height=height,
                            weight=weight,
                            date_of_birth=date_of_birth,
                            noc=noc_instance,
                            team=team_instance,
                        )
                    memo_dict['athlete_id'][athlete_id] = athlete_instance
                else:
                    athlete_instance = memo_dict['athlete_id'][athlete_id]

                if not memo_dict['olympics'].get(f'{season}-{year}-{city_instance.name}'):
                    olympics_instance = Olympics.objects.filter(
                        season=season,
                        year=year,
                        city=city_instance,
                    ).first()
                    if not olympics_instance:
                        olympics_instance = Olympics.objects.create(
                            season=season,
                            year=year,
                            city=city_instance,
                        )
                    memo_dict['olympics'][f'{season}-{year}-{city_instance.name}'] = olympics_instance
                else:
                    olympics_instance = memo_dict['olympics'][f'{season}-{year}-{city_instance.name}']

                result_instance = Result.objects.filter(
                    athlete=athlete_instance,
                    olympics=olympics_instance,
                    event=event_instance,
                    medal=medal,
                ).first()
                if not result_instance:
                    Result.objects.create(
                        athlete=athlete_instance,
                        olympics=olympics_instance,
                        event=event_instance,
                        medal=medal,
                    )

                object.activated = True
                object.save()

        return Response(status=status.HTTP_201_CREATED)
