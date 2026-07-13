

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsEnergyTypesDestinyEnergyTypeDefinition(UniversalBaseModel):
    """
    Represents types of Energy that can be used for costs and payments related to Armor 2.0 mods.
    """

    capacity_stat_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="capacityStatHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this Energy Type can be used for determining the Type of Energy that an item can consume, this is the hash for the DestinyInvestmentStatDefinition that represents the stat which holds the Capacity for that energy type. (Note that this is optional because "Any" is a valid cost, but not valid for Capacity - an Armor must have a specific Energy Type for determining the energy type that the Armor is restricted to use)
    """

    cost_stat_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="costStatHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this Energy Type can be used as a cost to pay for socketing Armor 2.0 items, this is the hash for the DestinyInvestmentStatDefinition that stores the plug's raw cost.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    The description of the energy type, icon etc...
    """

    enum_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="enumValue")] = pydantic.Field(
        default=None
    )
    """
    We have an enumeration for Energy types for quick reference. This is the current definition's Energy type enum value.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    show_icon: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="showIcon")] = pydantic.Field(
        default=None
    )
    """
    If TRUE, the game shows this Energy type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.
    """

    transparent_icon_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transparentIconPath")
    ] = pydantic.Field(default=None)
    """
    A variant of the icon that is transparent and colorless.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
