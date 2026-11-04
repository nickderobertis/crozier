

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.game_update_event import GameUpdateEvent
from .subscribe_to_game_events_response_item_zero_event import SubscribeToGameEventsResponseItemZeroEvent


class SubscribeToGameEventsResponseItemZero(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemZeroEvent] = None
    data: typing.Optional[GameUpdateEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
