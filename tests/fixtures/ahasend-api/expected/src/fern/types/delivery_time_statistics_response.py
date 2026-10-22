

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery_time_statistics import DeliveryTimeStatistics
from .delivery_time_statistics_response_object import DeliveryTimeStatisticsResponseObject


class DeliveryTimeStatisticsResponse(UniversalBaseModel):
    object: DeliveryTimeStatisticsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[DeliveryTimeStatistics] = pydantic.Field()
    """
    Array of delivery time statistics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
