from django.forms import ModelForm, TextInput
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'birthday']
        widgets = {
            'birthday': TextInput(attrs={'autocomplete': 'off'})
        }