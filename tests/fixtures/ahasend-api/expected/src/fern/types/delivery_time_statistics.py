

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery_time import DeliveryTime


class DeliveryTimeStatistics(UniversalBaseModel):
    from_timestamp: dt.datetime = pydantic.Field()
    """
    Start time of the statistics bucket
    """

    to_timestamp: dt.datetime = pydantic.Field()
    """
    End time of the statistics bucket
    """

    avg_delivery_time: float = pydantic.Field()
    """
    Average delivery time in seconds
    """

    delivered_count: int = pydantic.Field()
    """
    Number of messages
    """

    delivery_times: typing.List[DeliveryTime]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
