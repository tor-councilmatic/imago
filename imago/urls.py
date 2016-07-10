from django.conf.urls import url, include
from imago import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bills', views.BillViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'jurisdictions', views.JurisdictionViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'votes', views.VoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    # detail views
    url(r'^(?P<pk>ocd-jurisdiction/.+)/$', views.JurisdictionViewSet.as_view({'get':'retrieve'}), name='jurisdiction-detail'),
    url(r'^(?P<pk>ocd-person/.+)/$', views.PersonViewSet.as_view({'get':'retrieve'}), name='person-detail'),
    url(r'^(?P<pk>ocd-event/.+)/$', views.EventViewSet.as_view({'get':'retrieve'}), name='event-detail'),
    url(r'^(?P<pk>ocd-vote/.+)/$', views.VoteViewSet.as_view({'get':'retrieve'}), name='voteevent-detail'),
    url(r'^(?P<pk>ocd-organization/.+)/$', views.OrganizationViewSet.as_view({'get':'retrieve'}), name='organization-detail'),
    url(r'^(?P<pk>ocd-bill/.+)/$', views.BillViewSet.as_view({'get':'retrieve'}), name='bill-detail'),
    url(r'^(?P<pk>ocd-division/.+)/$', views.DivisionViewSet.as_view({'get':'retrieve'}), name='division-detail'),
]
