

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bottom_obstacle_tracking import BottomObstacleTracking
from .motor_speed import MotorSpeed


class CargoLowerInputs(UniversalBaseModel):
    position: int = pydantic.Field()
    """
    The position to lower the cargo
    """

    motor_speed: typing_extensions.Annotated[
        MotorSpeed, FieldMetadata(alias="motorSpeed"), pydantic.Field(alias="motorSpeed")
    ]
    bottom_obstacle_tracking: typing_extensions.Annotated[
        typing.Optional[BottomObstacleTracking],
        FieldMetadata(alias="bottomObstacleTracking"),
        pydantic.Field(
            alias="bottomObstacleTracking",
            description="This field is deprecated and will be removed in the future, use command config instead",
        ),
    ] = None
    """
    This field is deprecated and will be removed in the future, use command config instead
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
