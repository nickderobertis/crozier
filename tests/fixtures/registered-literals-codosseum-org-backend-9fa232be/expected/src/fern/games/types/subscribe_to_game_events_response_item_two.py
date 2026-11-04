

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.player_leave_event import PlayerLeaveEvent
from .subscribe_to_game_events_response_item_two_event import SubscribeToGameEventsResponseItemTwoEvent


class SubscribeToGameEventsResponseItemTwo(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemTwoEvent] = None
    data: typing.Optional[PlayerLeaveEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
