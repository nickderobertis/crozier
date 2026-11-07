

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommentStatus(UniversalBaseModel):
    """
    Observed state of a top-level comment.
    """

    has_new_reply: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasNewReply"),
        pydantic.Field(alias="hasNewReply", description="Whether unreadReplyCount is greater than zero."),
    ] = None
    """
    Whether unreadReplyCount is greater than zero.
    """

    last_reply_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastReplyTime"),
        pydantic.Field(alias="lastReplyTime", description="Creation time of the latest reply under this comment."),
    ] = None
    """
    Creation time of the latest reply under this comment.
    """

    observed_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="observedVersion"),
        pydantic.Field(
            alias="observedVersion", description="Metadata version observed by the last successful reconciliation."
        ),
    ] = None
    """
    Metadata version observed by the last successful reconciliation.
    """

    pending_reply_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pendingReplyCount"),
        pydantic.Field(
            alias="pendingReplyCount", description="Total number of not yet approved replies under this comment."
        ),
    ] = None
    """
    Total number of not yet approved replies under this comment.
    """

    reply_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="replyCount"),
        pydantic.Field(alias="replyCount", description="Total number of replies under this comment."),
    ] = None
    """
    Total number of replies under this comment.
    """

    unread_reply_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unreadReplyCount"),
        pydantic.Field(
            alias="unreadReplyCount", description="Number of replies created after the comment owner's last read time."
        ),
    ] = None
    """
    Number of replies created after the comment owner's last read time.
    """

    visible_reply_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="visibleReplyCount"),
        pydantic.Field(
            alias="visibleReplyCount", description="Total number of approved and non-hidden replies under this comment."
        ),
    ] = None
    """
    Total number of approved and non-hidden replies under this comment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
