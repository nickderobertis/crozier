

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_preference_stage_name import NotificationPreferenceStageName


class NotificationPreference(UniversalBaseModel):
    """
    Notification preference for a job stage.
    """

    send_notification: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="sendNotification"),
        pydantic.Field(alias="sendNotification", description="Notification is required or not."),
    ]
    """
    Notification is required or not.
    """

    stage_name: typing_extensions.Annotated[
        NotificationPreferenceStageName,
        FieldMetadata(alias="stageName"),
        pydantic.Field(alias="stageName", description="Name of the stage."),
    ]
    """
    Name of the stage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
