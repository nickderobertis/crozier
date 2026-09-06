

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .create_comment_reply_comments_response_author import CreateCommentReplyCommentsResponseAuthor
from .create_comment_reply_comments_response_mentioned_users_item import (
    CreateCommentReplyCommentsResponseMentionedUsersItem,
)


class CreateCommentReplyCommentsResponse(UniversalBaseModel):
    """
    A comment thread represents a conversation between users on a specific page. Each comment thread has a unique identifier and can contain multiple comments.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the comment thread
    """

    comment_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="commentId"),
        pydantic.Field(alias="commentId", description="The comment reply unique identifier"),
    ]
    """
    The comment reply unique identifier
    """

    site_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="siteId"), pydantic.Field(alias="siteId", description="The site unique identifier")
    ]
    """
    The site unique identifier
    """

    page_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="pageId"), pydantic.Field(alias="pageId", description="The page unique identifier")
    ]
    """
    The page unique identifier
    """

    locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localeId"),
        pydantic.Field(alias="localeId", description="The locale unique identifier"),
    ] = None
    """
    The locale unique identifier
    """

    breakpoint: str = pydantic.Field()
    """
    The breakpoint the comment was left on
    """

    content: str = pydantic.Field()
    """
    The content of the comment reply
    """

    is_resolved: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isResolved"),
        pydantic.Field(alias="isResolved", description="Boolean determining if the comment thread is resolved"),
    ]
    """
    Boolean determining if the comment thread is resolved
    """

    author: CreateCommentReplyCommentsResponseAuthor
    mentioned_users: typing_extensions.Annotated[
        typing.Optional[typing.List[CreateCommentReplyCommentsResponseMentionedUsersItem]],
        FieldMetadata(alias="mentionedUsers"),
        pydantic.Field(
            alias="mentionedUsers",
            description="List of mentioned users is an empty array until email notifications are sent.",
        ),
    ] = None
    """
    List of mentioned users is an empty array until email notifications are sent.
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the item was last updated"),
    ] = None
    """
    The date the item was last updated
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the item was created"),
    ] = None
    """
    The date the item was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
