from opencivicdata.models.people_orgs import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
                'id',
                'name',
                'created_at',
                'updated_at',
                )

