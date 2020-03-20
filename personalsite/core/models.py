from django.db import models

# Create your models here.

#bang csdl du an
class Project(models.Model):
	title = models.CharField(max_length=355)
	img = models.ImageField(upload_to='projects')

	def __str__(self):
		return self.title