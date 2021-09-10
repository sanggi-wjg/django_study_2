from django.shortcuts import render
from django.views import View

from user.mixins import LoginRequired


class DashBoardView(LoginRequired, View):
    view_title = 'Dash Sample'
    template_name = 'dash/dash_sample.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            'view_title': self.view_title,
        })
