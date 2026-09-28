

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_matplotlib_data_x_scale import MarimoMatplotlibDataXScale
from .marimo_matplotlib_data_y_scale import MarimoMatplotlibDataYScale


class MarimoMatplotlibData(UniversalBaseModel):
    chart_base64: typing_extensions.Annotated[
        str, FieldMetadata(alias="chartBase64"), pydantic.Field(alias="chartBase64")
    ]
    x_bounds: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="xBounds"), pydantic.Field(alias="xBounds")
    ]
    y_bounds: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="yBounds"), pydantic.Field(alias="yBounds")
    ]
    axes_pixel_bounds: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="axesPixelBounds"), pydantic.Field(alias="axesPixelBounds")
    ]
    width: float
    height: float
    selection_color: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selectionColor"), pydantic.Field(alias="selectionColor")
    ] = None
    selection_opacity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="selectionOpacity"), pydantic.Field(alias="selectionOpacity")
    ] = None
    stroke_width: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ] = None
    debounce: bool
    x_scale: typing_extensions.Annotated[
        typing.Optional[MarimoMatplotlibDataXScale], FieldMetadata(alias="xScale"), pydantic.Field(alias="xScale")
    ] = None
    y_scale: typing_extensions.Annotated[
        typing.Optional[MarimoMatplotlibDataYScale], FieldMetadata(alias="yScale"), pydantic.Field(alias="yScale")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
