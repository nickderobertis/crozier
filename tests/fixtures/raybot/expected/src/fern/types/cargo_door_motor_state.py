

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cargo_door_motor_state_direction import CargoDoorMotorStateDirection


class CargoDoorMotorState(UniversalBaseModel):
    direction: CargoDoorMotorStateDirection = pydantic.Field()
    """
    The direction of the cargo door motor
    """

    speed: int = pydantic.Field()
    """
    The speed of the cargo door motor
    """

    is_running: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isRunning"),
        pydantic.Field(alias="isRunning", description="Whether the cargo door motor is running"),
    ]
    """
    Whether the cargo door motor is running
    """

    enabled: bool = pydantic.Field()
    """
    Whether the cargo door motor is enabled
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the cargo door motor"),
    ]
    """
    The updated at time of the cargo door motor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
