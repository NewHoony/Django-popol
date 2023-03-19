from django.db import models
from main.models import User
# Create your models here.


class Project(models.Model):
    project = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cproject_maker", null=True, blank=True) 
    content = models.TextField(null=True, blank=True)
    tech = models.TextField(null=True, blank=True)
    pubdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.project
    


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="cproject/%y/%m",null=True, blank=True)
    con = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.project}_{self.con}"