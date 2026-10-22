



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateResponseRequestDataValue,
        CreateResponseRequestMeta,
        CreateResponseRequestMetaUserAgent,
        CreateResponseRequestVariablesValue,
        CreateResponseResponse,
        CreateResponseResponseDataValue,
        CreateResponseResponseMeta,
        CreateResponseResponseMetaUserAgent,
        CreateResponseResponseVariablesValue,
        DeleteResponseResponse,
        DeleteResponseResponseDataValue,
        DeleteResponseResponseMeta,
        DeleteResponseResponseMetaUserAgent,
        DeleteResponseResponseVariablesValue,
        GetResponseResponse,
        GetResponseResponseDataValue,
        GetResponseResponseMeta,
        GetResponseResponseMetaUserAgent,
        GetResponseResponseVariablesValue,
        GetResponsesRequestFilterDateField,
        GetResponsesRequestOrder,
        GetResponsesRequestSortBy,
        GetResponsesResponse,
        GetResponsesResponseDataItem,
        GetResponsesResponseDataItemDataValue,
        GetResponsesResponseDataItemMeta,
        GetResponsesResponseDataItemMetaUserAgent,
        GetResponsesResponseDataItemVariablesValue,
        GetResponsesResponseMeta,
        UpdateResponseRequestDataValue,
        UpdateResponseRequestVariablesValue,
        UpdateResponseResponse,
        UpdateResponseResponseDataValue,
        UpdateResponseResponseMeta,
        UpdateResponseResponseMetaUserAgent,
        UpdateResponseResponseVariablesValue,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateResponseRequestDataValue": ".types",
    "CreateResponseRequestMeta": ".types",
    "CreateResponseRequestMetaUserAgent": ".types",
    "CreateResponseRequestVariablesValue": ".types",
    "CreateResponseResponse": ".types",
    "CreateResponseResponseDataValue": ".types",
    "CreateResponseResponseMeta": ".types",
    "CreateResponseResponseMetaUserAgent": ".types",
    "CreateResponseResponseVariablesValue": ".types",
    "DeleteResponseResponse": ".types",
    "DeleteResponseResponseDataValue": ".types",
    "DeleteResponseResponseMeta": ".types",
    "DeleteResponseResponseMetaUserAgent": ".types",
    "DeleteResponseResponseVariablesValue": ".types",
    "GetResponseResponse": ".types",
    "GetResponseResponseDataValue": ".types",
    "GetResponseResponseMeta": ".types",
    "GetResponseResponseMetaUserAgent": ".types",
    "GetResponseResponseVariablesValue": ".types",
    "GetResponsesRequestFilterDateField": ".types",
    "GetResponsesRequestOrder": ".types",
    "GetResponsesRequestSortBy": ".types",
    "GetResponsesResponse": ".types",
    "GetResponsesResponseDataItem": ".types",
    "GetResponsesResponseDataItemDataValue": ".types",
    "GetResponsesResponseDataItemMeta": ".types",
    "GetResponsesResponseDataItemMetaUserAgent": ".types",
    "GetResponsesResponseDataItemVariablesValue": ".types",
    "GetResponsesResponseMeta": ".types",
    "UpdateResponseRequestDataValue": ".types",
    "UpdateResponseRequestVariablesValue": ".types",
    "UpdateResponseResponse": ".types",
    "UpdateResponseResponseDataValue": ".types",
    "UpdateResponseResponseMeta": ".types",
    "UpdateResponseResponseMetaUserAgent": ".types",
    "UpdateResponseResponseVariablesValue": ".types",
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
    "CreateResponseRequestDataValue",
    "CreateResponseRequestMeta",
    "CreateResponseRequestMetaUserAgent",
    "CreateResponseRequestVariablesValue",
    "CreateResponseResponse",
    "CreateResponseResponseDataValue",
    "CreateResponseResponseMeta",
    "CreateResponseResponseMetaUserAgent",
    "CreateResponseResponseVariablesValue",
    "DeleteResponseResponse",
    "DeleteResponseResponseDataValue",
    "DeleteResponseResponseMeta",
    "DeleteResponseResponseMetaUserAgent",
    "DeleteResponseResponseVariablesValue",
    "GetResponseResponse",
    "GetResponseResponseDataValue",
    "GetResponseResponseMeta",
    "GetResponseResponseMetaUserAgent",
    "GetResponseResponseVariablesValue",
    "GetResponsesRequestFilterDateField",
    "GetResponsesRequestOrder",
    "GetResponsesRequestSortBy",
    "GetResponsesResponse",
    "GetResponsesResponseDataItem",
    "GetResponsesResponseDataItemDataValue",
    "GetResponsesResponseDataItemMeta",
    "GetResponsesResponseDataItemMetaUserAgent",
    "GetResponsesResponseDataItemVariablesValue",
    "GetResponsesResponseMeta",
    "UpdateResponseRequestDataValue",
    "UpdateResponseRequestVariablesValue",
    "UpdateResponseResponse",
    "UpdateResponseResponseDataValue",
    "UpdateResponseResponseMeta",
    "UpdateResponseResponseMetaUserAgent",
    "UpdateResponseResponseVariablesValue",
]
