

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.eliminated_event import EliminatedEvent
from .subscribe_to_game_events_response_item_ten_event import SubscribeToGameEventsResponseItemTenEvent


class SubscribeToGameEventsResponseItemTen(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemTenEvent] = None
    data: typing.Optional[EliminatedEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
