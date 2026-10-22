

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deliverability_statistics import DeliverabilityStatistics
from .deliverability_statistics_response_object import DeliverabilityStatisticsResponseObject


class DeliverabilityStatisticsResponse(UniversalBaseModel):
    object: DeliverabilityStatisticsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[DeliverabilityStatistics] = pydantic.Field()
    """
    Array of deliverability statistics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
