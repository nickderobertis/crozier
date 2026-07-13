

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsItemsDestinyEnergyCapacityEntry(UniversalBaseModel):
    """
    Items can have Energy Capacity, and plugs can provide that capacity such as on a piece of Armor in Armor 2.0. This is how much "Energy" can be spent on activating plugs for this item.
    """

    capacity_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="capacityValue")] = (
        pydantic.Field(default=None)
    )
    """
    How much energy capacity this plug provides.
    """

    energy_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyType")] = pydantic.Field(
        default=None
    )
    """
    The Energy Type for this energy capacity, in enum form for easy use.
    """

    energy_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    Energy provided by a plug is always of a specific type - this is the hash identifier for the energy type for which it provides Capacity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
