

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chain_index import ChainIndex


class RescanResponse(UniversalBaseModel):
    start_index: typing_extensions.Annotated[
        ChainIndex, FieldMetadata(alias="startIndex"), pydantic.Field(alias="startIndex")
    ]
    index: ChainIndex
    start_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ]
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
