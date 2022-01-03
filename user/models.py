from django.db import models

class Project(models.Model):
    project_title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    Language_used=models.CharField(max_length=50)
    link=models.URLField(max_length=200)
    upload = models.ImageField(upload_to="images/",null=True,blank=True)



    def __str__(self):
        return self.project_title