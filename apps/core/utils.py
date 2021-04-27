from typing import Union
from urllib.error import HTTPError
from urllib.request import urlopen


def _content_available(url):
    """
    https://github.com/mps-youtube/pafy/blob/5903c16e70fa9ac46fd368cf6375dd88018378dd/pafy/backend_shared.py#L430
    """
    try:
        response = urlopen(url)
    except HTTPError:
        return False
    else:
        return response.getcode() < 300


def getbestthumb(thumbnails: dict) -> Union[dict, None] or str:
    """
    Return the best available thumbnail.
    https://github.com/mps-youtube/pafy/blob/5903c16e70fa9ac46fd368cf6375dd88018378dd/pafy/backend_shared.py#L438
    """
    resolutions = ("maxres", "standard", "high", "medium", "default")
    for resolution in resolutions:
        if bestthumb := thumbnails.get(resolution, None):
            if _content_available(bestthumb["url"]):
                return bestthumb
    return ""
