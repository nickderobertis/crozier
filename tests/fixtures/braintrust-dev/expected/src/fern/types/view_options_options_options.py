

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .view_options_options_options_span_type import ViewOptionsOptionsOptionsSpanType
from .view_options_options_options_type import ViewOptionsOptionsOptionsType


class ViewOptionsOptionsOptions(UniversalBaseModel):
    span_type: typing_extensions.Annotated[
        typing.Optional[ViewOptionsOptionsOptionsSpanType],
        FieldMetadata(alias="spanType"),
        pydantic.Field(alias="spanType"),
    ] = None
    range_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rangeValue"), pydantic.Field(alias="rangeValue")
    ] = None
    frame_start: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="frameStart"), pydantic.Field(alias="frameStart")
    ] = None
    frame_end: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="frameEnd"), pydantic.Field(alias="frameEnd")
    ] = None
    tz_utc: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tzUTC"), pydantic.Field(alias="tzUTC")
    ] = None
    chart_visibility: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[bool]]],
        FieldMetadata(alias="chartVisibility"),
        pydantic.Field(alias="chartVisibility"),
    ] = None
    project_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")
    ] = None
    type: typing.Optional[ViewOptionsOptionsOptionsType] = None
    group_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupBy"), pydantic.Field(alias="groupBy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
