



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostA2ARequestJsonrpc,
        PostA2ARequestMethod,
        PostA2ARequestParams,
        PostA2ARequestParamsHistoryLength,
        PostA2ARequestParamsMessage,
        PostA2ARequestParamsMessageMessage,
        PostA2ARequestParamsMessageMessagePartsItem,
        PostA2ARequestParamsMessageMessagePartsItemData,
        PostA2ARequestParamsMessageMessagePartsItemText,
        PostA2ARequestParamsMessageMessagePartsItem_Data,
        PostA2ARequestParamsMessageMessagePartsItem_Text,
        PostA2ARequestParamsMessageMessageRole,
        PostA2ARequestParamsTwo,
        PostA2AResponse,
        PostA2AResponseError,
        PostA2AResponseJsonrpc,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostA2ARequestJsonrpc": ".types",
    "PostA2ARequestMethod": ".types",
    "PostA2ARequestParams": ".types",
    "PostA2ARequestParamsHistoryLength": ".types",
    "PostA2ARequestParamsMessage": ".types",
    "PostA2ARequestParamsMessageMessage": ".types",
    "PostA2ARequestParamsMessageMessagePartsItem": ".types",
    "PostA2ARequestParamsMessageMessagePartsItemData": ".types",
    "PostA2ARequestParamsMessageMessagePartsItemText": ".types",
    "PostA2ARequestParamsMessageMessagePartsItem_Data": ".types",
    "PostA2ARequestParamsMessageMessagePartsItem_Text": ".types",
    "PostA2ARequestParamsMessageMessageRole": ".types",
    "PostA2ARequestParamsTwo": ".types",
    "PostA2AResponse": ".types",
    "PostA2AResponseError": ".types",
    "PostA2AResponseJsonrpc": ".types",
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
