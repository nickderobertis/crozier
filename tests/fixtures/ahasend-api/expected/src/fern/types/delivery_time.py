

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeliveryTime(UniversalBaseModel):
    recipient_domain: str = pydantic.Field()
    """
    The recipient domain
    """

    delivery_time: float = pydantic.Field()
    """
    The average time from reception to delivery in seconds
    """

    count: int = pydantic.Field()
    """
    Number of delivered messages included in the average
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
