

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .http_template_response_modifier_cookies import HttpTemplateResponseModifierCookies
from .http_template_response_modifier_headers import HttpTemplateResponseModifierHeaders


class HttpTemplateResponseModifier(UniversalBaseModel):
    headers: typing.Optional[HttpTemplateResponseModifierHeaders] = None
    cookies: typing.Optional[HttpTemplateResponseModifierCookies] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
