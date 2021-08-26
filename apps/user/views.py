from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView

from amk_demo.settings.base import LOGIN_URL


class UserLoginController(View):
    view_title = '로그인'
    template_name = 'user/user_login.html'

    def get(self, request, *args, **kwargs):
        auth_form = AuthenticationForm()

        return render(request, self.template_name, context = {
            'view_title': self.view_title,
            'auth_form' : auth_form
        })

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        return self.try_login(request, user)

    def try_login(self, request, user):
        if user is not None:
            login(request, user)
            return self.redirect_to_prev_request_page(request.POST.get('redirect_to', ''))
        else:
            return render(request, self.template_name, context = {
                'view_title': self.view_title,
                'error_msg' : '아이디 혹은 비밀번호가 틀렸습니다.'
            })

    def redirect_to_prev_request_page(self, redirect_to: str):
        if redirect_to == '':
            return redirect('/')
        else:
            return redirect(redirect_to)


class UserLogoutController(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(LOGIN_URL)


class UserSignUpController(View):
    view_title = '가입'
    template_name = 'user/user_signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        user_form = UserCreationForm()
        return render(request, self.template_name, {
            'view_title': self.view_title,
            'user_form' : user_form,
        })

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            self.try_signup(user_form)
        else:
            return render(request, self.template_name, {
                'view_title': self.view_title,
                'user_form' : user_form,
                'error_msg' : user_form.error_messages,
            })

    def try_signup(self, user_form):
        user = user_form.save()
        authenticate(username = user.username, passowrd = user.password)
        return redirect('/login')
