import os

from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import viewsets, permissions

from amk_demo.settings.base import MEDIA_ROOT
from file.helpers import upload_file_to_server
from sample.forms import UploadFileForm
from sample.serializers import SampleUserSerializer, SampleGroupSerializer
from sample.service.excel.sample_read_excel import ReadExcelSample
from user.mixins import LoginRequired


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


class SampleInsertExcelController(LoginRequired, View):

    def get(self, request, *args, **kwargs):
        filepath = os.path.join(MEDIA_ROOT, 'sample_excel_2.xlsx')
        service = ReadExcelSample(filepath)
        service.operate()

        return HttpResponse('Success')


# ViewSets define the view behavior.
class SampleUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SampleUserSerializer
    permission_classes = [permissions.IsAdminUser]


class SampleGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = SampleGroupSerializer
    permission_classes = [permissions.IsAdminUser]
