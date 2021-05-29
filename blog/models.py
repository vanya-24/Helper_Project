from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
	sn0 = models.AutoField(primary_key = True)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=13)
	age = models.CharField(max_length=2)
	requirment = models.TextField()
	slug = models.CharField(max_length=129)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return 'Title by: '+ self.title

class BlogComment(models.Model):
	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.CASCADE,null = True)
	timestamp = models.DateTimeField(default=now)
	def __str__(self):
		return self.comment[0:13] + "... " + "by " + self.user.username