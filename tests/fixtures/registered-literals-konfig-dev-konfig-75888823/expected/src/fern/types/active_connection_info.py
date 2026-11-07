

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .room_id import RoomId
from .transport_type import TransportType


class ActiveConnectionInfo(UniversalBaseModel):
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
