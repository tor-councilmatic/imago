from django.conf.urls import url, include
from imago.views import (JurisdictionList,
                         PeopleList,
                         VoteList,
                         EventList,
                         BillList,
                         OrganizationList,
                         DivisionList,

                         JurisdictionDetail,
                         PersonDetail,
                         EventDetail,
                         VoteDetail,
                         BillDetail,
                         OrganizationDetail,
                         DivisionDetail,

                         EventViewSet,
                         OrganizationViewSet,
                         PersonViewSet,
                        )

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jurisdictions/$', JurisdictionList.as_view()),
    url(r'^votes/$', VoteList.as_view()),
    url(r'^bills/$', BillList.as_view()),
    url(r'^divisions/$', DivisionList.as_view()),

    # detail views
    url(r'^(?P<pk>ocd-jurisdiction/.+)/$', JurisdictionDetail.as_view()),
    url(r'^(?P<pk>ocd-person/.+)/$', PersonViewSet.as_view({'get':'retrieve'}), name='person-detail'),
    url(r'^(?P<pk>ocd-event/.+)/$', EventViewSet.as_view({'get':'retrieve'}), name='event-detail'),
    url(r'^(?P<pk>ocd-vote/.+)/$', VoteDetail.as_view()),
    url(r'^(?P<pk>ocd-organization/.+)/$', OrganizationViewSet.as_view({'get':'retrieve'}), name='organization-detail'),
    url(r'^(?P<pk>ocd-bill/.+)/$', BillDetail.as_view()),
    url(r'^(?P<pk>ocd-division/.+)/$', DivisionDetail.as_view()),
]
