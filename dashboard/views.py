from django.shortcuts import render
from django.views import View

from user.mixins import LoginRequired


class DashBoardView(LoginRequired, View):
    view_title = 'Dashboard Sample'
    template_name = 'dashboard/dashboard_sample.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            'view_title': self.view_title,
        })
