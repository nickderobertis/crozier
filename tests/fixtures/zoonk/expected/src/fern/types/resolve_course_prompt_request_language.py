

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resolve_course_prompt_request_language_target_language import ResolveCoursePromptRequestLanguageTargetLanguage


class ResolveCoursePromptRequestLanguage(UniversalBaseModel):
    language: str = pydantic.Field()
    """
    Well-formed BCP 47 source locale
    """

    target_language: typing_extensions.Annotated[
        ResolveCoursePromptRequestLanguageTargetLanguage,
        FieldMetadata(alias="targetLanguage"),
        pydantic.Field(
            alias="targetLanguage", description="Target language, which must differ from the source language"
        ),
    ]
    """
    Target language, which must differ from the source language
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
