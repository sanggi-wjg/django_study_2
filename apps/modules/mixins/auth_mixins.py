from django.contrib.auth.mixins import AccessMixin

from amk_demo.settings.base import LOGIN_URL


class LoginRequired(AccessMixin):
    """Verify that the current user is authenticated."""
    login_url = LOGIN_URL
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
