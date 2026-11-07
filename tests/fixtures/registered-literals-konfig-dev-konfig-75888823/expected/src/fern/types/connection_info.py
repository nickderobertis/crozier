

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .room_id import RoomId
from .transport_type import TransportType


class ConnectionInfo_Starting(UniversalBaseModel):
    """
    Connection information to the default port.
    """

    status: typing.Literal["starting"] = "starting"
    room_id: typing_extensions.Annotated[RoomId, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectionInfo_Active(UniversalBaseModel):
    """
    Connection information to the default port.
    """

    status: typing.Literal["active"] = "active"
    transport_type: typing_extensions.Annotated[
        TransportType, FieldMetadata(alias="transportType"), pydantic.Field(alias="transportType")
    ]
    port: float
    host: str
    room_id: typing_extensions.Annotated[RoomId, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConnectionInfo = typing_extensions.Annotated[
    typing.Union[ConnectionInfo_Starting, ConnectionInfo_Active], pydantic.Field(discriminator="status")
]
