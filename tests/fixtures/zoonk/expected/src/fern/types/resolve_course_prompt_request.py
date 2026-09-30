

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resolve_course_prompt_request_language_target_language import ResolveCoursePromptRequestLanguageTargetLanguage


class ResolveCoursePromptRequest_Topic(UniversalBaseModel):
    kind: typing.Literal["topic"] = "topic"
    language: str
    prompt: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptRequest_Language(UniversalBaseModel):
    kind: typing.Literal["language"] = "language"
    language: str
    target_language: typing_extensions.Annotated[
        ResolveCoursePromptRequestLanguageTargetLanguage,
        FieldMetadata(alias="targetLanguage"),
        pydantic.Field(alias="targetLanguage"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResolveCoursePromptRequest = typing_extensions.Annotated[
    typing.Union[ResolveCoursePromptRequest_Topic, ResolveCoursePromptRequest_Language],
    pydantic.Field(discriminator="kind"),
]
