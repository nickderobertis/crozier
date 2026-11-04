



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .log_list_request_direction import LogListRequestDirection
    from .log_list_response import LogListResponse
    from .log_list_response_data_item import LogListResponseDataItem
    from .log_list_response_data_item_attributes_item import LogListResponseDataItemAttributesItem
    from .log_list_response_data_item_attributes_item_value import LogListResponseDataItemAttributesItemValue
    from .log_list_response_data_item_body import LogListResponseDataItemBody
    from .trace_list_request_direction import TraceListRequestDirection
    from .trace_list_request_order_by import TraceListRequestOrderBy
    from .trace_list_response import TraceListResponse
    from .trace_list_response_data_item import TraceListResponseDataItem
    from .trace_list_response_data_item_attributes_item import TraceListResponseDataItemAttributesItem
    from .trace_list_response_data_item_attributes_item_value import TraceListResponseDataItemAttributesItemValue
    from .trace_list_response_data_item_status import TraceListResponseDataItemStatus
_dynamic_imports: typing.Dict[str, str] = {
    "LogListRequestDirection": ".log_list_request_direction",
    "LogListResponse": ".log_list_response",
    "LogListResponseDataItem": ".log_list_response_data_item",
    "LogListResponseDataItemAttributesItem": ".log_list_response_data_item_attributes_item",
    "LogListResponseDataItemAttributesItemValue": ".log_list_response_data_item_attributes_item_value",
    "LogListResponseDataItemBody": ".log_list_response_data_item_body",
    "TraceListRequestDirection": ".trace_list_request_direction",
    "TraceListRequestOrderBy": ".trace_list_request_order_by",
    "TraceListResponse": ".trace_list_response",
    "TraceListResponseDataItem": ".trace_list_response_data_item",
    "TraceListResponseDataItemAttributesItem": ".trace_list_response_data_item_attributes_item",
    "TraceListResponseDataItemAttributesItemValue": ".trace_list_response_data_item_attributes_item_value",
    "TraceListResponseDataItemStatus": ".trace_list_response_data_item_status",
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
    "LogListRequestDirection",
    "LogListResponse",
    "LogListResponseDataItem",
    "LogListResponseDataItemAttributesItem",
    "LogListResponseDataItemAttributesItemValue",
    "LogListResponseDataItemBody",
    "TraceListRequestDirection",
    "TraceListRequestOrderBy",
    "TraceListResponse",
    "TraceListResponseDataItem",
    "TraceListResponseDataItemAttributesItem",
    "TraceListResponseDataItemAttributesItemValue",
    "TraceListResponseDataItemStatus",
]
