from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

class Blog(models.Model):
    class GenreChoices(models.TextChoices):
        TECHNOLOGY = "Technology", _("Technology")
        LIFESTYLE = "Lifestyle", _("Lifestyle")
        TRAVEL = "Travel", _("Travel")
        FOOD = "Food", _("Food")
        HEALTH = "Health", _("Health")
       
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(_("Title"), max_length=50)

    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="blogs"
    )

    summary = models.TextField(_("Summary"), max_length=200)

    image = models.ImageField(
        _("Image"), upload_to="blog_images/", blank=True, null=True
    )

    genre = models.CharField(
        _("Genre"), max_length=20, choices=GenreChoices.choices
    )

    content = models.TextField(_("Content"))

    created_at = models.DateTimeField(
        _("Created at"), default=timezone.now, editable=False
    )
    
    duration = models.DurationField(_("Duration"), default=timezone.timedelta())
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ["-created_at"]