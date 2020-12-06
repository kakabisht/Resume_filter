from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    '''
    User creating a form, using inbuilt django module
    '''
    class Meta:
        #fields  for sign up page
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()


    # For custom labeleling the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
