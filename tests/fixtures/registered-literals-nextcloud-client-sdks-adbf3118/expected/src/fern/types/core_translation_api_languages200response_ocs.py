

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_translation_api_languages200response_ocs_data import CoreTranslationApiLanguages200ResponseOcsData
from .ocs_meta import OcsMeta


class CoreTranslationApiLanguages200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: CoreTranslationApiLanguages200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
