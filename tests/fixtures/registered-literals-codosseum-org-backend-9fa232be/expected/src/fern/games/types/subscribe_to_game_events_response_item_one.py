

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.player_join_event import PlayerJoinEvent
from .subscribe_to_game_events_response_item_one_event import SubscribeToGameEventsResponseItemOneEvent


class SubscribeToGameEventsResponseItemOne(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemOneEvent] = None
    data: typing.Optional[PlayerJoinEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
