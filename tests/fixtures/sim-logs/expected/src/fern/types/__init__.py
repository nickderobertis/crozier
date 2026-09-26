



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .log_trace_span import LogTraceSpan
    from .log_trace_span_cost import LogTraceSpanCost
    from .log_trace_span_tokens import LogTraceSpanTokens
    from .log_trace_span_tokens_input import LogTraceSpanTokensInput
    from .log_trace_span_tool_calls_item import LogTraceSpanToolCallsItem
    from .v2actionable_forbidden_details import V2ActionableForbiddenDetails
    from .v2error import V2Error
    from .v2error_error import V2ErrorError
    from .v2error_error_details import V2ErrorErrorDetails
    from .v2forbidden_detail_code import V2ForbiddenDetailCode
    from .v2log_detail import V2LogDetail
    from .v2log_detail_cost import V2LogDetailCost
    from .v2log_detail_cost_items_item import V2LogDetailCostItemsItem
    from .v2log_detail_cost_items_item_category import V2LogDetailCostItemsItemCategory
    from .v2log_detail_response import V2LogDetailResponse
    from .v2log_detail_status import V2LogDetailStatus
    from .v2log_detail_workflow import V2LogDetailWorkflow
    from .v2log_file import V2LogFile
    from .v2log_list_item import V2LogListItem
    from .v2log_list_item_cost import V2LogListItemCost
    from .v2log_list_item_kind import V2LogListItemKind
    from .v2log_list_item_status import V2LogListItemStatus
    from .v2log_list_item_workflow import V2LogListItemWorkflow
    from .v2log_list_response import V2LogListResponse
    from .v2log_stats import V2LogStats
    from .v2log_stats_response import V2LogStatsResponse
    from .v2log_stats_segment import V2LogStatsSegment
    from .v2log_stats_time_bounds import V2LogStatsTimeBounds
    from .v2workflow_log_stats import V2WorkflowLogStats
_dynamic_imports: typing.Dict[str, str] = {
    "LogTraceSpan": ".log_trace_span",
    "LogTraceSpanCost": ".log_trace_span_cost",
    "LogTraceSpanTokens": ".log_trace_span_tokens",
    "LogTraceSpanTokensInput": ".log_trace_span_tokens_input",
    "LogTraceSpanToolCallsItem": ".log_trace_span_tool_calls_item",
    "V2ActionableForbiddenDetails": ".v2actionable_forbidden_details",
    "V2Error": ".v2error",
    "V2ErrorError": ".v2error_error",
    "V2ErrorErrorDetails": ".v2error_error_details",
    "V2ForbiddenDetailCode": ".v2forbidden_detail_code",
    "V2LogDetail": ".v2log_detail",
    "V2LogDetailCost": ".v2log_detail_cost",
    "V2LogDetailCostItemsItem": ".v2log_detail_cost_items_item",
    "V2LogDetailCostItemsItemCategory": ".v2log_detail_cost_items_item_category",
    "V2LogDetailResponse": ".v2log_detail_response",
    "V2LogDetailStatus": ".v2log_detail_status",
    "V2LogDetailWorkflow": ".v2log_detail_workflow",
    "V2LogFile": ".v2log_file",
    "V2LogListItem": ".v2log_list_item",
    "V2LogListItemCost": ".v2log_list_item_cost",
    "V2LogListItemKind": ".v2log_list_item_kind",
    "V2LogListItemStatus": ".v2log_list_item_status",
    "V2LogListItemWorkflow": ".v2log_list_item_workflow",
    "V2LogListResponse": ".v2log_list_response",
    "V2LogStats": ".v2log_stats",
    "V2LogStatsResponse": ".v2log_stats_response",
    "V2LogStatsSegment": ".v2log_stats_segment",
    "V2LogStatsTimeBounds": ".v2log_stats_time_bounds",
    "V2WorkflowLogStats": ".v2workflow_log_stats",
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
    "LogTraceSpan",
    "LogTraceSpanCost",
    "LogTraceSpanTokens",
    "LogTraceSpanTokensInput",
    "LogTraceSpanToolCallsItem",
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
]
