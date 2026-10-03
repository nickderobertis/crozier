

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CtaSettings(UniversalBaseModel):
    background_color: typing.Optional[str] = None
    button_background_color: typing.Optional[str] = None
    button_color: typing.Optional[str] = None
    button_label: typing.Optional[str] = None
    button_link: typing.Optional[str] = None
    color: typing.Optional[str] = None
    description: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
