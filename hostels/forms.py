from django import forms
from .models import Hostel
from accounts.models import CustomUser


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['custodian'].queryset = CustomUser.objects.filter(
            role='custodian')
