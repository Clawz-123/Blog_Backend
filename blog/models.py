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

   title = models.CharField(_(""), max_length=50)

   summary = models.TextField(_(""), max_length=200)

   image = models.ImageField(
       _(""), upload_to="blog_images/", blank=True, null=True
    )
    
   genre = models.CharField(
        _(""), max_length=20, choices=GenreChoices.choices
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



        