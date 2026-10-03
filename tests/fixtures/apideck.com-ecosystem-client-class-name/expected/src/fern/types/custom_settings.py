

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomSettings(UniversalBaseModel):
    css: typing.Optional[str] = None
    css_link: typing.Optional[str] = None
    domain: typing.Optional[str] = None
    html_footer: typing.Optional[str] = None
    html_nav: typing.Optional[str] = None
    java_script_link: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
