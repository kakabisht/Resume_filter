from django import forms
from . import models


class ApplicationForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Application

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["company"].queryset = (
                models.Company.objects.filter(
                    pk__in=user.companys.values_list("company__pk")
                )
            )
