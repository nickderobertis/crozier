

import typing

from .get_links_tweetbot_request_url_only_one import GetLinksTweetbotRequestUrlOnlyOne
from .get_links_tweetbot_request_url_only_zero import GetLinksTweetbotRequestUrlOnlyZero

GetLinksTweetbotRequestUrlOnly = typing.Union[
    GetLinksTweetbotRequestUrlOnlyZero, GetLinksTweetbotRequestUrlOnlyOne, bool
]
