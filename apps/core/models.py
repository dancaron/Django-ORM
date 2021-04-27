from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ShortUUIDField
from model_utils.models import TimeStampedModel as BaseTimeStampedModel


class UUIDModel(models.Model):
    """ Needed to hide sequential keys from API endpoints """

    uuid = ShortUUIDField(db_index=True, editable=False, unique=True)

    class Meta:
        abstract = True


class SlugUUIDModel(UUIDModel):
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class SearchFieldModel(models.Model):
    # Inspired by: oscar's AbstractAddress
    #: A field only used for searching - this contains all the relevant fields.
    # This is effectively a poor man's Solr text field.
    search_text = models.TextField(
        _("Search text - used only for searching products"),
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def _update_search_text(self):
        search_fields = filter(
            bool,
            [
                str(getattr(self, field.name)).lower()
                for field in self._meta.get_fields()
                if field.name in self.search_fields
            ],
        )
        self.search_text = " ".join(search_fields)

    def save(self, *args, **kwargs):
        self._update_search_text()
        super().save(*args, **kwargs)


class TimeStampedModel(BaseTimeStampedModel):
    @property
    def localized_created(self):
        return timezone.localtime(self.created)

    @property
    def current_timezone(self):
        return timezone.get_current_timezone()

    class Meta:
        abstract = True
