

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .process_id import ProcessId
from .room_allocation_id import RoomAllocationId


class RoomAllocation(UniversalBaseModel):
    """
    Metadata on an allocated instance of a room.
    """

    unscheduled_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="unscheduledAt"), pydantic.Field(alias="unscheduledAt")
    ] = None
    scheduled_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="scheduledAt"), pydantic.Field(alias="scheduledAt")
    ]
    process_id: typing_extensions.Annotated[
        ProcessId, FieldMetadata(alias="processId"), pydantic.Field(alias="processId")
    ]
    room_allocation_id: typing_extensions.Annotated[
        RoomAllocationId, FieldMetadata(alias="roomAllocationId"), pydantic.Field(alias="roomAllocationId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
