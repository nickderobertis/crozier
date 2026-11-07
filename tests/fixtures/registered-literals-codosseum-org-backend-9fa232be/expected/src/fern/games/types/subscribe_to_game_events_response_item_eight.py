

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.test_result_event import TestResultEvent
from .subscribe_to_game_events_response_item_eight_event import SubscribeToGameEventsResponseItemEightEvent


class SubscribeToGameEventsResponseItemEight(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemEightEvent] = None
    data: typing.Optional[TestResultEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
