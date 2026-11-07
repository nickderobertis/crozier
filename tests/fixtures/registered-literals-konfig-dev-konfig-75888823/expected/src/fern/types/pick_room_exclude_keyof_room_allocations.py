

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .room_allocation import RoomAllocation
from .room_config import RoomConfig
from .room_id import RoomId
from .room_status import RoomStatus


class PickRoomExcludeKeyofRoomAllocations(UniversalBaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """

    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]
    room_id: typing_extensions.Annotated[RoomId, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]
    room_config: typing_extensions.Annotated[
        typing.Optional[RoomConfig], FieldMetadata(alias="roomConfig"), pydantic.Field(alias="roomConfig")
    ] = None
    status: RoomStatus
    current_allocation: typing_extensions.Annotated[
        typing.Optional[RoomAllocation],
        FieldMetadata(alias="currentAllocation"),
        pydantic.Field(alias="currentAllocation"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
