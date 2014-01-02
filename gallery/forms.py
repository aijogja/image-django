from django import forms
from gallery.models import Gallery, Comment

class AddGalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = ['image']

class AddCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
		widgets = {
			'comment': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }