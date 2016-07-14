# Copyright (c) Sunlight Foundation, 2014, under the BSD-3 License.
# Authors:
#    - Paul R. Tagliamonte <paultag@sunlightfoundation.com>


from opencivicdata.models import (Jurisdiction,
                                  Organization,
                                  Person,
                                  Bill,
                                  VoteEvent,
                                  Event,
                                  Division
                                 )

import datetime
from imago.serializers import (
        SimpleBillSerializer,
        FullBillSerializer,
        DivisionSerializer,
        SimpleEventSerializer,
        FullEventSerializer,
        JurisdictionSerializer,
        OrganizationSerializer,
        PersonSerializer,
        VoteEventSerializer,
        )
from rest_framework import viewsets

"""
This module contains the class-based views that we expose over the API.

The common logic for these views are in imago.helpers.*Endpoint
"""

class MultiSerializerReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializers = {
        'default': None,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows people to be viewed.
    """
    queryset = Person.objects.all().order_by('-created_at')
    serializer_class = PersonSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows bills to be viewed.
    """
    queryset = Organization.objects.all().order_by('-created_at')
    serializer_class = OrganizationSerializer


class EventViewSet(MultiSerializerReadOnlyModelViewSet):
    """
    API endpoint that allows events to be viewed.
    """
    queryset = Event.objects.all().order_by('-start_time')
    serializers = {
            'default': FullEventSerializer,
            'list': SimpleEventSerializer,
            }


class JurisdictionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows juridiction to be viewed.
    """
    queryset = Jurisdiction.objects.all().order_by('-created_at')
    serializer_class = JurisdictionSerializer


class DivisionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows juridiction to be viewed.
    """
    queryset = Division.objects.all().order_by('-division')
    serializer_class = DivisionSerializer


class BillViewSet(MultiSerializerReadOnlyModelViewSet):
    """
    API endpoint that allows bills to be viewed.
    """
    queryset = Bill.objects.all().order_by('-created_at')
    serializers = {
            'default': FullBillSerializer,
            'list': SimpleBillSerializer,
            }


class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows votes to be viewed.
    """
    queryset = VoteEvent.objects.all().order_by('-created_at')
    serializer_class = VoteEventSerializer
