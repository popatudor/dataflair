from django import forms
from django.core import validators

#DataFlair #Custom_Validator
def check_size(value):
  if len(value) < 6:
    raise forms.ValidationError("the Password is too short")

#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField(required = False)
    email = forms.EmailField(help_text = 'write your email', required = False)
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )
    age = forms.IntegerField(required = False, )

    password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)

    #Validation #DataFlair
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password