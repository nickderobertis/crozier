

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_event_defaults import NotificationEventDefaults


class NotificationEvent(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the notification event. The names and allowable values are defined at https://github.com/advplyr/audiobookshelf/blob/master/server/utils/notifications.js
    """

    requires_library: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requiresLibrary"),
        pydantic.Field(
            alias="requiresLibrary", description="Whether the notification event depends on a library existing."
        ),
    ] = None
    """
    Whether the notification event depends on a library existing.
    """

    library_media_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="libraryMediaType"),
        pydantic.Field(
            alias="libraryMediaType",
            description="The type of media of the library the notification depends on existing. Will not exist if requiresLibrary is false.",
        ),
    ] = None
    """
    The type of media of the library the notification depends on existing. Will not exist if requiresLibrary is false.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the notification event.
    """

    variables: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The variables of the notification event that can be used in the notification templates.
    """

    defaults: typing.Optional[NotificationEventDefaults] = None
    test_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="testData"),
        pydantic.Field(
            alias="testData",
            description="The keys of the testData object will match the list of variables. The values will be the data used when sending a test notification.",
        ),
    ] = None
    """
    The keys of the testData object will match the list of variables. The values will be the data used when sending a test notification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
