from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'birthday']
        widgets = {
            'birthday': AdminDateWidget()
        }