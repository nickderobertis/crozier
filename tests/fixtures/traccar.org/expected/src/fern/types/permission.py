

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Permission(UniversalBaseModel):
    """
    This is a permission map that contain two object indexes. It is used to link/unlink objects. Order is important. Example: { deviceId:8, geofenceId: 16 }
    """

    attribute_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="attributeId"),
        pydantic.Field(alias="attributeId", description="Computed Attribute Id, can be second parameter only"),
    ] = None
    """
    Computed Attribute Id, can be second parameter only
    """

    calendar_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="calendarId"),
        pydantic.Field(
            alias="calendarId",
            description="Calendar Id, can be second parameter only and only in combination with userId",
        ),
    ] = None
    """
    Calendar Id, can be second parameter only and only in combination with userId
    """

    device_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="deviceId"),
        pydantic.Field(
            alias="deviceId", description="Device Id, can be first parameter or second only in combination with userId"
        ),
    ] = None
    """
    Device Id, can be first parameter or second only in combination with userId
    """

    driver_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="driverId"),
        pydantic.Field(alias="driverId", description="Driver Id, can be second parameter only"),
    ] = None
    """
    Driver Id, can be second parameter only
    """

    geofence_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="geofenceId"),
        pydantic.Field(alias="geofenceId", description="Geofence Id, can be second parameter only"),
    ] = None
    """
    Geofence Id, can be second parameter only
    """

    group_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="groupId"),
        pydantic.Field(
            alias="groupId", description="Group Id, can be first parameter or second only in combination with userId"
        ),
    ] = None
    """
    Group Id, can be first parameter or second only in combination with userId
    """

    managed_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="managedUserId"),
        pydantic.Field(
            alias="managedUserId",
            description="User Id, can be second parameter only and only in combination with userId",
        ),
    ] = None
    """
    User Id, can be second parameter only and only in combination with userId
    """

    notification_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="notificationId"),
        pydantic.Field(alias="notificationId", description="Notification Id, can be second parameter only"),
    ] = None
    """
    Notification Id, can be second parameter only
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="User Id, can be only first parameter"),
    ] = None
    """
    User Id, can be only first parameter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
