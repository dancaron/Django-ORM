"""
The fields matches xml push notifications by google api sent when a channel:
    - uploads a video
    - updates a video's title
    - updates a video's description

See "Subscribe to Push Notifications" for examples:
    https://developers.google.com/youtube/v3/guides/push_notifications
"""
import logging

from django.conf import settings
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from pyyoutube import Api
from rest_framework import exceptions

from apps.core.models import SlugUUIDModel
from apps.core.utils import getbestthumb

logger = logging.getLogger(__name__)


class YoutubeChannel(SlugUUIDModel, SoftDeletableModel, TimeStampedModel):
    channel_id = models.CharField(max_length=255, db_index=True, unique=True)
    name = models.CharField(max_length=255, db_index=True, unique=True)

    thumbnail_url = models.URLField(blank=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    thumbnail_width = models.IntegerField(blank=True, null=True)

    resp = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        """
        채널 정보를 유저가 수동으로 입력하는 것이 아니라, channel_id로
        Youtube Data API를 사용해 자동으로 저장
        """
        try:
            yt_client = Api(api_key=settings.YOUTUBE_DATA_API_KEY)
            ##################################################
            # try with channel_id first as it is more accurate
            #
            # resp의 차이:
            # get_channel_info: channeld_id가 snippet 바깥(한 레벨 위)에 있음
            #   - snippet
            #   |
            #   - channelID(get_channel_info)
            #
            # search_by_keywords: channeld_id가 snippet 아래에 있음
            #   - snippet - channelID(search_by_keywords)
            #
            ##################################################
            if self.channel_id:
                resp = yt_client.get_channel_info(
                    channel_id=self.channel_id, return_json=True
                )
            else:
                resp = yt_client.search_by_keywords(
                    q=self.name,
                    search_type=["channel"],
                    count=5,
                    limit=5,
                    return_json=True,
                )
        except Exception as e:
            logger.error(
                "Metadata for youtube channel: %s cannot be fetched: %s",
                self.channel_id,
                str(e),
            )
            raise exceptions.ValidationError(
                "%s maybe invalid channel_id" % self.channel_id
            )

        if not resp.get("items", None):
            raise exceptions.ValidationError(
                "Channel data seems invalid - id: %s, name: %s"
                % (self.channel_id, self.name)
            )

        #######################################################################
        # set the fields using the data from Youtube Data API
        #######################################################################
        extracted = resp["items"][0]["snippet"]

        self.resp = resp
        self.name = extracted["title"]
        # get_channel_info(by id)와 search_by_keywords(by name)의 응답값 형태가 다름
        self.channel_id = extracted.get("channelId", None) or resp["items"][0]["id"]

        best_thumb = getbestthumb(extracted["thumbnails"])
        self.thumbnail_url = best_thumb.get("url", None)
        self.thumbnail_height = best_thumb.get("height", None)
        self.thumbnail_width = best_thumb.get("width", None)
