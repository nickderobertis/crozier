

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_artifacts_destiny_artifact_tier import DestinyArtifactsDestinyArtifactTier


class DestinyArtifactsDestinyArtifactCharacterScoped(UniversalBaseModel):
    artifact_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="artifactHash")] = None
    points_used: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="pointsUsed")] = None
    reset_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="resetCount")] = None
    tiers: typing.Optional[typing.List[DestinyArtifactsDestinyArtifactTier]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
