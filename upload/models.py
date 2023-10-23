from django.db import models


class PDFUpload(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.TextField()  # URL path to external storage like AWS S3
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    last_accessed_timestamp = models.DateTimeField(null=True, blank=True)
    size = models.IntegerField()
