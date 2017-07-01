from django import forms
from closetclient.models import Profile

class ProfileForm(forms.ModelForm):  

    class Meta:
        model = Profile
        fields = ('profile_name', 'birth_date', 'zip_code', 'bio')