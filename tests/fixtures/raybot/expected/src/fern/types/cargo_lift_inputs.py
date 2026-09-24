

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .motor_speed import MotorSpeed


class CargoLiftInputs(UniversalBaseModel):
    position: int = pydantic.Field()
    """
    The position to lift the cargo
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
