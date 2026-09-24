

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .adas import Adas
from .battery import Battery
from .created_at_field import CreatedAtField
from .doors_state import DoorsState
from .driving_behavior import DrivingBehavior
from .energy import Energy
from .engine import Engine
from .environment import Environment
from .ignition import Ignition
from .kinetic import Kinetic
from .lighting_system import LightingSystem
from .position import Position
from .powertrain import Powertrain
from .preconditioning import Preconditioning
from .privacy import Privacy
from .safety import Safety
from .service_type import ServiceType
from .status_embedded import StatusEmbedded
from .status_links import StatusLinks
from .stolen_obj import StolenObj
from .transmission import Transmission
from .updated_at_field import UpdatedAtField
from .vehicle_odometer import VehicleOdometer
from .vehicle_status_alarm import VehicleStatusAlarm
from .vin import Vin
from .wiping_blades_state import WipingBladesState


class Status(CreatedAtField, UpdatedAtField):
    links: typing_extensions.Annotated[StatusLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    vin: Vin
    ignition: typing.Optional[Ignition] = None
    last_position: typing_extensions.Annotated[
        typing.Optional[Position], FieldMetadata(alias="lastPosition"), pydantic.Field(alias="lastPosition")
    ] = None
    preconditioning: typing.Optional[Preconditioning] = None
    energies: typing.Optional[typing.List[Energy]] = None
    engines: typing.Optional[typing.List[Engine]] = None
    transmission: typing.Optional[Transmission] = None
    powertrain: typing.Optional[Powertrain] = None
    adas: typing.Optional[Adas] = None
    doors_state: typing_extensions.Annotated[
        typing.Optional[DoorsState], FieldMetadata(alias="doorsState"), pydantic.Field(alias="doorsState")
    ] = None
    privacy: typing.Optional[Privacy] = None
    battery: typing.Optional[Battery] = None
    service: typing.Optional[ServiceType] = None
    safety: typing.Optional[Safety] = None
    odometer: typing.Optional[VehicleOdometer] = None
    kinetic: typing.Optional[Kinetic] = None
    environment: typing.Optional[Environment] = None
    driving_behavior: typing_extensions.Annotated[
        typing.Optional[DrivingBehavior],
        FieldMetadata(alias="drivingBehavior"),
        pydantic.Field(alias="drivingBehavior"),
    ] = None
    wiping_blades: typing_extensions.Annotated[
        typing.Optional[WipingBladesState], FieldMetadata(alias="wipingBlades"), pydantic.Field(alias="wipingBlades")
    ] = None
    lighting_system: typing_extensions.Annotated[
        typing.Optional[LightingSystem], FieldMetadata(alias="lightingSystem"), pydantic.Field(alias="lightingSystem")
    ] = None
    alarm: typing.Optional[VehicleStatusAlarm] = None
    stolen: typing.Optional[StolenObj] = None
    embedded: typing_extensions.Annotated[
        typing.Optional[StatusEmbedded], FieldMetadata(alias="_embedded"), pydantic.Field(alias="_embedded")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
