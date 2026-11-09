

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .process import Process
from .room_without_allocations import RoomWithoutAllocations


class ProcessWithRooms(Process):
    rooms: typing.List[RoomWithoutAllocations]
    total_rooms: typing_extensions.Annotated[int, FieldMetadata(alias="totalRooms"), pydantic.Field(alias="totalRooms")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
