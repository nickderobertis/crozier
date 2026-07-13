

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase(UniversalBaseModel):
    phase_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="phaseHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier of the activity's phase.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
