

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .emission_class import EmissionClass
from .fuel_type import FuelType
from .vehicle_type import VehicleType


class VehicleCharacteristics(UniversalBaseModel):
    """
    Vehicle characteristics
    """

    type: VehicleType
    width: typing.Optional[float] = pydantic.Field(default=None)
    """
    The width of the vehicle in metres
    """

    height: typing.Optional[float] = pydantic.Field(default=None)
    """
    The height of the vehicle in metres
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    The weight of the entire vehicle including axle load and trailers in metric tonnes
    """

    length: typing.Optional[float] = pydantic.Field(default=None)
    """
    The length of the specified vehicle in metres
    """

    axle_load: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="axleLoad"),
        pydantic.Field(alias="axleLoad", description="The axle load of the specified vehicle in metric tonnes"),
    ] = None
    """
    The axle load of the specified vehicle in metric tonnes
    """

    has_trailer: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasTrailer"),
        pydantic.Field(alias="hasTrailer", description="Indication whether a vehicle has a trailer"),
    ] = None
    """
    Indication whether a vehicle has a trailer
    """

    emission_class: typing_extensions.Annotated[
        typing.Optional[EmissionClass], FieldMetadata(alias="emissionClass"), pydantic.Field(alias="emissionClass")
    ] = None
    fuel_types: typing_extensions.Annotated[
        typing.Optional[typing.List[FuelType]],
        FieldMetadata(alias="fuelTypes"),
        pydantic.Field(alias="fuelTypes", description="A collection of fuel types"),
    ] = None
    """
    A collection of fuel types
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
