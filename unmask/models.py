from django.db import models

# Create your models here.


class links(models.Model):
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.url



