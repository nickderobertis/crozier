



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        LogTraceSpan,
        LogTraceSpanCost,
        LogTraceSpanTokens,
        LogTraceSpanTokensInput,
        LogTraceSpanToolCallsItem,
        V2ActionableForbiddenDetails,
        V2Error,
        V2ErrorError,
        V2ErrorErrorDetails,
        V2ForbiddenDetailCode,
        V2LogDetail,
        V2LogDetailCost,
        V2LogDetailCostItemsItem,
        V2LogDetailCostItemsItemCategory,
        V2LogDetailResponse,
        V2LogDetailStatus,
        V2LogDetailWorkflow,
        V2LogFile,
        V2LogListItem,
        V2LogListItemCost,
        V2LogListItemKind,
        V2LogListItemStatus,
        V2LogListItemWorkflow,
        V2LogListResponse,
        V2LogStats,
        V2LogStatsResponse,
        V2LogStatsSegment,
        V2LogStatsTimeBounds,
        V2WorkflowLogStats,
    )
    from .errors import (
        BadRequestError,
        ContentTooLargeError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import logs
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .logs import (
        GetLogStatsRequestLevel,
        ListLogsRequestDetails,
        ListLogsRequestLevel,
        ListLogsRequestSortBy,
        ListLogsRequestSortOrder,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetLogStatsRequestLevel": ".logs",
    "InternalServerError": ".errors",
    "ListLogsRequestDetails": ".logs",
    "ListLogsRequestLevel": ".logs",
    "ListLogsRequestSortBy": ".logs",
    "ListLogsRequestSortOrder": ".logs",
    "LogTraceSpan": ".types",
    "LogTraceSpanCost": ".types",
    "LogTraceSpanTokens": ".types",
    "LogTraceSpanTokensInput": ".types",
    "LogTraceSpanToolCallsItem": ".types",
    "NotFoundError": ".errors",
    "ServiceUnavailableError": ".errors",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "V2ActionableForbiddenDetails": ".types",
    "V2Error": ".types",
    "V2ErrorError": ".types",
    "V2ErrorErrorDetails": ".types",
    "V2ForbiddenDetailCode": ".types",
    "V2LogDetail": ".types",
    "V2LogDetailCost": ".types",
    "V2LogDetailCostItemsItem": ".types",
    "V2LogDetailCostItemsItemCategory": ".types",
    "V2LogDetailResponse": ".types",
    "V2LogDetailStatus": ".types",
    "V2LogDetailWorkflow": ".types",
    "V2LogFile": ".types",
    "V2LogListItem": ".types",
    "V2LogListItemCost": ".types",
    "V2LogListItemKind": ".types",
    "V2LogListItemStatus": ".types",
    "V2LogListItemWorkflow": ".types",
    "V2LogListResponse": ".types",
    "V2LogStats": ".types",
    "V2LogStatsResponse": ".types",
    "V2LogStatsSegment": ".types",
    "V2LogStatsTimeBounds": ".types",
    "V2WorkflowLogStats": ".types",
    "__version__": ".version",
    "logs": ".logs",
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
    "AsyncFernApi",
    "BadRequestError",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetLogStatsRequestLevel",
    "InternalServerError",
    "ListLogsRequestDetails",
    "ListLogsRequestLevel",
    "ListLogsRequestSortBy",
    "ListLogsRequestSortOrder",
    "LogTraceSpan",
    "LogTraceSpanCost",
    "LogTraceSpanTokens",
    "LogTraceSpanTokensInput",
    "LogTraceSpanToolCallsItem",
    "NotFoundError",
    "ServiceUnavailableError",
    "TooManyRequestsError",
    "UnauthorizedError",
    "V2ActionableForbiddenDetails",
    "V2Error",
    "V2ErrorError",
    "V2ErrorErrorDetails",
    "V2ForbiddenDetailCode",
    "V2LogDetail",
    "V2LogDetailCost",
    "V2LogDetailCostItemsItem",
    "V2LogDetailCostItemsItemCategory",
    "V2LogDetailResponse",
    "V2LogDetailStatus",
    "V2LogDetailWorkflow",
    "V2LogFile",
    "V2LogListItem",
    "V2LogListItemCost",
    "V2LogListItemKind",
    "V2LogListItemStatus",
    "V2LogListItemWorkflow",
    "V2LogListResponse",
    "V2LogStats",
    "V2LogStatsResponse",
    "V2LogStatsSegment",
    "V2LogStatsTimeBounds",
    "V2WorkflowLogStats",
    "__version__",
    "logs",
]
