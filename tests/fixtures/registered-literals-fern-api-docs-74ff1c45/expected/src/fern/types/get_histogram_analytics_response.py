

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .histogram_analytics_bar import HistogramAnalyticsBar


class GetHistogramAnalyticsResponse(UniversalBaseModel):
    bars: typing.List[HistogramAnalyticsBar] = pydantic.Field()
    """
    List of histogram analytics bars
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
