

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .website_get_public_stats_by_share_id_response_average_visit_duration import (
    WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration,
)
from .website_get_public_stats_by_share_id_response_bounce_rate import WebsiteGetPublicStatsByShareIdResponseBounceRate
from .website_get_public_stats_by_share_id_response_pageviews import WebsiteGetPublicStatsByShareIdResponsePageviews
from .website_get_public_stats_by_share_id_response_pageviews_trend_item import (
    WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem,
)
from .website_get_public_stats_by_share_id_response_visitors import WebsiteGetPublicStatsByShareIdResponseVisitors


class WebsiteGetPublicStatsByShareIdResponse(UniversalBaseModel):
    pageviews: WebsiteGetPublicStatsByShareIdResponsePageviews
    visitors: WebsiteGetPublicStatsByShareIdResponseVisitors
    bounce_rate: WebsiteGetPublicStatsByShareIdResponseBounceRate
    average_visit_duration: WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration
    pageviews_trend: typing.List[WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
