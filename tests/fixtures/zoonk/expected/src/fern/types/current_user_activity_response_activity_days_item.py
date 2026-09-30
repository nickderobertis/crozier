

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CurrentUserActivityResponseActivityDaysItem(UniversalBaseModel):
    date: dt.date = pydantic.Field()
    """
    Learner-local calendar date without a time or UTC offset
    """

    lesson_completions: typing_extensions.Annotated[
        int, FieldMetadata(alias="lessonCompletions"), pydantic.Field(alias="lessonCompletions")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
