from django.db import models

class Port(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='bport/pdfs/')
    cover = models.ImageField(upload_to='bport/covers/', null=True, blank=True)

    def __str__(self):
        return self.title
