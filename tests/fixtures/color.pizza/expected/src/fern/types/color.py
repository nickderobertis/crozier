

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .color_hsl import ColorHsl
from .color_lab import ColorLab
from .color_rgb import ColorRgb


class Color(UniversalBaseModel):
    distance: typing.Optional[float] = None
    hex: typing.Optional[str] = None
    hsl: typing.Optional[ColorHsl] = None
    lab: typing.Optional[ColorLab] = None
    luminance: typing.Optional[float] = None
    luminance_wcag: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="luminanceWCAG")] = None
    name: typing.Optional[str] = None
    requested_hex: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestedHex")] = None
    rgb: typing.Optional[ColorRgb] = None
    svg: typing.Optional[str] = None
    svg_named: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="svgNamed")] = None
    swatch_img: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="swatchImg")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
