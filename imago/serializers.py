from opencivicdata.models import (
        Bill,
        Division,
        Event,
        EventAgendaItem,
        EventParticipant,
        EventRelatedEntity,
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



class SimpleOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Organization
        exclude = ('locked_fields', 'extras', 'created_at', 'updated_at', 'parent')

class FullOrganizationSerializer(SimpleOrganizationSerializer):
    identifiers = InlineListField(include=['identifier', 'scheme'])
    links = InlineListField()
    memberships = InlineListField(include=['person', 'post_id', 'start_date', 'end_date'])
    contact_details = InlineListField(exclude=['id', 'organization'])
    other_names = InlineListField(exclude=['id', 'organization'])
    children = serializers.StringRelatedField(many=True)
    sources = InlineListField(include=['note', 'url'])
    posts = InlineListField(include=['division', 'id', 'label', 'role'])

    class Meta:
        model = Organization
        fields = None
        exclude = ('locked_fields',)


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


class EventRelatedEntitySerializer(serializers.ModelSerializer):
    entity_id = serializers.CharField()

    class Meta:
        model = EventRelatedEntity
        fields = ('entity_id', 'entity_name', 'entity_type', 'note')


class EventAgendaItemSerializer(serializers.ModelSerializer):
    related_entities = EventRelatedEntitySerializer(many=True)

    class Meta:
        model = EventAgendaItem
        fields = ('description', 'notes', 'order', 'related_entities', 'subjects')

class EventParticipantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EventParticipant
        # TODO: Figure out how to get ocd_url field working
        fields = ('entity_name', 'entity_type', 'entity_id', 'note')


class SimpleEventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Event
        exclude = ('location', 'extras', 'created_at', 'updated_at', 'locked_fields', 'jurisdiction')


class FullEventSerializer(SimpleEventSerializer):
    links = InlineListField()
    sources = InlineListField(exclude=['event', 'id'])
    agenda = EventAgendaItemSerializer(many=True)
    location = InlineDictField(exclude=['event', 'jurisdiction', 'id'])
    participants = EventParticipantSerializer(many=True)

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
    sources = InlineListField(include=['note', 'url'])
    sponsorships = InlineListField(exclude=['bill'])
    votes = InlineListField(include=['counts', 'id', 'motion_classification', 'motion_text', 'result', 'start_date'])


class LegislativeSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LegislativeSession
        fields = (
                'identifier',
                'classification',
                'jurisdiction',
                )
