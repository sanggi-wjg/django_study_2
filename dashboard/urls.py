from django.urls import path, include

from dashboard.views import DashBoardView

from dashboardfile import plotly_app
from dashboardfile import drowdown_app

urlpatterns = [
    path('', DashBoardView.as_view(), name = 'Sample'),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]
