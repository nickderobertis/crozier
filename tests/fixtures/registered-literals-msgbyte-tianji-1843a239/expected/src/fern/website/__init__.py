



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        WebsiteAddResponse,
        WebsiteAllResponseItem,
        WebsiteCreateOrEnableShareResponse,
        WebsiteDeleteResponse,
        WebsiteDisableShareResponse,
        WebsiteGeoStatsResponseItem,
        WebsiteGetLighthouseReportResponse,
        WebsiteGetLighthouseReportResponseItemsItem,
        WebsiteGetLighthouseReportResponseItemsItemStatus,
        WebsiteGetPublicInfoByShareIdResponse,
        WebsiteGetPublicMetricsByShareIdRequestRange,
        WebsiteGetPublicMetricsByShareIdRequestType,
        WebsiteGetPublicMetricsByShareIdResponseItem,
        WebsiteGetPublicStatsByShareIdRequestRange,
        WebsiteGetPublicStatsByShareIdResponse,
        WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration,
        WebsiteGetPublicStatsByShareIdResponseBounceRate,
        WebsiteGetPublicStatsByShareIdResponsePageviews,
        WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem,
        WebsiteGetPublicStatsByShareIdResponseVisitors,
        WebsiteInfoResponse,
        WebsiteMetricsRequestType,
        WebsiteMetricsResponseItem,
        WebsitePageviewsResponse,
        WebsiteStatsResponse,
        WebsiteStatsResponseBounces,
        WebsiteStatsResponsePageviews,
        WebsiteStatsResponseTotaltime,
        WebsiteStatsResponseUniques,
        WebsiteUpdateInfoResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "WebsiteAddResponse": ".types",
    "WebsiteAllResponseItem": ".types",
    "WebsiteCreateOrEnableShareResponse": ".types",
    "WebsiteDeleteResponse": ".types",
    "WebsiteDisableShareResponse": ".types",
    "WebsiteGeoStatsResponseItem": ".types",
    "WebsiteGetLighthouseReportResponse": ".types",
    "WebsiteGetLighthouseReportResponseItemsItem": ".types",
    "WebsiteGetLighthouseReportResponseItemsItemStatus": ".types",
    "WebsiteGetPublicInfoByShareIdResponse": ".types",
    "WebsiteGetPublicMetricsByShareIdRequestRange": ".types",
    "WebsiteGetPublicMetricsByShareIdRequestType": ".types",
    "WebsiteGetPublicMetricsByShareIdResponseItem": ".types",
    "WebsiteGetPublicStatsByShareIdRequestRange": ".types",
    "WebsiteGetPublicStatsByShareIdResponse": ".types",
    "WebsiteGetPublicStatsByShareIdResponseAverageVisitDuration": ".types",
    "WebsiteGetPublicStatsByShareIdResponseBounceRate": ".types",
    "WebsiteGetPublicStatsByShareIdResponsePageviews": ".types",
    "WebsiteGetPublicStatsByShareIdResponsePageviewsTrendItem": ".types",
    "WebsiteGetPublicStatsByShareIdResponseVisitors": ".types",
    "WebsiteInfoResponse": ".types",
    "WebsiteMetricsRequestType": ".types",
    "WebsiteMetricsResponseItem": ".types",
    "WebsitePageviewsResponse": ".types",
    "WebsiteStatsResponse": ".types",
    "WebsiteStatsResponseBounces": ".types",
    "WebsiteStatsResponsePageviews": ".types",
    "WebsiteStatsResponseTotaltime": ".types",
    "WebsiteStatsResponseUniques": ".types",
    "WebsiteUpdateInfoResponse": ".types",
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
