import os

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from amk_demo.settings.base import MEDIA_ROOT
from file.helpers import upload_file_to_server
from sample.forms import UploadFileForm
from sample.models import Snippet
from sample.serializers import SampleUserSerializer, SampleGroupSerializer, SnippetSerializer
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SampleGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = SampleGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class SnippetView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SnippetView(ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


class SnippetView(View):

    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return JsonResponse(serializer.data, safe = False)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)


class SnippetDetailView(View):

    def get(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet.objects, id = kwargs['pk'])
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    def put(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet.objects, id = kwargs['pk'])
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status = 400)

    def delete(self, request, *args, **kwargs):
        snippet = get_object_or_404(Snippet.objects, id = kwargs['pk'])
        snippet.delete()
        return HttpResponse(status = 204)
