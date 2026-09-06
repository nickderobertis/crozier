

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .apprise_api_url import AppriseApiUrl
from .max_failed_attempts import MaxFailedAttempts
from .max_notification_queue import MaxNotificationQueue
from .notification import Notification
from .notification_id import NotificationId


class NotificationSettings(UniversalBaseModel):
    id: typing.Optional[NotificationId] = None
    apprise_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appriseType"),
        pydantic.Field(
            alias="appriseType",
            description="The type of Apprise that will be used. At the moment, only api is available.",
        ),
    ] = None
    """
    The type of Apprise that will be used. At the moment, only api is available.
    """

    apprise_api_url: typing_extensions.Annotated[
        typing.Optional[AppriseApiUrl], FieldMetadata(alias="appriseApiUrl"), pydantic.Field(alias="appriseApiUrl")
    ] = None
    notifications: typing.Optional[typing.List[Notification]] = pydantic.Field(default=None)
    """
    The set notifications.
    """

    max_failed_attempts: typing_extensions.Annotated[
        typing.Optional[MaxFailedAttempts],
        FieldMetadata(alias="maxFailedAttempts"),
        pydantic.Field(alias="maxFailedAttempts"),
    ] = None
    max_notification_queue: typing_extensions.Annotated[
        typing.Optional[MaxNotificationQueue],
        FieldMetadata(alias="maxNotificationQueue"),
        pydantic.Field(alias="maxNotificationQueue"),
    ] = None
    notification_delay: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="notificationDelay"),
        pydantic.Field(alias="notificationDelay", description="The time (in ms) between notification pushes."),
    ] = None
    """
    The time (in ms) between notification pushes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
