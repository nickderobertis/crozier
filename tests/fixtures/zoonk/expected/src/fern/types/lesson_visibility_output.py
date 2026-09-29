

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_visibility_output_hidden_lesson_kinds_item import LessonVisibilityOutputHiddenLessonKindsItem


class LessonVisibilityOutput(UniversalBaseModel):
    hidden_lesson_kinds: typing_extensions.Annotated[
        typing.List[LessonVisibilityOutputHiddenLessonKindsItem],
        FieldMetadata(alias="hiddenLessonKinds"),
        pydantic.Field(alias="hiddenLessonKinds"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
