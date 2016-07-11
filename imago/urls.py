from django.conf.urls import url, include
from imago import views, routers
#from rest_framework.routers import DefaultRouter

router = routers.DefaultOCDRouter()
router.register(r'bills', views.BillViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'jurisdictions', views.JurisdictionViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'votes', views.VoteViewSet)

# Accept slash routes, like GitHub API
slashless_router = routers.DefaultOCDRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(slashless_router.urls)),
]
