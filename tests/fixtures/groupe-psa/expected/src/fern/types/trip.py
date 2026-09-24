

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .created_at_field import CreatedAtField
from .energy_consumption import EnergyConsumption
from .lite_energy import LiteEnergy
from .position import Position
from .trip_faults_item import TripFaultsItem
from .trip_kinetic import TripKinetic
from .trip_links import TripLinks
from .trip_segment import TripSegment
from .updated_at_field import UpdatedAtField
from .vin import Vin


class Trip(CreatedAtField, UpdatedAtField):
    links: typing_extensions.Annotated[TripLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    id: str = pydantic.Field()
    """
    Identifier of a trip
    """

    vin: Vin
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="Date & Time when the trip started"),
    ] = None
    """
    Date & Time when the trip started
    """

    stopped_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="stoppedAt"),
        pydantic.Field(alias="stoppedAt", description="Date & Time when the trip stopped"),
    ] = None
    """
    Date & Time when the trip stopped
    """

    start_position: typing_extensions.Annotated[
        typing.Optional[Position], FieldMetadata(alias="startPosition"), pydantic.Field(alias="startPosition")
    ] = None
    stop_position: typing_extensions.Annotated[
        typing.Optional[Position], FieldMetadata(alias="stopPosition"), pydantic.Field(alias="stopPosition")
    ] = None
    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Duration in second of the trip
    """

    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Distance in km of the trip
    """

    start_mileage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startMileage"),
        pydantic.Field(alias="startMileage", description="Vehicle mileage at the trip starting time."),
    ] = None
    """
    Vehicle mileage at the trip starting time.
    """

    start_energies: typing_extensions.Annotated[
        typing.Optional[typing.List[LiteEnergy]],
        FieldMetadata(alias="startEnergies"),
        pydantic.Field(
            alias="startEnergies", description="Vehicle energies levels and autonomies at the trip start time."
        ),
    ] = None
    """
    Vehicle energies levels and autonomies at the trip start time.
    """

    end_energies: typing_extensions.Annotated[
        typing.Optional[typing.List[LiteEnergy]],
        FieldMetadata(alias="endEnergies"),
        pydantic.Field(alias="endEnergies", description="Vehicle energies levels and autonomies at the trip end time."),
    ] = None
    """
    Vehicle energies levels and autonomies at the trip end time.
    """

    energy_consumptions: typing_extensions.Annotated[
        typing.Optional[typing.List[EnergyConsumption]],
        FieldMetadata(alias="energyConsumptions"),
        pydantic.Field(
            alias="energyConsumptions", description="The consumptions of different energies during this trip."
        ),
    ] = None
    """
    The consumptions of different energies during this trip.
    """

    kinetic: typing.Optional[TripKinetic] = pydantic.Field(default=None)
    """
    Expresses the max and average vehicle speed during this trip.
    """

    segments: typing.Optional[typing.List[TripSegment]] = pydantic.Field(default=None)
    """
    The parts of the trip crossed for each type of propulsion.
    """

    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines either this trip is finished or not.
    """

    faults: typing.Optional[typing.List[TripFaultsItem]] = pydantic.Field(default=None)
    """
    Faults of this finished or in progress trip. This means that we lacked data from the vehicle to complete the trip description during one of its step (starting, progressing, or finishing).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
