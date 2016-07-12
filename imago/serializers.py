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
from imago.utils import InlineListField, InlineDictField



class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    #jurisdiction = serializers.StringRelatedField(many=False)
    #sources = serializers.StringRelatedField(many=True)
    #identifiers = serializers.StringRelatedField(many=True)
    #links = serializers.StringRelatedField(many=True)
    #contact_details = serializers.StringRelatedField(many=True)
    #other_names = serializers.StringRelatedField(many=True)
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Organization
        fields = '__all__'


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    memberships = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        exclude = ('locked_fields',)

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
    id = serializers.CharField()
    division_id = serializers.CharField()
    legislative_sessions = InlineListField(exclude=['id', 'jurisdiction', 'bills', 'votes'])

    class Meta:
        model = Jurisdiction
        exclude = ('division', 'locked_fields')

class SimpleEventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Event
        exclude = ('locked_fields', 'location')

class FullEventSerializer(SimpleEventSerializer):
    links = InlineListField()
    sources = InlineListField(exclude=['event'])
    agenda = InlineListField(exclude=['event'])
    location = InlineDictField(exclude=['event', 'jurisdiction', 'id'])
    participants = InlineListField(exclude=['event', 'id'])

    class Meta:
        model = Event
        exclude = ('locked_fields',)

class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Division
        fields = ('id', 'name', 'country', 'posts', 'jurisdictions')


class VoteEventSerializer(serializers.HyperlinkedModelSerializer):
    legislative_session = serializers.StringRelatedField(many=False)

    class Meta:
        model = VoteEvent
        fields = '__all__'


class SimpleBillSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()
    legislative_session = InlineDictField(include=['identifier'])

    class Meta:
        model = Bill
        exclude = ('locked_fields',)


class FullBillSerializer(SimpleBillSerializer):
    actions = InlineListField(exclude=['bill', 'id'])
    sources = InlineListField(exclude=['bill'])
    sponsorships = InlineListField()
    votes = InlineListField(include=['counts', 'id', 'motion_classification', 'motion_text', 'result', 'start_date'])


class LegislativeSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LegislativeSession
        fields = (
                'identifier',
                'classification',
                'jurisdiction',
                )
