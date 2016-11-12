from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.CharField(label='School Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput())

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['confirm_password']:
            self._errors['password'] = ["Passwords do not match!"]  # why can we use that underscore there?
            del form_data['password']
        return form_data