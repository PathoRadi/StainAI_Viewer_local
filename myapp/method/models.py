from django.db import models


class AnalysisJob(models.Model):
    user_id = models.CharField(max_length=100)
    image_name = models.CharField(max_length=255)
    job_id = models.CharField(max_length=100, unique=True)

    blob_prefix = models.CharField(max_length=500, blank=True)
    original_url = models.TextField(blank=True)
    annotated_url = models.TextField(blank=True)
    result_json_url = models.TextField(blank=True)

    status = models.CharField(max_length=50, default="processing")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image_name} ({self.status})"