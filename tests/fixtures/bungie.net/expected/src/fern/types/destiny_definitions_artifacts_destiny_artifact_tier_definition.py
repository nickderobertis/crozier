

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_artifacts_destiny_artifact_tier_item_definition import (
    DestinyDefinitionsArtifactsDestinyArtifactTierItemDefinition,
)


class DestinyDefinitionsArtifactsDestinyArtifactTierDefinition(UniversalBaseModel):
    display_title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayTitle"),
        pydantic.Field(alias="displayTitle", description="The human readable title of this tier, if any."),
    ] = None
    """
    The human readable title of this tier, if any.
    """

    items: typing.Optional[typing.List[DestinyDefinitionsArtifactsDestinyArtifactTierItemDefinition]] = pydantic.Field(
        default=None
    )
    """
    The items that can be earned within this tier.
    """

    minimum_unlock_points_used_requirement: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minimumUnlockPointsUsedRequirement"),
        pydantic.Field(
            alias="minimumUnlockPointsUsedRequirement",
            description='The minimum number of "unlock points" that you must have used before you can unlock items from this tier.',
        ),
    ] = None
    """
    The minimum number of "unlock points" that you must have used before you can unlock items from this tier.
    """

    progress_requirement_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="progressRequirementMessage"),
        pydantic.Field(
            alias="progressRequirementMessage",
            description="A string representing the localized minimum requirement text for this Tier, if any.",
        ),
    ] = None
    """
    A string representing the localized minimum requirement text for this Tier, if any.
    """

    tier_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="tierHash"),
        pydantic.Field(
            alias="tierHash", description="An identifier, unique within the Artifact, for this specific tier."
        ),
    ] = None
    """
    An identifier, unique within the Artifact, for this specific tier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
