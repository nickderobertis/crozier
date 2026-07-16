

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .customerio_notification_configuration import CustomerioNotificationConfiguration
from .notification_type import NotificationType
from .slack_notification_configuration import SlackNotificationConfiguration


class Notification(UniversalBaseModel):
    customerio_configuration: typing_extensions.Annotated[
        typing.Optional[CustomerioNotificationConfiguration],
        FieldMetadata(alias="customerioConfiguration"),
        pydantic.Field(alias="customerioConfiguration"),
    ] = None
    notification_type: typing_extensions.Annotated[
        NotificationType, FieldMetadata(alias="notificationType"), pydantic.Field(alias="notificationType")
    ]
    send_on_failure: typing_extensions.Annotated[
        bool, FieldMetadata(alias="sendOnFailure"), pydantic.Field(alias="sendOnFailure")
    ]
    send_on_success: typing_extensions.Annotated[
        bool, FieldMetadata(alias="sendOnSuccess"), pydantic.Field(alias="sendOnSuccess")
    ]
    slack_configuration: typing_extensions.Annotated[
        typing.Optional[SlackNotificationConfiguration],
        FieldMetadata(alias="slackConfiguration"),
        pydantic.Field(alias="slackConfiguration"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
