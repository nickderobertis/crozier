

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .adas import Adas
from .base_alarm import BaseAlarm
from .base_safety import BaseSafety
from .basic_kinetic import BasicKinetic
from .battery_base import BatteryBase
from .doors_state_base import DoorsStateBase
from .driving_behavior_base import DrivingBehaviorBase
from .energy_base import EnergyBase
from .engine_base import EngineBase
from .ignition_base import IgnitionBase
from .lighting_base import LightingBase
from .lighting_system_base import LightingSystemBase
from .powertrain_base import PowertrainBase
from .telemetry_vehicle_odometer import TelemetryVehicleOdometer
from .transmission import Transmission
from .wiping_blades_state import WipingBladesState


class TelemetryVehicle(UniversalBaseModel):
    engines: typing.Optional[typing.List[EngineBase]] = None
    energies: typing.Optional[typing.List[EnergyBase]] = None
    transmission: typing.Optional[Transmission] = None
    powertrain: typing.Optional[PowertrainBase] = None
    adas: typing.Optional[Adas] = None
    lighting: typing.Optional[LightingBase] = None
    lighting_system: typing_extensions.Annotated[
        typing.Optional[LightingSystemBase],
        FieldMetadata(alias="lightingSystem"),
        pydantic.Field(alias="lightingSystem"),
    ] = None
    ignition: typing.Optional[IgnitionBase] = None
    doors_state: typing_extensions.Annotated[
        typing.Optional[DoorsStateBase], FieldMetadata(alias="doorsState"), pydantic.Field(alias="doorsState")
    ] = None
    battery: typing.Optional[BatteryBase] = None
    safety: typing.Optional[BaseSafety] = None
    wiping_blades: typing_extensions.Annotated[
        typing.Optional[WipingBladesState], FieldMetadata(alias="wipingBlades"), pydantic.Field(alias="wipingBlades")
    ] = None
    odometer: typing.Optional[TelemetryVehicleOdometer] = None
    alarm: typing.Optional[BaseAlarm] = None
    kinetic: typing.Optional[BasicKinetic] = None
    driving_behavior: typing_extensions.Annotated[
        typing.Optional[DrivingBehaviorBase],
        FieldMetadata(alias="drivingBehavior"),
        pydantic.Field(alias="drivingBehavior", description="Describe the behavior of the driver"),
    ] = None
    """
    Describe the behavior of the driver
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
