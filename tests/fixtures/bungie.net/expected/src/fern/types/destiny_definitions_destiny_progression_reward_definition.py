

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyProgressionRewardDefinition(UniversalBaseModel):
    """
    Inventory Items can reward progression when actions are performed on them. A common example of this in Destiny 1 was Bounties, which would reward Experience on your Character and the like when you completed the bounty.
    Note that this maps to a DestinyProgressionMappingDefinition, and *not* a DestinyProgressionDefinition directly. This is apparently so that multiple progressions can be granted progression points/experience at the same time.
    """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of experience to give to each of the mapped progressions.
    """

    apply_throttles: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="applyThrottles"),
        pydantic.Field(
            alias="applyThrottles",
            description="If true, the game's internal mechanisms to throttle progression should be applied.",
        ),
    ] = None
    """
    If true, the game's internal mechanisms to throttle progression should be applied.
    """

    progression_mapping_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressionMappingHash"),
        pydantic.Field(
            alias="progressionMappingHash",
            description="The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.",
        ),
    ] = None
    """
    The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
