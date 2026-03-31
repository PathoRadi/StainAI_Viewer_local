from django.db import models
from django.utils import timezone


class AnalysisJob(models.Model):
    """
    One analysis task for one uploaded image.
    This stores the high-level metadata for a detection run.
    """

    STATUS_CHOICES = [
        ("uploaded", "Uploaded"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    # Optional: if your main site later passes a real user id into StainAI_Viewer
    user_id = models.CharField(max_length=100, blank=True, default="anonymous")

    # One job id per analysis task
    job_id = models.CharField(max_length=100, unique=True)

    # Original image folder name in media/images/<image_name>/
    image_name = models.CharField(max_length=255)

    # Optional project name if you want grouping later
    project_name = models.CharField(max_length=255, blank=True, default="")

    # Current job status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="uploaded"
    )

    # Blob storage prefix, e.g. users/12/jobs/abc123
    blob_prefix = models.CharField(max_length=500, blank=True, default="")

    # Common representative URLs for quick display
    original_url = models.TextField(blank=True, default="")
    gray_url = models.TextField(blank=True, default="")
    annotated_url = models.TextField(blank=True, default="")
    result_json_url = models.TextField(blank=True, default="")
    progress_url = models.TextField(blank=True, default="")

    # Optional summary info
    total_detections = models.IntegerField(default=0)
    error_message = models.TextField(blank=True, default="")

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "analysis_job"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.image_name} [{self.status}]"

    @property
    def is_done(self):
        return self.status == "completed"

    @property
    def is_failed(self):
        return self.status == "failed"


class AnalysisJobFile(models.Model):
    """
    Stores each uploaded artifact file for an AnalysisJob.
    For example:
      - original/xxx.png
      - gray/xxx.png
      - annotated/xxx.png
      - result/bar_chart.png
      - _detect_result.json
    """

    FILE_TYPE_CHOICES = [
        ("original", "Original"),
        ("gray", "Gray"),
        ("annotated", "Annotated"),
        ("result", "Result"),
        ("json", "JSON"),
        ("progress", "Progress"),
        ("other", "Other"),
    ]

    job = models.ForeignKey(
        AnalysisJob,
        on_delete=models.CASCADE,
        related_name="files"
    )

    file_type = models.CharField(
        max_length=20,
        choices=FILE_TYPE_CHOICES,
        default="other"
    )

    # Relative path under the blob prefix
    # Example: original/CR1_slide_10.png
    relative_path = models.CharField(max_length=500)

    # Full blob path
    # Example: users/12/jobs/abc123/original/CR1_slide_10.png
    blob_path = models.CharField(max_length=1000)

    # Full accessible blob URL
    blob_url = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "analysis_job_file"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.job.image_name} - {self.relative_path}"


class DetectionSummary(models.Model):
    """
    Optional summary table for storing class counts from detection result.
    Useful if you want fast query for charts without reopening result JSON.
    """

    job = models.OneToOneField(
        AnalysisJob,
        on_delete=models.CASCADE,
        related_name="summary"
    )

    r_count = models.IntegerField(default=0)
    h_count = models.IntegerField(default=0)
    b_count = models.IntegerField(default=0)
    a_count = models.IntegerField(default=0)
    rd_count = models.IntegerField(default=0)
    hr_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "detection_summary"

    def __str__(self):
        return f"Summary for {self.job.image_name}"

    @property
    def total(self):
        return (
            self.r_count
            + self.h_count
            + self.b_count
            + self.a_count
            + self.rd_count
            + self.hr_count
        )