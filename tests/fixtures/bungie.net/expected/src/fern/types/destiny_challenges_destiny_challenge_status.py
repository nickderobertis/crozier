

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyChallengesDestinyChallengeStatus(UniversalBaseModel):
    """
    Represents the status and other related information for a challenge that is - or was - available to a player.
    A challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play.
    """

    objective: typing.Optional[DestinyQuestsDestinyObjectiveProgress] = pydantic.Field(default=None)
    """
    The progress - including completion status - of the active challenge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
