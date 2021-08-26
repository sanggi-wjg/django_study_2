from django.http import JsonResponse
from django.views.generic.base import View

from apps.modules.helpers.upload_file_helper import upload_file_to_server
from apps.modules.mixins.auth_mixins import LoginRequired


class FileUploadController(LoginRequired, View):

    def post(self, request, *args, **kwargs):
        # form = UploadFileForm(request.POST, request.FILES)
        try:
            media_save_path = request.POST.get('mediaSavePath', 'temp')
            upload_file = request.FILES['uploadFile']

            upload_file_to_server(upload_file, media_save_path)
            return JsonResponse({ 'Code': '0000', 'Message': 'Success' }, status = 200)

        except Exception as e:
            return JsonResponse({ 'Code': '1000', 'Message': e.__str__() }, status = 200)
