

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_inventory_item_stat_definition import (
    DestinyDefinitionsDestinyInventoryItemStatDefinition,
)


class DestinyDefinitionsSourcesDestinyItemSourceDefinition(UniversalBaseModel):
    """
    Properties of a DestinyInventoryItemDefinition that store all of the information we were able to discern about how the item spawns, and where you can find the item.
    Items will have many of these sources, one per level at which it spawns, to try and give more granular data about where items spawn for specific level ranges.
    """

    computed_stats: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyDefinitionsDestinyInventoryItemStatDefinition]],
        FieldMetadata(alias="computedStats"),
        pydantic.Field(alias="computedStats", description="The stats computed for this level/quality range."),
    ] = None
    """
    The stats computed for this level/quality range.
    """

    level: typing.Optional[int] = pydantic.Field(default=None)
    """
    The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns.
    """

    max_level_required: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxLevelRequired"),
        pydantic.Field(
            alias="maxLevelRequired",
            description="The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.",
        ),
    ] = None
    """
    The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.
    """

    max_quality: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxQuality"),
        pydantic.Field(alias="maxQuality", description="The maximum quality at which the item spawns for this level."),
    ] = None
    """
    The maximum quality at which the item spawns for this level.
    """

    min_level_required: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minLevelRequired"),
        pydantic.Field(
            alias="minLevelRequired",
            description="The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.",
        ),
    ] = None
    """
    The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.
    """

    min_quality: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minQuality"),
        pydantic.Field(
            alias="minQuality",
            description="The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don't ask Phaedrus about it, he'll never stop talking and you'll have to write a book about it.",
        ),
    ] = None
    """
    The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don't ask Phaedrus about it, he'll never stop talking and you'll have to write a book about it.
    """

    source_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="sourceHashes"),
        pydantic.Field(
            alias="sourceHashes",
            description="The DestinyRewardSourceDefinitions found that can spawn the item at this level.",
        ),
    ] = None
    """
    The DestinyRewardSourceDefinitions found that can spawn the item at this level.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
