

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.game_over_event import GameOverEvent
from .subscribe_to_game_events_response_item_data_event import SubscribeToGameEventsResponseItemDataEvent


class SubscribeToGameEventsResponseItemData(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemDataEvent] = None
    data: typing.Optional[GameOverEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
