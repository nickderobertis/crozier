



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .website_add_response import WebsiteAddResponse
    from .website_all_response_item import WebsiteAllResponseItem
    from .website_create_or_enable_share_response import WebsiteCreateOrEnableShareResponse
    from .website_delete_response import WebsiteDeleteResponse
    from .website_disable_share_response import WebsiteDisableShareResponse
    from .website_geo_stats_response_item import WebsiteGeoStatsResponseItem
    from .website_get_lighthouse_report_response import WebsiteGetLighthouseReportResponse
    from .website_get_lighthouse_report_response_items_item import WebsiteGetLighthouseReportResponseItemsItem
    from .website_get_lighthouse_report_response_items_item_status import (
        WebsiteGetLighthouseReportResponseItemsItemStatus,
    )
    from .website_get_public_info_by_share_id_response import WebsiteGetPublicInfoByShareIdResponse
    from .website_get_public_metrics_by_share_id_request_range import WebsiteGetPublicMetricsByShareIdRequestRange
    from .website_get_public_metrics_by_share_id_request_type import WebsiteGetPublicMetricsByShareIdRequestType
    from .website_get_public_metrics_by_share_id_response_item import WebsiteGetPublicMetricsByShareIdResponseItem
    from .website_get_public_stats_by_share_id_request_range import WebsiteGetPublicStatsByShareIdRequestRange
    from .website_get_public_stats_by_share_id_response import WebsiteGetPublicStatsByShareIdResponse
    from .website_get_public_stats_by_share_id_response_average_visit_duration import (
        WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration,
    )
    from .website_get_public_stats_by_share_id_response_bounce_rate import (
        WebsiteGetPublicStatsByShareIdResponseBounceRate,
    )
    from .website_get_public_stats_by_share_id_response_pageviews import WebsiteGetPublicStatsByShareIdResponsePageviews
    from .website_get_public_stats_by_share_id_response_pageviews_trend_item import (
        WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem,
    )
    from .website_get_public_stats_by_share_id_response_visitors import WebsiteGetPublicStatsByShareIdResponseVisitors
    from .website_info_response import WebsiteInfoResponse
    from .website_metrics_request_type import WebsiteMetricsRequestType
    from .website_metrics_response_item import WebsiteMetricsResponseItem
    from .website_pageviews_response import WebsitePageviewsResponse
    from .website_stats_response import WebsiteStatsResponse
    from .website_stats_response_bounces import WebsiteStatsResponseBounces
    from .website_stats_response_pageviews import WebsiteStatsResponsePageviews
    from .website_stats_response_totaltime import WebsiteStatsResponseTotaltime
    from .website_stats_response_uniques import WebsiteStatsResponseUniques
    from .website_update_info_response import WebsiteUpdateInfoResponse
_dynamic_imports: typing.Dict[str, str] = {
    "WebsiteAddResponse": ".website_add_response",
    "WebsiteAllResponseItem": ".website_all_response_item",
    "WebsiteCreateOrEnableShareResponse": ".website_create_or_enable_share_response",
    "WebsiteDeleteResponse": ".website_delete_response",
    "WebsiteDisableShareResponse": ".website_disable_share_response",
    "WebsiteGeoStatsResponseItem": ".website_geo_stats_response_item",
    "WebsiteGetLighthouseReportResponse": ".website_get_lighthouse_report_response",
    "WebsiteGetLighthouseReportResponseItemsItem": ".website_get_lighthouse_report_response_items_item",
    "WebsiteGetLighthouseReportResponseItemsItemStatus": ".website_get_lighthouse_report_response_items_item_status",
    "WebsiteGetPublicInfoByShareIdResponse": ".website_get_public_info_by_share_id_response",
    "WebsiteGetPublicMetricsByShareIdRequestRange": ".website_get_public_metrics_by_share_id_request_range",
    "WebsiteGetPublicMetricsByShareIdRequestType": ".website_get_public_metrics_by_share_id_request_type",
    "WebsiteGetPublicMetricsByShareIdResponseItem": ".website_get_public_metrics_by_share_id_response_item",
    "WebsiteGetPublicStatsByShareIdRequestRange": ".website_get_public_stats_by_share_id_request_range",
    "WebsiteGetPublicStatsByShareIdResponse": ".website_get_public_stats_by_share_id_response",
    "WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration": ".website_get_public_stats_by_share_id_response_average_visit_duration",
    "WebsiteGetPublicStatsByShareIdResponseBounceRate": ".website_get_public_stats_by_share_id_response_bounce_rate",
    "WebsiteGetPublicStatsByShareIdResponsePageviews": ".website_get_public_stats_by_share_id_response_pageviews",
    "WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem": ".website_get_public_stats_by_share_id_response_pageviews_trend_item",
    "WebsiteGetPublicStatsByShareIdResponseVisitors": ".website_get_public_stats_by_share_id_response_visitors",
    "WebsiteInfoResponse": ".website_info_response",
    "WebsiteMetricsRequestType": ".website_metrics_request_type",
    "WebsiteMetricsResponseItem": ".website_metrics_response_item",
    "WebsitePageviewsResponse": ".website_pageviews_response",
    "WebsiteStatsResponse": ".website_stats_response",
    "WebsiteStatsResponseBounces": ".website_stats_response_bounces",
    "WebsiteStatsResponsePageviews": ".website_stats_response_pageviews",
    "WebsiteStatsResponseTotaltime": ".website_stats_response_totaltime",
    "WebsiteStatsResponseUniques": ".website_stats_response_uniques",
    "WebsiteUpdateInfoResponse": ".website_update_info_response",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "WebsiteAddResponse",
    "WebsiteAllResponseItem",
    "WebsiteCreateOrEnableShareResponse",
    "WebsiteDeleteResponse",
    "WebsiteDisableShareResponse",
    "WebsiteGeoStatsResponseItem",
    "WebsiteGetLighthouseReportResponse",
    "WebsiteGetLighthouseReportResponseItemsItem",
    "WebsiteGetLighthouseReportResponseItemsItemStatus",
    "WebsiteGetPublicInfoByShareIdResponse",
    "WebsiteGetPublicMetricsByShareIdRequestRange",
    "WebsiteGetPublicMetricsByShareIdRequestType",
    "WebsiteGetPublicMetricsByShareIdResponseItem",
    "WebsiteGetPublicStatsByShareIdRequestRange",
    "WebsiteGetPublicStatsByShareIdResponse",
    "WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration",
    "WebsiteGetPublicStatsByShareIdResponseBounceRate",
    "WebsiteGetPublicStatsByShareIdResponsePageviews",
    "WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem",
    "WebsiteGetPublicStatsByShareIdResponseVisitors",
    "WebsiteInfoResponse",
    "WebsiteMetricsRequestType",
    "WebsiteMetricsResponseItem",
    "WebsitePageviewsResponse",
    "WebsiteStatsResponse",
    "WebsiteStatsResponseBounces",
    "WebsiteStatsResponsePageviews",
    "WebsiteStatsResponseTotaltime",
    "WebsiteStatsResponseUniques",
    "WebsiteUpdateInfoResponse",
]
