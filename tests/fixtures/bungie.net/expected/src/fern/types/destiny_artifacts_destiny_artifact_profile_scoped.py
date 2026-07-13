

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_progression import DestinyDestinyProgression


class DestinyArtifactsDestinyArtifactProfileScoped(UniversalBaseModel):
    """
    Represents a Seasonal Artifact and all data related to it for the requested Account.
    It can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.
    """

    artifact_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="artifactHash")] = None
    point_progression: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyProgression], FieldMetadata(alias="pointProgression")
    ] = None
    points_acquired: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="pointsAcquired")] = None
    power_bonus: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="powerBonus")] = None
    power_bonus_progression: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyProgression], FieldMetadata(alias="powerBonusProgression")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
