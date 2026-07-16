

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventTypeFilter(UniversalBaseModel):
    """
    Filter events by event type.
    """

    types: typing.List[str] = pydantic.Field()
    """
    The loyalty event types used to filter the result.
    If multiple values are specified, the endpoint uses a 
    logical OR to combine them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
