from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

import uuid


class Blog(models.Model):
   id = models.UUIDField(
       primary_key=True, default=uuid.uuid4, editable=False, unique=True
   )

   title = models.CharField(_(""), max_length=50)

   summary = models.TextField(_(""), max_length=200)

   image = models.ImageField(
       _(""), upload_to="blog_images/", blank=True, null=True
    )
   
   content = models.TextField(_(""))

   created_at = models.DateTimeField(
       _(""), default=timezone.now, editable=False
   )
   duration = models.DurationField(_(""), default=timezone.timedelta())



class Meta:
    verbose_name = _("Blog")
    verbose_name_plural = _("Blogs")
    ordering = ["-id"]


class Choices(models.Choices):
    TECHNOLOGY = "Technology"
    DESIGN = "Design"
    BUSINESS = "Business"
    PROGRAMMING = "Programming"

    STATUS_CHOICES = [
        (TECHNOLOGY, _("Technology")),
        (DESIGN, _("Design")),
        (BUSINESS, _("Business")),
        (PROGRAMMING, _("Programming")),
    ]

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")
        ordering = ["-id"]
        