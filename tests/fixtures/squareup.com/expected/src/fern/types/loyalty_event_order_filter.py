

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventOrderFilter(UniversalBaseModel):
    """
    Filter events by the order associated with the event.
    """

    order_id: str = pydantic.Field()
    """
    The ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) associated with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
