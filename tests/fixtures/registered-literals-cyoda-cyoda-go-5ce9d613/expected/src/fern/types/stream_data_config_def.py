

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_data_def import StreamDataDef


class StreamDataConfigDef(UniversalBaseModel):
    stream_data_def: typing_extensions.Annotated[
        typing.Optional[StreamDataDef], FieldMetadata(alias="streamDataDef"), pydantic.Field(alias="streamDataDef")
    ] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    create_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ] = None
    owner: typing.Optional[str] = None
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
