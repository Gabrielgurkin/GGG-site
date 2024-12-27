from .models import UserInput
from django.forms import ModelForm, TextInput

class UserInputForm(ModelForm):
    class Meta:
        model = UserInput
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'centered-input',
                'placeholder': 'Введите число',
                'style': 'width: 700px; height: 80px; left: 287px; top: 461px; position: absolute; background: #FFFEFE; border-radius: 60px'

            })
        }
    