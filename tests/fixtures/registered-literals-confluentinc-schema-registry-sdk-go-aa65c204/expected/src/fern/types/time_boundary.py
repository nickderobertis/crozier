

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeBoundary(UniversalBaseModel):
    start_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    end_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endTime"), pydantic.Field(alias="endTime")
    ] = None
    time_zone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="timeZone"), pydantic.Field(alias="timeZone")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
