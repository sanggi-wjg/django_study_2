from django.shortcuts import render

from django.views.generic.base import View


class HomeController(View):
    view_title = 'AMK_DEMO'
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name, {
            'view_title': self.view_title
        })
