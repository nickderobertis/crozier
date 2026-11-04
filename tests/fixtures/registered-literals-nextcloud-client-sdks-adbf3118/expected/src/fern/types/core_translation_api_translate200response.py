

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_translation_api_translate200response_ocs import CoreTranslationApiTranslate200ResponseOcs


class CoreTranslationApiTranslate200Response(UniversalBaseModel):
    ocs: CoreTranslationApiTranslate200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
