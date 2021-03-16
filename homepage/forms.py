from django import forms
from registration.models import user_profile


class userprofile_updateForm(forms.ModelForm):
    # emp_no = forms.IntegerField(disabled=True)
    # first_name = forms.CharField(max_length=14, disabled=True)
    
    class Meta:
        model = user_profile
        fields = ("profile_picture","website","bio")


