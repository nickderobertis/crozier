

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loyalty_event_date_time_filter import LoyaltyEventDateTimeFilter
from .loyalty_event_location_filter import LoyaltyEventLocationFilter
from .loyalty_event_loyalty_account_filter import LoyaltyEventLoyaltyAccountFilter
from .loyalty_event_order_filter import LoyaltyEventOrderFilter
from .loyalty_event_type_filter import LoyaltyEventTypeFilter


class LoyaltyEventFilter(UniversalBaseModel):
    """
    The filtering criteria. If the request specifies multiple filters,
    the endpoint uses a logical AND to evaluate them.
    """

    date_time_filter: typing.Optional[LoyaltyEventDateTimeFilter] = None
    location_filter: typing.Optional[LoyaltyEventLocationFilter] = None
    loyalty_account_filter: typing.Optional[LoyaltyEventLoyaltyAccountFilter] = None
    order_filter: typing.Optional[LoyaltyEventOrderFilter] = None
    type_filter: typing.Optional[LoyaltyEventTypeFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
