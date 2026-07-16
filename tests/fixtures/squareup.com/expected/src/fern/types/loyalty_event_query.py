

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loyalty_event_filter import LoyaltyEventFilter


class LoyaltyEventQuery(UniversalBaseModel):
    """
    Represents a query used to search for loyalty events.
    """

    filter: typing.Optional[LoyaltyEventFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
