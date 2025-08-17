from django.db import models


class GeneralInfo(models.Model):
    company_name=models.CharField(max_length=255,default="Company")
    location=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    open_hours=models.CharField(max_length=100,blank=True,null=True)
    video_url=models.URLField(blank=True,null=True)
    twitter_url=models.URLField(blank=True,null=True)
    facebook_url=models.URLField(blank=True,null=True)
    instagram_url=models.URLField(blank=True,null=True)
    linkdin_url=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.company_name

