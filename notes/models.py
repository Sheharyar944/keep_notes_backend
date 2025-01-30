from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    user=models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
    





