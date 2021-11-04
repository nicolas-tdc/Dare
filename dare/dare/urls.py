"""URL configuration for Dare App."""


from django.contrib import admin
from django.urls import path
from rest_framework import routers
from dare_app.views import (
    UserViewSet, GroupViewSet, ChallengeViewSet, ChallengeCollectionViewSet,
    PartyViewSet, EquimentViewSet, ProofOfSuccessViewSet,
)

"""
ViewSets Routing
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'challenges', ChallengeViewSet)
router.register(r'challenge-collections', ChallengeCollectionViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'equipments', EquimentViewSet)
router.register(r'proofs-of-success', ProofOfSuccessViewSet)


"""
URL Patterns
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
