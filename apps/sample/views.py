from django.shortcuts import render
from django.views.generic.base import View

from apps.modules.helpers.upload_file_helper import upload_file_to_server
from apps.modules.mixins.auth_mixins import LoginRequired
from apps.sample.forms import UploadFileForm


class SampleController(LoginRequired, View):
    view_title = '샘플'
    template_name = 'sample/sample_content.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            'view_title' : self.view_title,
            'upload_form': UploadFileForm()
        })

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            upload_file_to_server(request.FILES.get('uploadFile'))


class SampleMultiController(LoginRequired, View):
    view_title = '샘플'
    template_name = 'sample/sample_multi_content.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context = {
            'view_title' : self.view_title,
            'upload_form': UploadFileForm()
        })
