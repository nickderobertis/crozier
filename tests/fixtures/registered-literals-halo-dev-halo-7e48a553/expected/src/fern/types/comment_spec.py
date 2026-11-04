

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .comment_owner import CommentOwner
from .ref import Ref


class CommentSpec(UniversalBaseModel):
    """
    Desired state of a top-level comment.
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

    last_read_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastReadTime"),
        pydantic.Field(
            alias="lastReadTime", description="Latest time the comment owner has read replies for this comment."
        ),
    ] = None
    """
    Latest time the comment owner has read replies for this comment.
    """

    owner: CommentOwner
    priority: int = pydantic.Field()
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    raw: str = pydantic.Field()
    """
    Raw comment body submitted by the owner before HTML sanitization and rendering.
    """

    subject_ref: typing_extensions.Annotated[Ref, FieldMetadata(alias="subjectRef"), pydantic.Field(alias="subjectRef")]
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
