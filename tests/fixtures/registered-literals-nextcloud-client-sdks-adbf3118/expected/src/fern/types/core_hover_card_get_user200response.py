

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_hover_card_get_user200response_ocs import CoreHoverCardGetUser200ResponseOcs


class CoreHoverCardGetUser200Response(UniversalBaseModel):
    ocs: CoreHoverCardGetUser200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
