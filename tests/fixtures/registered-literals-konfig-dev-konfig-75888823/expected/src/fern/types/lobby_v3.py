

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .lobby_visibility import LobbyVisibility
from .region import Region
from .room_config import RoomConfig
from .room_id import RoomId
from .short_code import ShortCode


class LobbyV3(UniversalBaseModel):
    """
    A lobby object allows you to store and manage metadata for your rooms.
    """

    short_code: typing_extensions.Annotated[
        ShortCode,
        FieldMetadata(alias="shortCode"),
        pydantic.Field(alias="shortCode", description="User defined identifier for a lobby, defaults to `roomId`"),
    ]
    """
    User defined identifier for a lobby, defaults to `roomId`
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the lobby was created."),
    ]
    """
    When the lobby was created.
    """

    created_by: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="UserId or email address for the user that created the lobby."),
    ]
    """
    UserId or email address for the user that created the lobby.
    """

    room_config: typing_extensions.Annotated[
        typing.Optional[RoomConfig], FieldMetadata(alias="roomConfig"), pydantic.Field(alias="roomConfig")
    ] = None
    visibility: LobbyVisibility
    region: Region
    room_id: typing_extensions.Annotated[
        RoomId,
        FieldMetadata(alias="roomId"),
        pydantic.Field(
            alias="roomId",
            description="Hathora generated identifier for a room, unique for a given application (including stopped rooms)",
        ),
    ]
    """
    Hathora generated identifier for a room, unique for a given application (including stopped rooms)
    """

    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
