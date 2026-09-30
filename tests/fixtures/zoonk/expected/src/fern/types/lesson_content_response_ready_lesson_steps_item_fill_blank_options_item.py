

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem(UniversalBaseModel):
    audio_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioUrl"), pydantic.Field(alias="audioUrl")
    ] = None
    pronunciation: typing.Optional[str] = None
    romanization: typing.Optional[str] = None
    translation: typing.Optional[str] = None
    word: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
