

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_generation_target import LessonGenerationTarget


class LessonContentResponseNotGenerated(UniversalBaseModel):
    generation_target: typing_extensions.Annotated[
        typing.Optional[LessonGenerationTarget],
        FieldMetadata(alias="generationTarget"),
        pydantic.Field(alias="generationTarget"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
