

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.round_start_event import RoundStartEvent
from .subscribe_to_game_events_response_item_three_event import SubscribeToGameEventsResponseItemThreeEvent


class SubscribeToGameEventsResponseItemThree(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemThreeEvent] = None
    data: typing.Optional[RoundStartEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
