

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.player_finish_event import PlayerFinishEvent
from .subscribe_to_game_events_response_item_seven_event import SubscribeToGameEventsResponseItemSevenEvent


class SubscribeToGameEventsResponseItemSeven(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemSevenEvent] = None
    data: typing.Optional[PlayerFinishEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
