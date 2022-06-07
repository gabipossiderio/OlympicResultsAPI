from rest_framework import serializers
from core.models import CSV


class CsvReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = ('file_name',)
