from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django.forms import TextInput, CharField, PasswordInput


class LoginForm(AuthenticationForm):

    username = UsernameField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )
