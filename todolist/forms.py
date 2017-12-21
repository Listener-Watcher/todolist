from django import forms

PRIORITY_CHOICES = (
	(0,'Urgent'),
	(1,'Normal'),
)
STATUS_CHOICES = (
	(0,'Unfinished'),
	(1,'finished'),
)
class AddForm(forms.Form):
 	title = forms.CharField(max_length=100)
	text = forms.CharField()
	createdTime = forms.SplitDateTimeField()
	priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
	finished = forms.ChoiceField(choices=STATUS_CHOICES)

class DeleteForm(forms.Form):
	title=forms.CharField(max_length=100)
	
class EditForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(max_length=200)
class EditTimeForm(forms.Form):
	title = forms.CharField(max_length=100)
	createdTime = forms.SplitDateTimeField()
class EditFinishedForm(forms.Form):
	title = forms.CharField(max_length=100)
	finished = forms.ChoiceField(choices=STATUS_CHOICES)
