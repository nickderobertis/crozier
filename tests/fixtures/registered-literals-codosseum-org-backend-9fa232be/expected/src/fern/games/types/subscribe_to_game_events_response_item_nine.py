

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.sync_event import SyncEvent
from .subscribe_to_game_events_response_item_nine_event import SubscribeToGameEventsResponseItemNineEvent


class SubscribeToGameEventsResponseItemNine(UniversalBaseModel):
    event: typing.Optional[SubscribeToGameEventsResponseItemNineEvent] = None
    data: typing.Optional[SyncEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
