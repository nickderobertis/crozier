

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_info_v2status import ConnectionInfoV2Status
from .exposed_port import ExposedPort
from .room_id import RoomId


class ConnectionInfoV2(UniversalBaseModel):
    """
    Connection information for the default and additional ports.
    """

    additional_exposed_ports: typing_extensions.Annotated[
        typing.List[ExposedPort],
        FieldMetadata(alias="additionalExposedPorts"),
        pydantic.Field(alias="additionalExposedPorts"),
    ]
    exposed_port: typing_extensions.Annotated[
        typing.Optional[ExposedPort], FieldMetadata(alias="exposedPort"), pydantic.Field(alias="exposedPort")
    ] = None
    status: ConnectionInfoV2Status = pydantic.Field()
    """
    `exposedPort` will only be available when the `status` of a room is "active".
    """

    room_id: typing_extensions.Annotated[RoomId, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
