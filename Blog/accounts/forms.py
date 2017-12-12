from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Feedback1


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Feedback"
        }
    ))

    class Meta:
        model = Feedback1
        fields = ('text',)

# class EditBioForm(forms.ModelForm):
#         description = forms.CharField(widget = forms.TextInput(
#             attrs = {
#             'class' :'form-control',
#             'placeholder' : "Description"
#             }
#         ))
#         phone = forms.IntegerField(widget = forms.NumberInput(
#             attrs = {
#             'class' :'form-control',
#             'placeholder' : "Mobile Number"
#             }
#         ))
#
#         class Meta:
#             model = Bio
#             fields = ('description',
#                     'phone',)
