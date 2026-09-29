

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class LessonCompletionRequestStepTimingsValue(UniversalBaseModel):
    answered_at: typing_extensions.Annotated[
        float, FieldMetadata(alias="answeredAt"), pydantic.Field(alias="answeredAt")
    ]
    day_of_week: typing_extensions.Annotated[int, FieldMetadata(alias="dayOfWeek"), pydantic.Field(alias="dayOfWeek")]
    duration_seconds: typing_extensions.Annotated[
        float, FieldMetadata(alias="durationSeconds"), pydantic.Field(alias="durationSeconds")
    ]
    hour_of_day: typing_extensions.Annotated[int, FieldMetadata(alias="hourOfDay"), pydantic.Field(alias="hourOfDay")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
