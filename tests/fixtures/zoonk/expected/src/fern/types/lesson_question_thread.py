

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_question import LessonQuestion


class LessonQuestionThread(UniversalBaseModel):
    has_more: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasMore"),
        pydantic.Field(alias="hasMore", description="Whether an earlier page exists"),
    ]
    """
    Whether an earlier page exists
    """

    id: str
    lesson_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lessonId"), pydantic.Field(alias="lessonId")
    ] = None
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(alias="nextCursor", description="Opaque cursor for the earlier page"),
    ] = None
    """
    Opaque cursor for the earlier page
    """

    questions: typing.List[LessonQuestion]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
