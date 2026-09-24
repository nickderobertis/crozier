

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_connection import AppConnection
from .battery_state import BatteryState
from .cargo_door_motor_state import CargoDoorMotorState
from .cargo_state import CargoState
from .charge_state import ChargeState
from .discharge_state import DischargeState
from .distance_sensor_state import DistanceSensorState
from .drive_motor_state import DriveMotorState
from .lift_motor_state import LiftMotorState
from .location_state import LocationState
from .robot_state_response_leds import RobotStateResponseLeds


class RobotStateResponse(UniversalBaseModel):
    battery: BatteryState
    charge: ChargeState
    discharge: DischargeState
    distance_sensor: typing_extensions.Annotated[
        DistanceSensorState, FieldMetadata(alias="distanceSensor"), pydantic.Field(alias="distanceSensor")
    ]
    lift_motor: typing_extensions.Annotated[
        LiftMotorState, FieldMetadata(alias="liftMotor"), pydantic.Field(alias="liftMotor")
    ]
    drive_motor: typing_extensions.Annotated[
        DriveMotorState, FieldMetadata(alias="driveMotor"), pydantic.Field(alias="driveMotor")
    ]
    location: LocationState
    cargo: CargoState
    cargo_door_motor: typing_extensions.Annotated[
        CargoDoorMotorState, FieldMetadata(alias="cargoDoorMotor"), pydantic.Field(alias="cargoDoorMotor")
    ]
    app_connection: typing_extensions.Annotated[
        AppConnection, FieldMetadata(alias="appConnection"), pydantic.Field(alias="appConnection")
    ]
    leds: RobotStateResponseLeds

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
