

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_artifacts_destiny_artifact_profile_scoped import DestinyArtifactsDestinyArtifactProfileScoped


class DestinyComponentsProfilesDestinyProfileProgressionComponent(UniversalBaseModel):
    """
    The set of progression-related information that applies at a Profile-wide level for your Destiny experience. This differs from the Jimi Hendrix Experience because there's less guitars on fire. Yet. #spoileralert?
    This will include information such as Checklist info.
    """

    checklists: typing.Optional[typing.Dict[str, typing.Dict[str, bool]]] = pydantic.Field(default=None)
    """
    The set of checklists that can be examined on a profile-wide basis, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)
    For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
    """

    seasonal_artifact: typing_extensions.Annotated[
        typing.Optional[DestinyArtifactsDestinyArtifactProfileScoped],
        FieldMetadata(alias="seasonalArtifact"),
        pydantic.Field(
            alias="seasonalArtifact",
            description="Data related to your progress on the current season's artifact that is the same across characters.",
        ),
    ] = None
    """
    Data related to your progress on the current season's artifact that is the same across characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
