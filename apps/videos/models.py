import logging

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import SoftDeletableModel, TimeStampedModel
from pyyoutube import Api
from rest_framework import exceptions

from apps.core.models import SearchFieldModel, SlugUUIDModel
from apps.core.utils import getbestthumb
from apps.youtube.models import YoutubeChannel

logger = logging.getLogger(__name__)


def upload_video_image_to(_instance, filename):
    # use youtube's default video_id
    extension = filename.split(".").pop()
    return "images/videos/youtube/" + _instance.video_id + "." + extension


def upload_screenshot_image_to(_instance, filename):
    return "images/videos/screenshot/"


class Video(
    SlugUUIDModel, SearchFieldModel, SoftDeletableModel, TimeStampedModel
):  # noqa
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="videos",
        to_field="uuid",
        blank=True,
        null=True,
    )

    ##################
    # Youtube specific
    ##################
    channel = models.ForeignKey(
        "youtube.YoutubeChannel",
        on_delete=models.CASCADE,
        related_name="videos",
        to_field="uuid",
        blank=True,
    )
    video_id = models.CharField(
        verbose_name=_("Youtube video id"),
        max_length=255,
        db_index=True,
        unique=True,
    )

    title = models.CharField(
        _("Title"),
        max_length=255,
        help_text="영상의 제목",
        blank=True,
    )
    description = models.TextField(blank=True)

    # Ref:
    #   - tiktok uses flat thumbnails data whereas youtube uses dictionary format
    # https://developers.tiktok.com/doc/Embed
    thumbnail_url = models.URLField(blank=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    thumbnail_width = models.IntegerField(blank=True, null=True)

    image = models.ImageField(
        upload_to=upload_video_image_to,
        width_field="image_width",
        height_field="image_height",
        max_length=255,
        blank=True,
        null=True,
    )
    image_height = models.IntegerField(
        null=True, blank=True, editable=False, default="0"
    )
    image_width = models.IntegerField(
        null=True, blank=True, editable=False, default="0"
    )
    screenshot = models.ImageField(
        upload_to=upload_screenshot_image_to,
        max_length=255,
        blank=True,
        null=True,
    )

    resp = models.JSONField(null=True, blank=True)

    is_public = models.BooleanField(
        _("Is public"),
        default=False,
        help_text=_("Show this video in search results"),
    )

    # fields to save in search_text from SearchFieldModel
    search_fields = ["title", "channel"]

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        default_related_name = "videos"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        """
        비디오 정보를 유저가 수동으로 입력하는 것이 아니라, video_id로
        Youtube Data API를 사용해 자동으로 저장
        """
        # use Youtube Data API to fill up the fields automatically
        try:
            yt_client = Api(api_key=settings.YOUTUBE_DATA_API_KEY)
            resp = yt_client.get_video_by_id(
                video_id=self.video_id,
                return_json=True,
            )
        except Exception as e:
            logger.error(
                "Metadata for video: %s cannot be fetched: %s", self.video_id, str(e)
            )
            raise exceptions.ValidationError(
                "Error while requesting video data: %s", self.video_id
            )

        #######################################################################
        # automatically set the fields using the data from Youtube Data API
        #######################################################################
        if not resp.get("items"):
            raise exceptions.ValidationError("%s maybe invalid video_id", self.video_id)

        extracted = resp["items"][0]["snippet"]

        self.resp = resp
        self.title = extracted["title"]
        self.description = extracted["description"]

        best_thumb = getbestthumb(extracted["thumbnails"])
        self.thumbnail_url = best_thumb["url"]
        self.thumbnail_height = best_thumb["height"]
        self.thumbnail_width = best_thumb["width"]

        channel, __ = YoutubeChannel.available_objects.get_or_create(
            channel_id=extracted["channelId"]
        )
        self.channel = channel
