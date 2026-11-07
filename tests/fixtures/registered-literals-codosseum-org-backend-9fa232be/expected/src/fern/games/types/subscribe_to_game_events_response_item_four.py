

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subscribe_to_game_events_response_item_four_event import SubscribeToGameEventsResponseItemFourEvent


class SubscribeToGameEventsResponseItemFour(UniversalBaseModel):
    """
    This event doesn't have data associated with it because all relevant data is received
    before this event through PlayerSubmitEvent, PlayerFinishEvent and PlayerCodeRevealEvent.
    To get everything at once proactively, GET /games/{id}/rounds/results can be used.
    """

    event: typing.Optional[SubscribeToGameEventsResponseItemFourEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
