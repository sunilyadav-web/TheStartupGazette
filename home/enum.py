from django.db import models


class StatusEnum(models.TextChoices):
    DRAFT = "Drafted", "Draft"
    PUBLISH = "Published", "Publish"
