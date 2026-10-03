

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardSettings(UniversalBaseModel):
    background_color: typing.Optional[str] = None
    border_color: typing.Optional[str] = None
    border_radius: typing.Optional[str] = None
    border_size: typing.Optional[str] = None
    color: typing.Optional[str] = None
    columns: typing.Optional[int] = None
    description_lines: typing.Optional[int] = None
    icon_border_radius: typing.Optional[str] = None
    icon_shadow_enabled: typing.Optional[bool] = None
    icon_size: typing.Optional[int] = None
    shadow_enabled: typing.Optional[bool] = None
    show_action: typing.Optional[bool] = None
    show_badges: typing.Optional[bool] = None
    show_category: typing.Optional[bool] = None
    show_description: typing.Optional[bool] = None
    style: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
