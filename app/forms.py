from django import forms
from .models import User, Account


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class CreateAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender']


# class CreatePost(forms.ModelForm):

#     # this is how you can add custome validation to your forms
#     class Meta:
#         model = Post
#         fields = ['title', 'body', 'thumbnail']
#         labels = {
#             'title': 'Post title:',
#             'body': 'Post content:',
#             'thumbnail': 'Thumbnail for the post:'
#         }


# class TestForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.TextInput()

#     def clean(self):
#         cleaned_data = super(TestForm, self).clean()
#         title = cleaned_data.get('title')
#         if 'fuck' in title:
#             raise forms.ValidationError('the title cannot contain bad words')
#         return cleaned_data
