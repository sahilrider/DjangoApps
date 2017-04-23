import datetime
from django.db import models
from django.db.models import permalink
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=50)
	body = models.TextField()
	posted=models.DateTimeField('date published')
	author=models.CharField(max_length=30)
	def __str__(self):
		return self.title
	
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=200)
    body = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    '''approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()'''

    def __str__(self):
        return self.body

