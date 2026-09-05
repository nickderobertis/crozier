

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Stats(UniversalBaseModel):
    cpu_usage: typing_extensions.Annotated[float, FieldMetadata(alias="cpuUsage"), pydantic.Field(alias="cpuUsage")]
    mem_usage: typing_extensions.Annotated[float, FieldMetadata(alias="memUsage"), pydantic.Field(alias="memUsage")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
