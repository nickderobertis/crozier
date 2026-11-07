

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .comment_stats import CommentStats
from .owner_info import OwnerInfo
from .reply import Reply


class ListedReply(UniversalBaseModel):
    """
    Reply list item with resolved owner and counters.
    """

    owner: OwnerInfo
    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Frontend permalink to this reply, when its subject URL is available.
    """

    reply: Reply
    stats: CommentStats

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
