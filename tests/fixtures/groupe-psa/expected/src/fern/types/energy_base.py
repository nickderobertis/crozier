

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .energy_base_extension import EnergyBaseExtension
from .energy_base_sub_type import EnergyBaseSubType
from .energy_base_type import EnergyBaseType


class EnergyBase(UniversalBaseModel):
    """
    Describe vehicle energy supply for thermic, low emission vehicle or both.
    """

    type: EnergyBaseType = pydantic.Field()
    """
    Energy type present on the vehicle.
    """

    sub_type: typing_extensions.Annotated[
        typing.Optional[EnergyBaseSubType],
        FieldMetadata(alias="subType"),
        pydantic.Field(
            alias="subType",
            description="Energy subtype. This field is not mandatory and therefore if it is not present, it means that the resource consumer should only process the primary energy type. The enumeration of the subtypes is not exhaustive and may contain more elements depending on the evolution of the vehicles. The consumer of the data must take this constraint into account. The Fossil and Electric energy subtypes are only used to populate this subtype for the default Fuel and Eletric types.\n  * Electric and hydrogen vehicles energy types are considered as low emission energies whereas fuel(fossil) is associated to thermic energy",
        ),
    ] = None
    """
    Energy subtype. This field is not mandatory and therefore if it is not present, it means that the resource consumer should only process the primary energy type. The enumeration of the subtypes is not exhaustive and may contain more elements depending on the evolution of the vehicles. The consumer of the data must take this constraint into account. The Fossil and Electric energy subtypes are only used to populate this subtype for the default Fuel and Eletric types.
      * Electric and hydrogen vehicles energy types are considered as low emission energies whereas fuel(fossil) is associated to thermic energy
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Percentage of remaining energy (Fuel or electric) level. Expressed with a precision of 0.1%.
    """

    autonomy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Vehicle autonomy expressed in km for this energy class.
    """

    extension: typing.Optional[EnergyBaseExtension] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
