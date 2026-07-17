

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_talent_node_step_groups import DestinyDefinitionsDestinyTalentNodeStepGroups


class DestinyDefinitionsDestinySandboxPerkDefinition(UniversalBaseModel):
    """
    Perks are modifiers to a character or item that can be applied situationally.
    - Perks determine a weapons' damage type.
    - Perks put the Mods in Modifiers (they are literally the entity that bestows the Sandbox benefit for whatever fluff text about the modifier in the Socket, Plug or Talent Node)
    - Perks are applied for unique alterations of state in Objectives
    Anyways, I'm sure you can see why perks are so interesting.
    What Perks often don't have is human readable information, so we attempt to reverse engineer that by pulling that data from places that uniquely refer to these perks: namely, Talent Nodes and Plugs. That only gives us a subset of perks that are human readable, but those perks are the ones people generally care about anyways. The others are left as a mystery, their true purpose mostly unknown and undocumented.
    """

    damage_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="damageType"),
        pydantic.Field(
            alias="damageType",
            description="If this perk grants a damage type to a weapon, the damage type will be defined here.\r\nUnless you have a compelling reason to use this enum value, use the damageTypeHash instead to look up the actual DestinyDamageTypeDefinition.",
        ),
    ] = None
    """
    If this perk grants a damage type to a weapon, the damage type will be defined here.
    Unless you have a compelling reason to use this enum value, use the damageTypeHash instead to look up the actual DestinyDamageTypeDefinition.
    """

    damage_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="damageTypeHash"),
        pydantic.Field(
            alias="damageTypeHash",
            description="The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.\r\nThis is preferred over using the damageType enumeration value, which has been left purely because it is occasionally convenient.",
        ),
    ] = None
    """
    The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.
    This is preferred over using the damageType enumeration value, which has been left purely because it is occasionally convenient.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties",
            description="These display properties are by no means guaranteed to be populated. Usually when it is, it's only because we back-filled them with the displayProperties of some Talent Node or Plug item that happened to be uniquely providing that perk.",
        ),
    ] = None
    """
    These display properties are by no means guaranteed to be populated. Usually when it is, it's only because we back-filled them with the displayProperties of some Talent Node or Plug item that happened to be uniquely providing that perk.
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

    is_displayable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDisplayable"),
        pydantic.Field(
            alias="isDisplayable",
            description="If true, you can actually show the perk in the UI. Otherwise, it doesn't have useful player-facing information.",
        ),
    ] = None
    """
    If true, you can actually show the perk in the UI. Otherwise, it doesn't have useful player-facing information.
    """

    perk_groups: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyTalentNodeStepGroups],
        FieldMetadata(alias="perkGroups"),
        pydantic.Field(
            alias="perkGroups",
            description="An old holdover from the original Armory, this was an attempt to group perks by functionality.\r\nIt is as yet unpopulated, and there will be quite a bit of work needed to restore it to its former working order.",
        ),
    ] = None
    """
    An old holdover from the original Armory, this was an attempt to group perks by functionality.
    It is as yet unpopulated, and there will be quite a bit of work needed to restore it to its former working order.
    """

    perk_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="perkIdentifier"),
        pydantic.Field(alias="perkIdentifier", description="The string identifier for the perk."),
    ] = None
    """
    The string identifier for the perk.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
