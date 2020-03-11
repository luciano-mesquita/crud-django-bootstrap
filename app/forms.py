from django.forms import ModelForm
from .models import Person, User


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

