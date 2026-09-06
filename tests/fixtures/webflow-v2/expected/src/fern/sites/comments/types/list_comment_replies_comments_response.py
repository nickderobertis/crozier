

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_comment_replies_comments_response_comments_item import ListCommentRepliesCommentsResponseCommentsItem
from .list_comment_replies_comments_response_pagination import ListCommentRepliesCommentsResponsePagination


class ListCommentRepliesCommentsResponse(UniversalBaseModel):
    """
    A list of comment replies.
    """

    comments: typing.List[ListCommentRepliesCommentsResponseCommentsItem]
    pagination: ListCommentRepliesCommentsResponsePagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
