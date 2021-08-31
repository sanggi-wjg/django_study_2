from django import forms


class UploadFileForm(forms.Form):
    """
    파일 업로드 Form
    https://docs.djangoproject.com/ko/3.2/topics/http/file-uploads/
    """
    uploadFile = forms.FileField(label = '파일 선택', allow_empty_file = False, )
