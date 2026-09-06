

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_comment_threads_comments_response_comments_item import ListCommentThreadsCommentsResponseCommentsItem
from .list_comment_threads_comments_response_pagination import ListCommentThreadsCommentsResponsePagination


class ListCommentThreadsCommentsResponse(UniversalBaseModel):
    """
    A list of comment threads on the site. Contains the content of the first reply.
    """

    comments: typing.List[ListCommentThreadsCommentsResponseCommentsItem]
    pagination: ListCommentThreadsCommentsResponsePagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
