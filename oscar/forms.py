from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Full Name', widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(label = 'Confirm-Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class OfferForm(forms.ModelForm):
    class Meta:
        model = SkillOffer
        fields = ['skill', 'available_time', 'description']

class RequestForm(forms.ModelForm):
    class Meta:
        model = SkillRequest
        fields = ['skill', 'description']



class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Email', widget = forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('username')
        passowrd = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
            self.cleaned_data['username'] = user.username

        except User.DoesNotExist:
            raise forms.ValidationError("Invalid Email or password")
        
        return super().clean()