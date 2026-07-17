

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition(UniversalBaseModel):
    challenge_objective_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="challengeObjectiveHash"),
        pydantic.Field(alias="challengeObjectiveHash", description="The challenge related to this milestone."),
    ] = None
    """
    The challenge related to this milestone.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
