from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Login Error")
            if not user.check_password(password):
                raise forms.ValidationError("Login Error")
            if not user.is_active:
                raise forms.ValidationError("Login Error")
        # Continue as normal
        return super(UserLoginForm, self).clean(*args, **kwargs)



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]