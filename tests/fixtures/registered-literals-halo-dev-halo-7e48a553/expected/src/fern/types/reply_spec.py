

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .comment_owner import CommentOwner


class ReplySpec(UniversalBaseModel):
    """
    Desired state of a reply.
    """

    allow_notification: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="allowNotification"),
        pydantic.Field(
            alias="allowNotification",
            description="Whether notification subscriptions should be created for this comment or reply.",
        ),
    ]
    """
    Whether notification subscriptions should be created for this comment or reply.
    """

    approved: bool = pydantic.Field()
    """
    Whether the comment has passed moderation and may be visible.
    """

    approved_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="approvedTime"),
        pydantic.Field(alias="approvedTime", description="Time when the comment was approved."),
    ] = None
    """
    Time when the comment was approved.
    """

    comment_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="commentName"),
        pydantic.Field(alias="commentName", description="Parent Comment metadata.name."),
    ]
    """
    Parent Comment metadata.name.
    """

    content: str = pydantic.Field()
    """
    Rendered HTML content displayed to REST and theme consumers.
    """

    creation_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationTime"),
        pydantic.Field(
            alias="creationTime",
            description="Creation time supplied by the caller. If absent, metadata.creationTimestamp is used.",
        ),
    ] = None
    """
    Creation time supplied by the caller. If absent, metadata.creationTimestamp is used.
    """

    hidden: bool = pydantic.Field()
    """
    Whether the comment should be hidden from public REST and theme output.
    """

    ip_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ipAddress"),
        pydantic.Field(alias="ipAddress", description="IP address recorded when the comment was submitted."),
    ] = None
    """
    IP address recorded when the comment was submitted.
    """

    owner: CommentOwner
    priority: int = pydantic.Field()
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    quote_reply: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="quoteReply"),
        pydantic.Field(
            alias="quoteReply", description="Quoted Reply metadata.name when this reply responds to another reply."
        ),
    ] = None
    """
    Quoted Reply metadata.name when this reply responds to another reply.
    """

    raw: str = pydantic.Field()
    """
    Raw comment body submitted by the owner before HTML sanitization and rendering.
    """

    top: bool = pydantic.Field()
    """
    Whether the comment is pinned above normal comment ordering.
    """

    user_agent: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userAgent"),
        pydantic.Field(alias="userAgent", description="Browser user agent recorded when the comment was submitted."),
    ] = None
    """
    Browser user agent recorded when the comment was submitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
