from django import forms

from django.contrib.auth.forms import UserCreationForm

from userauths.models import User

class UserRegisterForm(UserCreationForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': '', 'id': ""}))

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User name', 'class': '', 'id': ""})
                               , max_length=100, required=True)

    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile No', 'class': '', 'id': ""})
                            , max_length=100, required=True)

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': '', 'id': ""})
                            , required=True)

    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'id': ""}), required=True)

    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password', 'id': ""})
                                , required=True)

    class Meta:

        model = User

        fields = ('full_name', 'username', 'email', 'phone', 'gender', 'password1', 'password2')


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():

            visible.field.widget.attrs['class'] = "with-border"