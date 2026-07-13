

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsDestinyActivityChallengeDefinition(UniversalBaseModel):
    """
    Represents a reference to a Challenge, which for now is just an Objective.
    """

    dummy_rewards: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]], FieldMetadata(alias="dummyRewards")
    ] = pydantic.Field(default=None)
    """
    The rewards as they're represented in the UI. Note that they generally link to "dummy" items that give a summary of rewards rather than direct, real items themselves.
    If the quantity is 0, don't show the quantity.
    """

    objective_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="objectiveHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
