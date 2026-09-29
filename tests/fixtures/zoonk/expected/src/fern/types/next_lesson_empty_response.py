

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NextLessonEmptyResponse(UniversalBaseModel):
    completed: bool = pydantic.Field()
    """
    Whether all lessons are completed
    """

    has_started: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasStarted"),
        pydantic.Field(alias="hasStarted", description="Whether the user has started"),
    ]
    """
    Whether the user has started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
