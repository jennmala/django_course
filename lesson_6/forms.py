from django import forms
from durationwidget.widgets import TimeDurationWidget

from lesson_5.models import Client


class MyForm(forms.Form):
    name = forms.CharField(label='User name', initial='User name')
    profile_picture = forms.ImageField(widget=forms.FileInput)
    # additional_file = forms.FileField(widget=forms.FileInput)

    email = forms.EmailField(initial='admin@admin.com', error_messages={'required': 'Please enter you available email'})
    password = forms.CharField(max_length=20, min_length=10, widget=forms.PasswordInput(), required=False)
    age = forms.IntegerField(required=False, help_text='Enter your current age')
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10)
    birthday = forms.DateField(widget=forms.SelectDateWidget, required=False)
    work_experience = forms.DurationField(required=False, widget=TimeDurationWidget(show_days=True, show_hours=True, show_minutes=False, show_seconds=False))
    gender = forms.ChoiceField(required=False, choices=[('1', 'man'), ('2', 'woman')])


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['user', 'second_email']