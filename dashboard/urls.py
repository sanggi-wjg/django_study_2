from django.urls import path, include

from dashboard.views import DashBoardView

urlpatterns = [
    path('', DashBoardView.as_view(), name = 'Sample'),
]
