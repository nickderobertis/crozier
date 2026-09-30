

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chapter_completion_response_lessons_item import ChapterCompletionResponseLessonsItem


class ChapterCompletionResponse(UniversalBaseModel):
    lessons: typing.List[ChapterCompletionResponseLessonsItem] = pydantic.Field()
    """
    Completion status per lesson
    """

    percent_complete: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="percentComplete"),
        pydantic.Field(alias="percentComplete", description="Overall visible chapter completion percentage"),
    ] = None
    """
    Overall visible chapter completion percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
