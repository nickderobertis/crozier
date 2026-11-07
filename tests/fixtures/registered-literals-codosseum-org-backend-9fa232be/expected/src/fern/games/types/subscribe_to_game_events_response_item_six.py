

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.player_code_reveal_event import PlayerCodeRevealEvent
from .subscribe_to_game_events_response_item_six_event import SubscribeToGameEventsResponseItemSixEvent


class SubscribeToGameEventsResponseItemSix(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemSixEvent] = None
    data: typing.Optional[PlayerCodeRevealEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
