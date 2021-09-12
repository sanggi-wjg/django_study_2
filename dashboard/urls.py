from django.urls import path, include

from dashboard.views import DashBoardView, DashBoardStatView

urlpatterns = [
    path('', DashBoardView.as_view(), name = 'Sample'),
    path('stat', DashBoardStatView.as_view(), name = 'StatSample'),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]
