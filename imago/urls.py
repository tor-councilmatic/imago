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

                         DivisionViewSet,
                         EventViewSet,
                         JurisdictionViewSet,
                         OrganizationViewSet,
                         PersonViewSet,
                        )

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'divisions', DivisionViewSet)
router.register(r'events', EventViewSet)
router.register(r'jurisdictions', JurisdictionViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'people', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^votes/$', VoteList.as_view()),
    url(r'^bills/$', BillList.as_view()),
    url(r'^divisions/$', DivisionList.as_view()),

    # detail views
    url(r'^(?P<pk>ocd-jurisdiction/.+)/$', JurisdictionViewSet.as_view({'get':'retrieve'}), name='jurisdiction-detail'),
    url(r'^(?P<pk>ocd-person/.+)/$', PersonViewSet.as_view({'get':'retrieve'}), name='person-detail'),
    url(r'^(?P<pk>ocd-event/.+)/$', EventViewSet.as_view({'get':'retrieve'}), name='event-detail'),
    url(r'^(?P<pk>ocd-vote/.+)/$', VoteDetail.as_view()),
    url(r'^(?P<pk>ocd-organization/.+)/$', OrganizationViewSet.as_view({'get':'retrieve'}), name='organization-detail'),
    url(r'^(?P<pk>ocd-bill/.+)/$', BillDetail.as_view()),
    url(r'^(?P<pk>ocd-division/.+)/$', DivisionViewSet.as_view({'get':'retrieve'}), name='division-detail'),
]
