

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_completion_response_belt import LessonCompletionResponseBelt


class LessonCompletionResponse(UniversalBaseModel):
    belt: LessonCompletionResponseBelt
    brain_power: typing_extensions.Annotated[
        float, FieldMetadata(alias="brainPower"), pydantic.Field(alias="brainPower")
    ]
    correct_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="correctCount"), pydantic.Field(alias="correctCount")
    ]
    energy_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="energyDelta"), pydantic.Field(alias="energyDelta")
    ]
    incorrect_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="incorrectCount"), pydantic.Field(alias="incorrectCount")
    ]
    new_total_bp: typing_extensions.Annotated[
        float, FieldMetadata(alias="newTotalBp"), pydantic.Field(alias="newTotalBp")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
