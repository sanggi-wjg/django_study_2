"""amk_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.home import views as home
from apps.user import views as user
from apps.file import views as file
from apps.sample import views as sample

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', home.HomeController.as_view(), name = 'Home'),

    path('login', user.UserLoginController.as_view(), name = 'Login'),
    path('logout', user.UserLogoutController.as_view(), name = 'Logout'),
    path('signup', user.UserSignUpController.as_view(), name = "SignUp"),

    path('file/upload', file.FileUploadController.as_view(), name = 'FileUpload'),

    path('sample', sample.SampleController.as_view(), name = 'Sample'),
    path('sample-multi', sample.SampleMultiController.as_view(), name = 'SampleMulti'),
]
