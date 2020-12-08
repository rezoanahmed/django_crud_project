from django import forms
from myapp.views import *
class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"