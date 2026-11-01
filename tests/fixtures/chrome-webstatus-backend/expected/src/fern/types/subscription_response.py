

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .saved_search_info import SavedSearchInfo
from .subscription_frequency import SubscriptionFrequency
from .subscription_response_channel_type import SubscriptionResponseChannelType
from .subscription_trigger_response_item import SubscriptionTriggerResponseItem


class SubscriptionResponse(UniversalBaseModel):
    id: str
    created_at: dt.datetime
    updated_at: dt.datetime
    subscribable: SavedSearchInfo
    channel_id: str
    channel_type: SubscriptionResponseChannelType = pydantic.Field()
    """
    Self-describing type to allow the UI to identify the delivery mode without fetching the underlying channel.
    """

    frequency: SubscriptionFrequency
    triggers: typing.List[SubscriptionTriggerResponseItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
