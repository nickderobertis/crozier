



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_a2a_request_jsonrpc import PostA2ARequestJsonrpc
    from .post_a2a_request_method import PostA2ARequestMethod
    from .post_a2a_request_params import PostA2ARequestParams
    from .post_a2a_request_params_history_length import PostA2ARequestParamsHistoryLength
    from .post_a2a_request_params_message import PostA2ARequestParamsMessage
    from .post_a2a_request_params_message_message import PostA2ARequestParamsMessageMessage
    from .post_a2a_request_params_message_message_parts_item import (
        PostA2ARequestParamsMessageMessagePartsItem,
        PostA2ARequestParamsMessageMessagePartsItem_Data,
        PostA2ARequestParamsMessageMessagePartsItem_Text,
    )
    from .post_a2a_request_params_message_message_parts_item_data import PostA2ARequestParamsMessageMessagePartsItemData
    from .post_a2a_request_params_message_message_parts_item_text import PostA2ARequestParamsMessageMessagePartsItemText
    from .post_a2a_request_params_message_message_role import PostA2ARequestParamsMessageMessageRole
    from .post_a2a_request_params_two import PostA2ARequestParamsTwo
    from .post_a2a_response import PostA2AResponse
    from .post_a2a_response_error import PostA2AResponseError
    from .post_a2a_response_jsonrpc import PostA2AResponseJsonrpc
_dynamic_imports: typing.Dict[str, str] = {
    "PostA2ARequestJsonrpc": ".post_a2a_request_jsonrpc",
    "PostA2ARequestMethod": ".post_a2a_request_method",
    "PostA2ARequestParams": ".post_a2a_request_params",
    "PostA2ARequestParamsHistoryLength": ".post_a2a_request_params_history_length",
    "PostA2ARequestParamsMessage": ".post_a2a_request_params_message",
    "PostA2ARequestParamsMessageMessage": ".post_a2a_request_params_message_message",
    "PostA2ARequestParamsMessageMessagePartsItem": ".post_a2a_request_params_message_message_parts_item",
    "PostA2ARequestParamsMessageMessagePartsItemData": ".post_a2a_request_params_message_message_parts_item_data",
    "PostA2ARequestParamsMessageMessagePartsItemText": ".post_a2a_request_params_message_message_parts_item_text",
    "PostA2ARequestParamsMessageMessagePartsItem_Data": ".post_a2a_request_params_message_message_parts_item",
    "PostA2ARequestParamsMessageMessagePartsItem_Text": ".post_a2a_request_params_message_message_parts_item",
    "PostA2ARequestParamsMessageMessageRole": ".post_a2a_request_params_message_message_role",
    "PostA2ARequestParamsTwo": ".post_a2a_request_params_two",
    "PostA2AResponse": ".post_a2a_response",
    "PostA2AResponseError": ".post_a2a_response_error",
    "PostA2AResponseJsonrpc": ".post_a2a_response_jsonrpc",
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
    "PostA2ARequestJsonrpc",
    "PostA2ARequestMethod",
    "PostA2ARequestParams",
    "PostA2ARequestParamsHistoryLength",
    "PostA2ARequestParamsMessage",
    "PostA2ARequestParamsMessageMessage",
    "PostA2ARequestParamsMessageMessagePartsItem",
    "PostA2ARequestParamsMessageMessagePartsItemData",
    "PostA2ARequestParamsMessageMessagePartsItemText",
    "PostA2ARequestParamsMessageMessagePartsItem_Data",
    "PostA2ARequestParamsMessageMessagePartsItem_Text",
    "PostA2ARequestParamsMessageMessageRole",
    "PostA2ARequestParamsTwo",
    "PostA2AResponse",
    "PostA2AResponseError",
    "PostA2AResponseJsonrpc",
]
