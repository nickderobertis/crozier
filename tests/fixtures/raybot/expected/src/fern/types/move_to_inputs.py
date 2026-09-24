

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .motor_speed import MotorSpeed
from .move_direction import MoveDirection


class MoveToInputs(UniversalBaseModel):
    location: str = pydantic.Field()
    """
    The location to move to
    """

    direction: MoveDirection = pydantic.Field()
    """
    The direction when moving
    """

    motor_speed: typing_extensions.Annotated[
        MotorSpeed, FieldMetadata(alias="motorSpeed"), pydantic.Field(alias="motorSpeed")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
