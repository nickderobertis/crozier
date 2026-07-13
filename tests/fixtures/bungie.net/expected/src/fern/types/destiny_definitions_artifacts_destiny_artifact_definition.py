

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_artifacts_destiny_artifact_tier_definition import (
    DestinyDefinitionsArtifactsDestinyArtifactTierDefinition,
)
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_item_translation_block_definition import (
    DestinyDefinitionsDestinyItemTranslationBlockDefinition,
)


class DestinyDefinitionsArtifactsDestinyArtifactDefinition(UniversalBaseModel):
    """
    Represents known info about a Destiny Artifact.
    We cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change.
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

    tiers: typing.Optional[typing.List[DestinyDefinitionsArtifactsDestinyArtifactTierDefinition]] = pydantic.Field(
        default=None
    )
    """
    Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change.
    """

    translation_block: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyItemTranslationBlockDefinition],
        FieldMetadata(alias="translationBlock"),
    ] = pydantic.Field(default=None)
    """
    Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item's gearset information, but the source of this data is subject to change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
