



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .put_v1trace_request_trace import PutV1TraceRequestTrace
    from .put_v1trace_request_trace_eth import PutV1TraceRequestTraceEth
    from .put_v1trace_request_trace_ip import PutV1TraceRequestTraceIp
    from .put_v1trace_request_trace_switch import PutV1TraceRequestTraceSwitch
    from .put_v1trace_request_trace_tp import PutV1TraceRequestTraceTp
    from .put_v1trace_response import PutV1TraceResponse
    from .put_v1trace_response_result_item import PutV1TraceResponseResultItem
    from .put_v1trace_response_result_item_type import PutV1TraceResponseResultItemType
    from .put_v1traces_request_item import PutV1TracesRequestItem
    from .put_v1traces_request_item_trace import PutV1TracesRequestItemTrace
    from .put_v1traces_request_item_trace_eth import PutV1TracesRequestItemTraceEth
    from .put_v1traces_request_item_trace_ip import PutV1TracesRequestItemTraceIp
    from .put_v1traces_request_item_trace_switch import PutV1TracesRequestItemTraceSwitch
    from .put_v1traces_request_item_trace_tp import PutV1TracesRequestItemTraceTp
    from .put_v1traces_response import PutV1TracesResponse
    from .put_v1traces_response_result_item_item import PutV1TracesResponseResultItemItem
    from .put_v1traces_response_result_item_item_type import PutV1TracesResponseResultItemItemType
_dynamic_imports: typing.Dict[str, str] = {
    "PutV1TraceRequestTrace": ".put_v1trace_request_trace",
    "PutV1TraceRequestTraceEth": ".put_v1trace_request_trace_eth",
    "PutV1TraceRequestTraceIp": ".put_v1trace_request_trace_ip",
    "PutV1TraceRequestTraceSwitch": ".put_v1trace_request_trace_switch",
    "PutV1TraceRequestTraceTp": ".put_v1trace_request_trace_tp",
    "PutV1TraceResponse": ".put_v1trace_response",
    "PutV1TraceResponseResultItem": ".put_v1trace_response_result_item",
    "PutV1TraceResponseResultItemType": ".put_v1trace_response_result_item_type",
    "PutV1TracesRequestItem": ".put_v1traces_request_item",
    "PutV1TracesRequestItemTrace": ".put_v1traces_request_item_trace",
    "PutV1TracesRequestItemTraceEth": ".put_v1traces_request_item_trace_eth",
    "PutV1TracesRequestItemTraceIp": ".put_v1traces_request_item_trace_ip",
    "PutV1TracesRequestItemTraceSwitch": ".put_v1traces_request_item_trace_switch",
    "PutV1TracesRequestItemTraceTp": ".put_v1traces_request_item_trace_tp",
    "PutV1TracesResponse": ".put_v1traces_response",
    "PutV1TracesResponseResultItemItem": ".put_v1traces_response_result_item_item",
    "PutV1TracesResponseResultItemItemType": ".put_v1traces_response_result_item_item_type",
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
    "PutV1TraceRequestTrace",
    "PutV1TraceRequestTraceEth",
    "PutV1TraceRequestTraceIp",
    "PutV1TraceRequestTraceSwitch",
    "PutV1TraceRequestTraceTp",
    "PutV1TraceResponse",
    "PutV1TraceResponseResultItem",
    "PutV1TraceResponseResultItemType",
    "PutV1TracesRequestItem",
    "PutV1TracesRequestItemTrace",
    "PutV1TracesRequestItemTraceEth",
    "PutV1TracesRequestItemTraceIp",
    "PutV1TracesRequestItemTraceSwitch",
    "PutV1TracesRequestItemTraceTp",
    "PutV1TracesResponse",
    "PutV1TracesResponseResultItemItem",
    "PutV1TracesResponseResultItemItemType",
]
