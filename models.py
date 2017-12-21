from django.db import models
import datetime

PRIORITY_CHOICES = (
	(0,'Urgent'),
	(1,'Normal'),
)
class Item(models.Model):
	title = models.CharField(max_length=100,primary_key=True)
	text = models.TextField()
	createdTime = models.DateTimeField()
	priority = models.IntegerField(choices=PRIORITY_CHOICES,default=1)
	finished = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-priority','title']#descending order for the priority column
	class Admin:
		pass
# Create your models here.
