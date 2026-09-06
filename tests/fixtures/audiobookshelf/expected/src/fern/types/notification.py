

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_template import BodyTemplate
from .created_at import CreatedAt
from .enabled import Enabled
from .library_id_nullable import LibraryIdNullable
from .notification_event_name import NotificationEventName
from .notification_id import NotificationId
from .notification_type import NotificationType
from .title_template import TitleTemplate
from .urls import Urls


class Notification(UniversalBaseModel):
    id: typing.Optional[NotificationId] = None
    library_id: typing_extensions.Annotated[
        typing.Optional[LibraryIdNullable], FieldMetadata(alias="libraryId"), pydantic.Field(alias="libraryId")
    ] = None
    event_name: typing_extensions.Annotated[
        typing.Optional[NotificationEventName], FieldMetadata(alias="eventName"), pydantic.Field(alias="eventName")
    ] = None
    urls: typing.Optional[Urls] = None
    title_template: typing_extensions.Annotated[
        typing.Optional[TitleTemplate], FieldMetadata(alias="titleTemplate"), pydantic.Field(alias="titleTemplate")
    ] = None
    body_template: typing_extensions.Annotated[
        typing.Optional[BodyTemplate], FieldMetadata(alias="bodyTemplate"), pydantic.Field(alias="bodyTemplate")
    ] = None
    enabled: typing.Optional[Enabled] = None
    type: typing.Optional[NotificationType] = None
    last_fired_at: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastFiredAt"),
        pydantic.Field(
            alias="lastFiredAt",
            description="The time (in ms since POSIX epoch) when the notification was last fired. Will be null if the notification has not fired.",
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the notification was last fired. Will be null if the notification has not fired.
    """

    last_attempt_failed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="lastAttemptFailed"),
        pydantic.Field(alias="lastAttemptFailed", description="Whether the last notification attempt failed."),
    ] = None
    """
    Whether the last notification attempt failed.
    """

    num_consecutive_failed_attempts: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numConsecutiveFailedAttempts"),
        pydantic.Field(
            alias="numConsecutiveFailedAttempts",
            description="The number of consecutive times the notification has failed.",
        ),
    ] = None
    """
    The number of consecutive times the notification has failed.
    """

    num_times_fired: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numTimesFired"),
        pydantic.Field(alias="numTimesFired", description="The number of times the notification has fired."),
    ] = None
    """
    The number of times the notification has fired.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[CreatedAt], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
