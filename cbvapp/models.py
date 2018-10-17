from django.db import models
from django.urls import reverse
class Collage(models.Model):
    name = models.CharField(max_length=250)
    principal_name = models.CharField(max_length=250)
    location = models.CharField(max_length=200)
    contact_no = models.PositiveIntegerField()
    registered_at = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cbvapp:detail',kwargs={'pk':self.pk})

class student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    contact = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE,related_name='students')
    pic = models.FileField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.name
