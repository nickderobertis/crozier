

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_translation_api_languages200response_ocs_data_languages_inner import (
    CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner,
)


class CoreTranslationApiLanguages200ResponseOcsData(UniversalBaseModel):
    languages: typing.List[CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner]
    language_detection: typing_extensions.Annotated[
        bool, FieldMetadata(alias="languageDetection"), pydantic.Field(alias="languageDetection")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
