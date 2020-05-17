from django import forms
from .models import ColdEntry,Diary
from django.core.exceptions import ValidationError

class EntryForm(forms.ModelForm):

    class Meta:
        model=ColdEntry
        fields=['serial_no','rank','packets','floor']


class DiaryForm(forms.ModelForm):
    class Meta:
        model=Diary
        fields=['diary_name']
