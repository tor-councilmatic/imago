from opencivicdata.models import (
        Bill,
        Division,
        Event,
        Jurisdiction,
        LegislativeSession,
        Membership,
        Organization,
        Person,
        Post,
        VoteEvent,
        )
from rest_framework import serializers



class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    jurisdiction = serializers.StringRelatedField(many=False)
    sources = serializers.StringRelatedField(many=True)
    identifiers = serializers.StringRelatedField(many=True)
    links = serializers.StringRelatedField(many=True)
    contact_details = serializers.StringRelatedField(many=True)
    other_names = serializers.StringRelatedField(many=True)

    class Meta:
        model = Organization
        fields = (
                'id',
                'url',
                'name',
                'image',

                'created_at',
                'updated_at',

                'extras',

                'identifiers',
                'links',
                'contact_details',
                'other_names',

                'classification',
                'founding_date',
                'dissolution_date',
                'jurisdiction',
                'sources',
                )



class PersonSerializer(serializers.HyperlinkedModelSerializer):
    memberships = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = (
                'id',
                'url',
                'name',
                'sort_name',
                'image',
                'gender',
                'memberships',
                )

class MembershipSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField(many=False)
    person = serializers.StringRelatedField(many=False)
    post = serializers.StringRelatedField(many=False)
    # TODO: fix
    on_behalf_of = serializers.StringRelatedField(many=False)
    contact_details = serializers.StringRelatedField(many=True)

    class Meta:
        model = Membership
        fields = (
            'start_date',
            'end_date',
            'role',
            'label',
            )

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
                'id',
                'label',
                'role',
                'start_date',
                'end_date',
                )

class JurisdictionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Jurisdiction
        fields = (
                'id',
                'url',
                'name',
                'url',

                'updated_at',
                'created_at',

                'classification',
                'extras',
                'feature_flags',

                'division',
                #'division_id',
                )


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = (
                'id',
                'url',
                'name',
                'jurisdiction',
                'jurisdiction_id',
                'description',
                'classification',

                'participants',

                'documents',
                'media',

                'links',

                'created_at',
                'updated_at',

                'start_time',
                'end_time',
                'timezone',

                'all_day',
                'status',

                'location',

                'agenda',
                'extras',

                'sources',
                )

class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Division
        fields = '__all__'


class VoteEventSerializer(serializers.HyperlinkedModelSerializer):
    legislative_session = serializers.StringRelatedField(many=False)

    class Meta:
        model = VoteEvent
        fields = '__all__'


class BillSerializer(serializers.HyperlinkedModelSerializer):
    legislative_session = serializers.StringRelatedField(many=False)

    class Meta:
        model = Bill
        fields = '__all__'

class LegislativeSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LegislativeSession
        fields = (
                'identifier',
                'classification',
                'jurisdiction',
                )
