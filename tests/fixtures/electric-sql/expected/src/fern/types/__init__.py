



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .conflict_error_body_item import ConflictErrorBodyItem
    from .conflict_error_body_item_headers import ConflictErrorBodyItemHeaders
    from .conflict_error_body_item_headers_control import ConflictErrorBodyItemHeadersControl
    from .get_v1shape_request_log import GetV1ShapeRequestLog
    from .get_v1shape_request_replica import GetV1ShapeRequestReplica
    from .get_v1shape_response import GetV1ShapeResponse
    from .get_v1shape_response_data import GetV1ShapeResponseData
    from .get_v1shape_response_data_data_item import GetV1ShapeResponseDataDataItem
    from .get_v1shape_response_data_data_item_headers import GetV1ShapeResponseDataDataItemHeaders
    from .get_v1shape_response_data_data_item_headers_operation import GetV1ShapeResponseDataDataItemHeadersOperation
    from .get_v1shape_response_data_metadata import GetV1ShapeResponseDataMetadata
    from .get_v1shape_response_zero_item import GetV1ShapeResponseZeroItem
    from .get_v1shape_response_zero_item_headers import GetV1ShapeResponseZeroItemHeaders
    from .get_v1shape_response_zero_item_headers_control import GetV1ShapeResponseZeroItemHeadersControl
    from .get_v1shape_response_zero_item_headers_operation import GetV1ShapeResponseZeroItemHeadersOperation
    from .post_v1shape_request_log import PostV1ShapeRequestLog
    from .post_v1shape_request_replica import PostV1ShapeRequestReplica
    from .post_v1shape_response import PostV1ShapeResponse
    from .post_v1shape_response_data_item import PostV1ShapeResponseDataItem
    from .post_v1shape_response_metadata import PostV1ShapeResponseMetadata
    from .too_many_requests_error_body import TooManyRequestsErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "ConflictErrorBodyItem": ".conflict_error_body_item",
    "ConflictErrorBodyItemHeaders": ".conflict_error_body_item_headers",
    "ConflictErrorBodyItemHeadersControl": ".conflict_error_body_item_headers_control",
    "GetV1ShapeRequestLog": ".get_v1shape_request_log",
    "GetV1ShapeRequestReplica": ".get_v1shape_request_replica",
    "GetV1ShapeResponse": ".get_v1shape_response",
    "GetV1ShapeResponseData": ".get_v1shape_response_data",
    "GetV1ShapeResponseDataDataItem": ".get_v1shape_response_data_data_item",
    "GetV1ShapeResponseDataDataItemHeaders": ".get_v1shape_response_data_data_item_headers",
    "GetV1ShapeResponseDataDataItemHeadersOperation": ".get_v1shape_response_data_data_item_headers_operation",
    "GetV1ShapeResponseDataMetadata": ".get_v1shape_response_data_metadata",
    "GetV1ShapeResponseZeroItem": ".get_v1shape_response_zero_item",
    "GetV1ShapeResponseZeroItemHeaders": ".get_v1shape_response_zero_item_headers",
    "GetV1ShapeResponseZeroItemHeadersControl": ".get_v1shape_response_zero_item_headers_control",
    "GetV1ShapeResponseZeroItemHeadersOperation": ".get_v1shape_response_zero_item_headers_operation",
    "PostV1ShapeRequestLog": ".post_v1shape_request_log",
    "PostV1ShapeRequestReplica": ".post_v1shape_request_replica",
    "PostV1ShapeResponse": ".post_v1shape_response",
    "PostV1ShapeResponseDataItem": ".post_v1shape_response_data_item",
    "PostV1ShapeResponseMetadata": ".post_v1shape_response_metadata",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
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
    "ConflictErrorBodyItem",
    "ConflictErrorBodyItemHeaders",
    "ConflictErrorBodyItemHeadersControl",
    "GetV1ShapeRequestLog",
    "GetV1ShapeRequestReplica",
    "GetV1ShapeResponse",
    "GetV1ShapeResponseData",
    "GetV1ShapeResponseDataDataItem",
    "GetV1ShapeResponseDataDataItemHeaders",
    "GetV1ShapeResponseDataDataItemHeadersOperation",
    "GetV1ShapeResponseDataMetadata",
    "GetV1ShapeResponseZeroItem",
    "GetV1ShapeResponseZeroItemHeaders",
    "GetV1ShapeResponseZeroItemHeadersControl",
    "GetV1ShapeResponseZeroItemHeadersOperation",
    "PostV1ShapeRequestLog",
    "PostV1ShapeRequestReplica",
    "PostV1ShapeResponse",
    "PostV1ShapeResponseDataItem",
    "PostV1ShapeResponseMetadata",
    "TooManyRequestsErrorBody",
]
