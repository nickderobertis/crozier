

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .energy_sub_type import EnergySubType
from .energy_type import EnergyType


class LiteEnergy(UniversalBaseModel):
    """
    Describe vehicle energy supply for thermic, low emission vehicle or both.
    """

    type: typing.Optional[EnergyType] = None
    sub_type: typing_extensions.Annotated[
        typing.Optional[EnergySubType], FieldMetadata(alias="subType"), pydantic.Field(alias="subType")
    ] = None
    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Percentage of remaining energy (Fuel or electric) level. Expressed with a precision of 0.1%.
    """

    autonomy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Vehicle autonomy expressed in km for this energy class.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
