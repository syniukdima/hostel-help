from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Contact, Report


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', "Email exists")
            raise forms.ValidationError("Email exists")

        return self.cleaned_data

    def clean_username(self):
        data = self.cleaned_data['username']
        user_model = get_user_model()
        if user_model.objects.filter(username=data).exists():
            raise ValidationError("Username already exists")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'problem_type', 'dormitory', 'exact_place',
                  'description']
        labels = {
            'title':  'Проблема',
            'problem_type': "Тип проблеми",
            'dormitory': "Номер гуртожитка",
            'exact_place': "Де саме потрібна допомога?",
            'description': "Опис"
        }


    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['exact_place'].widget.attrs['placeholder'] = "Номер кімнати чи поверх"
        self.fields['description'].widget.attrs['placeholder'] = "Введіть короткий опис проблеми..."


    def clean(self):
        title = self.cleaned_data.get('title')
        problem_type = self.cleaned_data.get('problem_type')
        dormitory = self.cleaned_data.get('dormitory')
        exact_place = self.cleaned_data.get('exact_place')
        description= self.cleaned_data.get('description')
        if not title or not problem_type or not dormitory or not exact_place or not description:
            raise forms.ValidationError("Ви повинні заповнити всі поля!")
        return self.cleaned_data
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','message']

