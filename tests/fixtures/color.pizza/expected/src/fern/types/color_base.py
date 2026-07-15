

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .color_base_hsl import ColorBaseHsl
from .color_base_lab import ColorBaseLab
from .color_base_rgb import ColorBaseRgb
from .color_base_swatch_img import ColorBaseSwatchImg


class ColorBase(UniversalBaseModel):
    hex: typing.Optional[str] = None
    hsl: typing.Optional[ColorBaseHsl] = None
    lab: typing.Optional[ColorBaseLab] = None
    luminance: typing.Optional[float] = None
    luminance_wcag: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="luminanceWCAG")] = None
    name: typing.Optional[str] = None
    rgb: typing.Optional[ColorBaseRgb] = None
    swatch_img: typing_extensions.Annotated[typing.Optional[ColorBaseSwatchImg], FieldMetadata(alias="swatchImg")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
