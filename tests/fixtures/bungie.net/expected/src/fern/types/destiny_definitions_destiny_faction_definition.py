

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_faction_vendor_definition import DestinyDefinitionsDestinyFactionVendorDefinition


class DestinyDefinitionsDestinyFactionDefinition(UniversalBaseModel):
    """
    These definitions represent Factions in the game. Factions have ended up unilaterally being related to Vendors that represent them, but that need not necessarily be the case.
    A Faction is really just an entity that has a related progression for which a character can gain experience. In Destiny 1, Dead Orbit was an example of a Faction: there happens to be a Vendor that represents Dead Orbit (and indeed, DestinyVendorDefinition.factionHash defines to this relationship), but Dead Orbit could theoretically exist without the Vendor that provides rewards.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    progression_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressionHash"),
        pydantic.Field(
            alias="progressionHash",
            description="The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.",
        ),
    ] = None
    """
    The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    reward_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardItemHash"),
        pydantic.Field(alias="rewardItemHash", description="The faction reward item hash, usually an engram."),
    ] = None
    """
    The faction reward item hash, usually an engram.
    """

    reward_vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardVendorHash"),
        pydantic.Field(
            alias="rewardVendorHash", description="The faction reward vendor hash, used for faction engram previews."
        ),
    ] = None
    """
    The faction reward vendor hash, used for faction engram previews.
    """

    token_values: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="tokenValues"),
        pydantic.Field(
            alias="tokenValues", description="The faction token item hashes, and their respective progression values."
        ),
    ] = None
    """
    The faction token item hashes, and their respective progression values.
    """

    vendors: typing.Optional[typing.List[DestinyDefinitionsDestinyFactionVendorDefinition]] = pydantic.Field(
        default=None
    )
    """
    List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
