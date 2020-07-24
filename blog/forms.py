from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """Add form-control to all elements in the field to use bootstrap
        Forms """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')
