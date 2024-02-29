from django.db import models
import uuid

class XML(models.Model):
    file_name = models.CharField(max_length=255)
    file_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.file_name)
