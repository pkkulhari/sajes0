from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from accounts.forms import LoginForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next is not None:
            return next

        return reverse("dashboard:home")


class LogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")
