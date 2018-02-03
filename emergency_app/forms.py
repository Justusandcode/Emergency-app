from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username'
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

RECIPIENTS_CHOICES= [
    (2347083665033 , 'Sandbox'),
    
]

class NewMessageForm(forms.Form):
    message= forms.CharField(required=True,widget=forms.Textarea,max_length=100)
    recipients = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=RECIPIENTS_CHOICES,
    )
