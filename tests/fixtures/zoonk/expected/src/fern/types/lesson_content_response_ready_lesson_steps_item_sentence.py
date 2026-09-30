

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonContentResponseReadyLessonStepsItemSentence(UniversalBaseModel):
    audio_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioUrl"), pydantic.Field(alias="audioUrl")
    ] = None
    distractors: typing.List[str]
    explanation: typing.Optional[str] = None
    id: str
    romanization: typing.Optional[str] = None
    sentence: str
    translation: str
    translation_distractors: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="translationDistractors"), pydantic.Field(alias="translationDistractors")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
