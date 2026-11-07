

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_active_query_query import GetActiveQueryQuery


class GetActiveQuery(UniversalBaseModel):
    pid: typing.Optional[int] = None
    query: typing.Optional[GetActiveQueryQuery] = None
    start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    elapsed: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
