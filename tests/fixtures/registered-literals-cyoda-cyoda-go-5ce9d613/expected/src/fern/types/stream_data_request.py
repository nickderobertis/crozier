

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_data_def import StreamDataDef


class StreamDataRequest(UniversalBaseModel):
    sd_def: typing_extensions.Annotated[
        typing.Optional[StreamDataDef], FieldMetadata(alias="sdDef"), pydantic.Field(alias="sdDef")
    ] = None
    point_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pointTime"), pydantic.Field(alias="pointTime")
    ] = None
    offset: typing.Optional[int] = None
    length: typing.Optional[int] = None
    from_pos_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fromPosIndex"), pydantic.Field(alias="fromPosIndex")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
