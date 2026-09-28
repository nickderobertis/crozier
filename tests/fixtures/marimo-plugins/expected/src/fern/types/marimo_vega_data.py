

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_vega_data_chart_selection import MarimoVegaDataChartSelection
from .marimo_vega_data_field_selection import MarimoVegaDataFieldSelection


class MarimoVegaData(UniversalBaseModel):
    spec: typing.Dict[str, typing.Any]
    chart_selection: typing_extensions.Annotated[
        typing.Optional[MarimoVegaDataChartSelection],
        FieldMetadata(alias="chartSelection"),
        pydantic.Field(alias="chartSelection"),
    ] = None
    field_selection: typing_extensions.Annotated[
        typing.Optional[MarimoVegaDataFieldSelection],
        FieldMetadata(alias="fieldSelection"),
        pydantic.Field(alias="fieldSelection"),
    ] = None
    embed_options: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="embedOptions"),
        pydantic.Field(alias="embedOptions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
