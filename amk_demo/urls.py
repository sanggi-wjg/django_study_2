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
from django.conf import settings
from django.urls import path, include

from home import views as home
from user import views as user
from file import views as file

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', home.HomeController.as_view(), name = 'Home'),

    path('login', user.UserLoginController.as_view(), name = 'Login'),
    path('logout', user.UserLogoutController.as_view(), name = 'Logout'),
    path('signup', user.UserSignUpController.as_view(), name = "SignUp"),

    path('file/upload', file.FileUploadController.as_view(), name = 'FileUpload'),

    path('sample/', include('sample.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.urls import include

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)), )
