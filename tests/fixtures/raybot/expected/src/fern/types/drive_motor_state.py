

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .drive_motor_state_direction import DriveMotorStateDirection


class DriveMotorState(UniversalBaseModel):
    direction: DriveMotorStateDirection = pydantic.Field()
    """
    The direction of the drive motor
    """

    speed: int = pydantic.Field()
    """
    The speed of the drive motor (0-100)
    """

    is_running: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isRunning"),
        pydantic.Field(alias="isRunning", description="Whether the drive motor is running"),
    ]
    """
    Whether the drive motor is running
    """

    enabled: bool = pydantic.Field()
    """
    Whether the drive motor is enabled
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the drive motor"),
    ]
    """
    The updated at time of the drive motor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
