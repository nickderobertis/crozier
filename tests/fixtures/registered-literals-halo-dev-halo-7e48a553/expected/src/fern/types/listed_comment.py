

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .comment import Comment
from .comment_stats import CommentStats
from .extension import Extension
from .owner_info import OwnerInfo


class ListedComment(UniversalBaseModel):
    """
    Comment list item with resolved owner, subject, and counters.
    """

    comment: Comment
    owner: OwnerInfo
    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Frontend permalink to this comment, when its subject URL is available.
    """

    stats: CommentStats
    subject: typing.Optional[Extension] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
