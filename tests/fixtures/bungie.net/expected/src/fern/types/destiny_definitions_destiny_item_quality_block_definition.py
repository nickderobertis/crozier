

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_version_definition import DestinyDefinitionsDestinyItemVersionDefinition


class DestinyDefinitionsDestinyItemQualityBlockDefinition(UniversalBaseModel):
    """
    An item's "Quality" determines its calculated stats. The Level at which the item spawns is combined with its "qualityLevel" along with some additional calculations to determine the value of those stats.
    In Destiny 2, most items don't have default item levels and quality, making this property less useful: these apparently are almost always determined by the complex mechanisms of the Reward system rather than statically. They are still provided here in case they are still useful for people. This also contains some information about Infusion.
    """

    current_version: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="currentVersion")] = (
        pydantic.Field(default=None)
    )
    """
    The latest version available for this item.
    """

    display_version_watermark_icons: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="displayVersionWatermarkIcons")
    ] = pydantic.Field(default=None)
    """
    Icon overlays to denote the item version and power cap status.
    """

    infusion_category_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="infusionCategoryHash")
    ] = pydantic.Field(default=None)
    """
    The hash identifier for the infusion. It does not map to a Definition entity.
    DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.
    """

    infusion_category_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="infusionCategoryHashes")
    ] = pydantic.Field(default=None)
    """
    If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other.
    """

    infusion_category_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="infusionCategoryName")
    ] = pydantic.Field(default=None)
    """
    The string identifier for this item's "infusability", if any. 
    Items that match the same infusionCategoryName are allowed to infuse with each other.
    DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.
    """

    item_levels: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="itemLevels")] = (
        pydantic.Field(default=None)
    )
    """
    The "base" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.
    In practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result.
    """

    progression_level_requirement_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="progressionLevelRequirementHash")
    ] = pydantic.Field(default=None)
    """
    An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition.
    """

    quality_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="qualityLevel")] = (
        pydantic.Field(default=None)
    )
    """
    qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does.
    """

    versions: typing.Optional[typing.List[DestinyDefinitionsDestinyItemVersionDefinition]] = pydantic.Field(
        default=None
    )
    """
    The list of versions available for this item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
