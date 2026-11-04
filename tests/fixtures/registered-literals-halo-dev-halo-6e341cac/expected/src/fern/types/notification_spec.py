

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NotificationSpec(UniversalBaseModel):
    """
    Notification content and read state for one recipient.
    """

    html_content: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="htmlContent"),
        pydantic.Field(alias="htmlContent", description="HTML notification content."),
    ]
    """
    HTML notification content.
    """

    last_read_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastReadAt"),
        pydantic.Field(alias="lastReadAt", description="Last time the recipient marked this notification as read."),
    ] = None
    """
    Last time the recipient marked this notification as read.
    """

    raw_content: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rawContent"),
        pydantic.Field(alias="rawContent", description="Plain text or source notification content."),
    ]
    """
    Plain text or source notification content.
    """

    reason: str = pydantic.Field()
    """
    Reason metadata.name that generated this notification.
    """

    recipient: str = pydantic.Field()
    """
    User metadata.name that receives the notification.
    """

    title: str = pydantic.Field()
    """
    Notification title shown in the notification center.
    """

    unread: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the recipient has not read the notification yet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
