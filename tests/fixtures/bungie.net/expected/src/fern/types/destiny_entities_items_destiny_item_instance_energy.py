

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyEntitiesItemsDestinyItemInstanceEnergy(UniversalBaseModel):
    energy_capacity: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyCapacity")] = (
        pydantic.Field(default=None)
    )
    """
    The total capacity of Energy that the item currently has, regardless of if it is currently being used.
    """

    energy_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyType")] = pydantic.Field(
        default=None
    )
    """
    This is the enum version of the Energy Type value, for convenience.
    """

    energy_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The type of energy for this item. Plugs that require Energy can only be inserted if they have the "Any" Energy Type or the matching energy type of this item. This is a reference to the DestinyEnergyTypeDefinition for the energy type, where you can find extended info about it.
    """

    energy_unused: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyUnused")] = (
        pydantic.Field(default=None)
    )
    """
    The amount of energy still available for inserting new plugs.
    """

    energy_used: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="energyUsed")] = pydantic.Field(
        default=None
    )
    """
    The amount of Energy currently in use by inserted plugs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
