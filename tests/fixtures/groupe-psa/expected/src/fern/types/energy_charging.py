

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .charging_status_enum import ChargingStatusEnum
from .energy_charging_charging_power_level import EnergyChargingChargingPowerLevel
from .energy_charging_schedule import EnergyChargingSchedule
from .energy_charging_type import EnergyChargingType


class EnergyCharging(UniversalBaseModel):
    """
    Electric charging state.
    """

    plugged: typing.Optional[bool] = None
    status: typing.Optional[ChargingStatusEnum] = None
    remaining_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="remainingTime"),
        pydantic.Field(
            alias="remainingTime",
            description="Remaning time before the battery is fully charged. This duration is expressed using [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
        ),
    ] = None
    """
    Remaning time before the battery is fully charged. This duration is expressed using [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.
    """

    charging_rate: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="chargingRate"),
        pydantic.Field(
            alias="chargingRate", description="Charging speed (expressed in gained batteryLife per hour -> KM/H)."
        ),
    ] = None
    """
    Charging speed (expressed in gained batteryLife per hour -> KM/H).
    """

    charging_power_level: typing_extensions.Annotated[
        typing.Optional[EnergyChargingChargingPowerLevel],
        FieldMetadata(alias="chargingPowerLevel"),
        pydantic.Field(
            alias="chargingPowerLevel",
            description="Charging power level. Expressed by possible values enum. This enum list may change in the future. The application must be aware of this and provide for lenient deserialization.",
        ),
    ] = None
    """
    Charging power level. Expressed by possible values enum. This enum list may change in the future. The application must be aware of this and provide for lenient deserialization.
    """

    charging_mode: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="chargingMode"),
        pydantic.Field(alias="chargingMode", description="The charging mode; Slow, Quick and No(not charging)."),
    ] = None
    """
    The charging mode; Slow, Quick and No(not charging).
    """

    next_delayed_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextDelayedTime"),
        pydantic.Field(
            alias="nextDelayedTime",
            description="Duration (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) until the next battery charging.",
        ),
    ] = None
    """
    Duration (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) until the next battery charging.
    """

    schedule: typing.Optional[EnergyChargingSchedule] = None
    type: typing.Optional[EnergyChargingType] = pydantic.Field(default=None)
    """
    Charging type associated to the vehicle. Full means that the charge will stop when it is completed whereas partial will stop before end of charge in order to optimize battery lifetime.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
