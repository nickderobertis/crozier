

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_artifacts_destiny_artifact_tier_item import DestinyArtifactsDestinyArtifactTierItem


class DestinyArtifactsDestinyArtifactTier(UniversalBaseModel):
    is_unlocked: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isUnlocked"), pydantic.Field(alias="isUnlocked")
    ] = None
    items: typing.Optional[typing.List[DestinyArtifactsDestinyArtifactTierItem]] = None
    points_to_unlock: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pointsToUnlock"), pydantic.Field(alias="pointsToUnlock")
    ] = None
    tier_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tierHash"), pydantic.Field(alias="tierHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
