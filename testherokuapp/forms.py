from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    contactdetails = forms.IntegerField()
    emailid = forms.EmailField()
    addressdetails = forms.CharField(required=False)
    workexperience = forms.CharField(required=False)
    visastatus = forms.CharField(required=False)
    workpermit = forms.CharField(required=False)
    readytorelocate = forms.CharField(required=False)
    technology = forms.CharField(widget=forms.Textarea, required=False)


    class Meta:
        model = Candidate
        fields = "__all__"