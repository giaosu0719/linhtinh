from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 69420)
    pub_date = models.DateTimeField("date published")
    
    show_on_list = models.BooleanField(default = True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title