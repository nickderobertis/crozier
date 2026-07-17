

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsItemsDestinyEnergyCostEntry(UniversalBaseModel):
    """
    Some plugs cost Energy, which is a stat on the item that can be increased by other plugs (that, at least in Armor 2.0, have a "masterworks-like" mechanic for upgrading). If a plug has costs, the details of that cost are defined here.
    """

    energy_cost: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="energyCost"),
        pydantic.Field(alias="energyCost", description="The Energy cost for inserting this plug."),
    ] = None
    """
    The Energy cost for inserting this plug.
    """

    energy_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="energyType"),
        pydantic.Field(alias="energyType", description="The type of energy that this plug costs, in enum form."),
    ] = None
    """
    The type of energy that this plug costs, in enum form.
    """

    energy_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="energyTypeHash"),
        pydantic.Field(
            alias="energyTypeHash",
            description="The type of energy that this plug costs, as a reference to the DestinyEnergyTypeDefinition of the energy type.",
        ),
    ] = None
    """
    The type of energy that this plug costs, as a reference to the DestinyEnergyTypeDefinition of the energy type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
