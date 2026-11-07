

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.player_submit_event import PlayerSubmitEvent
from .subscribe_to_game_events_response_item_five_event import SubscribeToGameEventsResponseItemFiveEvent


class SubscribeToGameEventsResponseItemFive(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemFiveEvent] = None
    data: typing.Optional[PlayerSubmitEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
