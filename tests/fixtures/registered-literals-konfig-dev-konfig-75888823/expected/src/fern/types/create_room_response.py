

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .connection_info_v2 import ConnectionInfoV2
from .process_id import ProcessId


class CreateRoomResponse(ConnectionInfoV2):
    process_id: typing_extensions.Annotated[
        ProcessId, FieldMetadata(alias="processId"), pydantic.Field(alias="processId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
