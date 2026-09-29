

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonQuestionContextInputStep(UniversalBaseModel):
    step_id: typing_extensions.Annotated[str, FieldMetadata(alias="stepId"), pydantic.Field(alias="stepId")]
    step_number: typing_extensions.Annotated[int, FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
