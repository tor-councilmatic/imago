from opencivicdata.models.people_orgs import Person, Membership
from rest_framework import serializers


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = (
            'start_date',
            'end_date',
            'role',
            'label',
            )


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    memberships = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = (
                'name',
                'id',
                'sort_name',
                'image',
                'gender',
                'url',
                'memberships',
                )
