

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_style_font_size_unit import TextStyleFontSizeUnit


class TextStyle(UniversalBaseModel):
    font_family: typing.Optional[str] = None
    font_size: typing.Optional[float] = None
    font_size_unit: typing.Optional[TextStyleFontSizeUnit] = None
    font_weight: typing.Optional[int] = None
    bold: typing.Optional[bool] = None
    italic: typing.Optional[bool] = None
    underline: typing.Optional[bool] = None
    strikethrough: typing.Optional[bool] = None
    handwritten: typing.Optional[bool] = None
    monospace: typing.Optional[bool] = None
    small_caps: typing.Optional[bool] = None
    superscript: typing.Optional[bool] = None
    subscript: typing.Optional[bool] = None
    foreground_color: typing.Optional[str] = None
    background_color: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
