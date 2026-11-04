

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .website_stats_response_bounces import WebsiteStatsResponseBounces
from .website_stats_response_pageviews import WebsiteStatsResponsePageviews
from .website_stats_response_totaltime import WebsiteStatsResponseTotaltime
from .website_stats_response_uniques import WebsiteStatsResponseUniques


class WebsiteStatsResponse(UniversalBaseModel):
    pageviews: WebsiteStatsResponsePageviews
    uniques: WebsiteStatsResponseUniques
    totaltime: WebsiteStatsResponseTotaltime
    bounces: WebsiteStatsResponseBounces

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
