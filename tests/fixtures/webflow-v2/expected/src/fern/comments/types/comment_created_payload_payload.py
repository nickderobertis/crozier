

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .comment_created_payload_payload_author import CommentCreatedPayloadPayloadAuthor
from .comment_created_payload_payload_mentioned_users_item import CommentCreatedPayloadPayloadMentionedUsersItem
from .comment_created_payload_payload_type import CommentCreatedPayloadPayloadType


class CommentCreatedPayloadPayload(UniversalBaseModel):
    """
    The comment webhook payload contains data for the thread and for replies.  Check the type to determine if the payload is for a thread or a reply.  The webhook payload may be delayed by up to 5 minutes.
    """

    thread_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="threadId"),
        pydantic.Field(alias="threadId", description="Unique identifier for the comment thread"),
    ] = None
    """
    Unique identifier for the comment thread
    """

    comment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="commentId"),
        pydantic.Field(alias="commentId", description="Unique identifier for the comment reply"),
    ] = None
    """
    Unique identifier for the comment reply
    """

    type: typing.Optional[CommentCreatedPayloadPayloadType] = pydantic.Field(default=None)
    """
    The type of comment payload. `new_comment` indicates a new thread; `reply` indicates a reply to an existing thread.
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The site unique identifier"),
    ] = None
    """
    The site unique identifier
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageId"),
        pydantic.Field(
            alias="pageId", description="The page unique identifier, or for CMS item comments, the template page ID"
        ),
    ] = None
    """
    The page unique identifier, or for CMS item comments, the template page ID
    """

    locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localeId"),
        pydantic.Field(alias="localeId", description="The locale unique identifier"),
    ] = None
    """
    The locale unique identifier
    """

    breakpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The breakpoint the comment was left on
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the page the comment was left on
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

    author: CommentCreatedPayloadPayloadAuthor
    mentioned_users: typing_extensions.Annotated[
        typing.List[CommentCreatedPayloadPayloadMentionedUsersItem],
        FieldMetadata(alias="mentionedUsers"),
        pydantic.Field(
            alias="mentionedUsers",
            description="List of mentioned users. This is an empty array until email notifications are sent, which can take up to 5 minutes after the comment is created.",
        ),
    ]
    """
    List of mentioned users. This is an empty array until email notifications are sent, which can take up to 5 minutes after the comment is created.
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the item was created"),
    ] = None
    """
    The date the item was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the item was last updated"),
    ] = None
    """
    The date the item was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
