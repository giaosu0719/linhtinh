import uuid
import os
from django.db import models
from django.utils.deconstruct import deconstructible

@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        extension = os.path.splitext(filename)[-1]
        
        new_filename = f'{uuid.uuid4()}{extension}'
    
        return os.path.join(self.path, new_filename)

file_upload_path = RandomFileName("")

class File(models.Model):

    name_file = models.CharField(max_length = 69,unique = True)
    file_upload = models.FileField(upload_to=file_upload_path)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file_upload.name)
