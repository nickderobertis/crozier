

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .course_completion_response_chapters_item import CourseCompletionResponseChaptersItem


class CourseCompletionResponse(UniversalBaseModel):
    chapters: typing.List[CourseCompletionResponseChaptersItem] = pydantic.Field()
    """
    Completion status per chapter
    """

    percent_complete: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="percentComplete"),
        pydantic.Field(alias="percentComplete", description="Overall visible course completion percentage"),
    ] = None
    """
    Overall visible course completion percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
