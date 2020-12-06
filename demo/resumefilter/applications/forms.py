from django import forms
from . import models


class ApplicationForm(forms.ModelForm):
    '''
        Application form for applying to a company        
    '''
    class Meta:
        # Selecting all the fields
        fields = '__all__'
        model = models.Application

    def __init__(self, *args, **kwargs):
        # Storing information about a user to a company
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["company"].queryset = (
                models.Company.objects.filter(
                    pk__in=user.companys.values_list("company__pk")
                )
            )
