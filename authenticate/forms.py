from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email address'}))
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small>'
        self.fields['username'].widget.attrs['placeholder'] = 'user name'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        self.fields['password1'].widget.attrs['placeholder'] = 'pass word'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<small>Enter the same password as before, for verification.</small>'
        self.fields['password2'].widget.attrs['placeholder'] = 'retype your password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'email address'
        self.fields['email'].widget.attrs['class'] = 'form-control'

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email address'}))
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',)

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small>'
        self.fields['username'].widget.attrs['placeholder'] = 'user name'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        #self.fields['password1'].label = ''
        #self.fields['password1'].help_text = '<ul class="small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        #self.fields['password1'].widget.attrs['placeholder'] = 'pass word'
        #self.fields['password1'].widget.attrs['class'] = 'form-control'
        #self.fields['password2'].label = ''
        #self.fields['password2'].help_text = '<small>Enter the same password as before, for verification.</small>'
        #self.fields['password2'].widget.attrs['placeholder'] = 'retype your password'
        #self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'email address'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class UpdateProfileForm(forms.ModelForm):
    fav_colour = forms.CharField(label="", required=True , max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Favourite Color'}))

    class Meta:
        model = Profile
        fields = ('fav_colour',)

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['fav_colour'].label = ''