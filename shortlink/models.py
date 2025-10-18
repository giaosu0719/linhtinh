from django.db import models

class Domain(models.Model):

    domain_custom = models.CharField(max_length = 256, unique = True)

    def __str__(self):
        return self.domain_custom

class UrlInput(models.Model):

    url_original = models.CharField(max_length = 512, unique = True)
    url_new = models.CharField(max_length = 25, unique = True)
    instant_forward = models.BooleanField(default = False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.url_original
    
    