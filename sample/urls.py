from django.urls import path, include
from rest_framework import routers

from sample.views import SampleUserViewSet, SampleGroupViewSet, SampleController, SampleMultiController, SampleInsertExcelController, SnippetView, SnippetDetailView

router = routers.DefaultRouter()
router.register('users', SampleUserViewSet)
router.register('groups', SampleGroupViewSet)

urlpatterns = [
    path('', include(router.urls), name = 'UserSerial'),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),

    path('sample', SampleController.as_view(), name = 'Sample'),
    path('sample-multi', SampleMultiController.as_view(), name = 'SampleMulti'),
    path('sample-insert', SampleInsertExcelController.as_view(), name = 'SampleInsertExcel'),

    path('snippets/', SnippetView.as_view()),
    path('snippets/<int:pk>/', SnippetDetailView.as_view()),
]
