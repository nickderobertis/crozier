

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounce_statistics import BounceStatistics
from .bounce_statistics_response_object import BounceStatisticsResponseObject


class BounceStatisticsResponse(UniversalBaseModel):
    object: BounceStatisticsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[BounceStatistics] = pydantic.Field()
    """
    Array of bounce statistics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
