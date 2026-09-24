

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LiftMotorState(UniversalBaseModel):
    current_position: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="currentPosition"),
        pydantic.Field(alias="currentPosition", description="The current position of the lift motor"),
    ]
    """
    The current position of the lift motor
    """

    target_position: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="targetPosition"),
        pydantic.Field(alias="targetPosition", description="The target position of the lift motor"),
    ]
    """
    The target position of the lift motor
    """

    is_running: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isRunning"),
        pydantic.Field(alias="isRunning", description="Whether the lift motor is running"),
    ]
    """
    Whether the lift motor is running
    """

    enabled: bool = pydantic.Field()
    """
    Whether the lift motor is enabled
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the lift motor"),
    ]
    """
    The updated at time of the lift motor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
