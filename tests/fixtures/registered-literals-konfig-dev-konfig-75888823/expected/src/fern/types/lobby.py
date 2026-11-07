

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .lobby_initial_config import LobbyInitialConfig
from .lobby_visibility import LobbyVisibility
from .region import Region
from .room_id import RoomId
from .short_code import ShortCode


class Lobby(UniversalBaseModel):
    """
    A lobby object allows you to store and manage metadata for your rooms.
    """

    short_code: typing_extensions.Annotated[
        typing.Optional[ShortCode], FieldMetadata(alias="shortCode"), pydantic.Field(alias="shortCode")
    ] = None
    state: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON blob to store metadata for a room. Must be smaller than 1MB.
    """

    initial_config: typing_extensions.Annotated[
        LobbyInitialConfig, FieldMetadata(alias="initialConfig"), pydantic.Field(alias="initialConfig")
    ]
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

    local: bool
    visibility: LobbyVisibility
    region: Region
    room_id: typing_extensions.Annotated[RoomId, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]
    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
