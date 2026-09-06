



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BatchCreateCustomFontsRequestItemsItem,
        BatchCreateCustomFontsRequestItemsItemAxesItem,
        BatchCreateCustomFontsRequestItemsItemFontDisplay,
        BatchCreateCustomFontsResponse,
        BatchCreateCustomFontsResponseCreatedItem,
        BatchCreateCustomFontsResponseCreatedItemCustomFont,
        BatchCreateCustomFontsResponseCreatedItemCustomFontAxesItem,
        BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay,
        BatchCreateCustomFontsResponseCreatedItemCustomFontFormat,
        BatchCreateCustomFontsResponseCreatedItemUpload,
        BatchCreateCustomFontsResponseCreatedItemUploadFields,
        BatchCreateCustomFontsResponseFailedItem,
        BatchDeleteCustomFontsRequestItemsItem,
        BatchDeleteCustomFontsResponse,
        BatchDeleteCustomFontsResponseDeletedItem,
        BatchDeleteCustomFontsResponseFailedItem,
        CreateCustomFontsRequestAxesItem,
        CreateCustomFontsRequestFontDisplay,
        CreateCustomFontsResponse,
        CreateCustomFontsResponseCustomFont,
        CreateCustomFontsResponseCustomFontAxesItem,
        CreateCustomFontsResponseCustomFontFontDisplay,
        CreateCustomFontsResponseCustomFontFormat,
        CreateCustomFontsResponseUpload,
        CreateCustomFontsResponseUploadFields,
        GetCustomFontsResponse,
        GetCustomFontsResponseCustomFont,
        GetCustomFontsResponseCustomFontAxesItem,
        GetCustomFontsResponseCustomFontFontDisplay,
        GetCustomFontsResponseCustomFontFormat,
        ListCustomFontsResponse,
        ListCustomFontsResponseCustomFontsItem,
        ListCustomFontsResponseCustomFontsItemAxesItem,
        ListCustomFontsResponseCustomFontsItemFontDisplay,
        ListCustomFontsResponseCustomFontsItemFormat,
        ListCustomFontsResponsePagination,
        ReplaceFileCustomFontsRequestAxesItem,
        ReplaceFileCustomFontsResponse,
        ReplaceFileCustomFontsResponseCustomFont,
        ReplaceFileCustomFontsResponseCustomFontAxesItem,
        ReplaceFileCustomFontsResponseCustomFontFontDisplay,
        ReplaceFileCustomFontsResponseCustomFontFormat,
        ReplaceFileCustomFontsResponseUpload,
        ReplaceFileCustomFontsResponseUploadFields,
        UpdateCustomFontsRequestFontDisplay,
        UpdateCustomFontsResponse,
        UpdateCustomFontsResponseCustomFont,
        UpdateCustomFontsResponseCustomFontAxesItem,
        UpdateCustomFontsResponseCustomFontFontDisplay,
        UpdateCustomFontsResponseCustomFontFormat,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "BatchCreateCustomFontsRequestItemsItem": ".types",
    "BatchCreateCustomFontsRequestItemsItemAxesItem": ".types",
    "BatchCreateCustomFontsRequestItemsItemFontDisplay": ".types",
    "BatchCreateCustomFontsResponse": ".types",
    "BatchCreateCustomFontsResponseCreatedItem": ".types",
    "BatchCreateCustomFontsResponseCreatedItemCustomFont": ".types",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontAxesItem": ".types",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay": ".types",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFormat": ".types",
    "BatchCreateCustomFontsResponseCreatedItemUpload": ".types",
    "BatchCreateCustomFontsResponseCreatedItemUploadFields": ".types",
    "BatchCreateCustomFontsResponseFailedItem": ".types",
    "BatchDeleteCustomFontsRequestItemsItem": ".types",
    "BatchDeleteCustomFontsResponse": ".types",
    "BatchDeleteCustomFontsResponseDeletedItem": ".types",
    "BatchDeleteCustomFontsResponseFailedItem": ".types",
    "CreateCustomFontsRequestAxesItem": ".types",
    "CreateCustomFontsRequestFontDisplay": ".types",
    "CreateCustomFontsResponse": ".types",
    "CreateCustomFontsResponseCustomFont": ".types",
    "CreateCustomFontsResponseCustomFontAxesItem": ".types",
    "CreateCustomFontsResponseCustomFontFontDisplay": ".types",
    "CreateCustomFontsResponseCustomFontFormat": ".types",
    "CreateCustomFontsResponseUpload": ".types",
    "CreateCustomFontsResponseUploadFields": ".types",
    "GetCustomFontsResponse": ".types",
    "GetCustomFontsResponseCustomFont": ".types",
    "GetCustomFontsResponseCustomFontAxesItem": ".types",
    "GetCustomFontsResponseCustomFontFontDisplay": ".types",
    "GetCustomFontsResponseCustomFontFormat": ".types",
    "ListCustomFontsResponse": ".types",
    "ListCustomFontsResponseCustomFontsItem": ".types",
    "ListCustomFontsResponseCustomFontsItemAxesItem": ".types",
    "ListCustomFontsResponseCustomFontsItemFontDisplay": ".types",
    "ListCustomFontsResponseCustomFontsItemFormat": ".types",
    "ListCustomFontsResponsePagination": ".types",
    "ReplaceFileCustomFontsRequestAxesItem": ".types",
    "ReplaceFileCustomFontsResponse": ".types",
    "ReplaceFileCustomFontsResponseCustomFont": ".types",
    "ReplaceFileCustomFontsResponseCustomFontAxesItem": ".types",
    "ReplaceFileCustomFontsResponseCustomFontFontDisplay": ".types",
    "ReplaceFileCustomFontsResponseCustomFontFormat": ".types",
    "ReplaceFileCustomFontsResponseUpload": ".types",
    "ReplaceFileCustomFontsResponseUploadFields": ".types",
    "UpdateCustomFontsRequestFontDisplay": ".types",
    "UpdateCustomFontsResponse": ".types",
    "UpdateCustomFontsResponseCustomFont": ".types",
    "UpdateCustomFontsResponseCustomFontAxesItem": ".types",
    "UpdateCustomFontsResponseCustomFontFontDisplay": ".types",
    "UpdateCustomFontsResponseCustomFontFormat": ".types",
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
    "BatchCreateCustomFontsRequestItemsItem",
    "BatchCreateCustomFontsRequestItemsItemAxesItem",
    "BatchCreateCustomFontsRequestItemsItemFontDisplay",
    "BatchCreateCustomFontsResponse",
    "BatchCreateCustomFontsResponseCreatedItem",
    "BatchCreateCustomFontsResponseCreatedItemCustomFont",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontAxesItem",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFormat",
    "BatchCreateCustomFontsResponseCreatedItemUpload",
    "BatchCreateCustomFontsResponseCreatedItemUploadFields",
    "BatchCreateCustomFontsResponseFailedItem",
    "BatchDeleteCustomFontsRequestItemsItem",
    "BatchDeleteCustomFontsResponse",
    "BatchDeleteCustomFontsResponseDeletedItem",
    "BatchDeleteCustomFontsResponseFailedItem",
    "CreateCustomFontsRequestAxesItem",
    "CreateCustomFontsRequestFontDisplay",
    "CreateCustomFontsResponse",
    "CreateCustomFontsResponseCustomFont",
    "CreateCustomFontsResponseCustomFontAxesItem",
    "CreateCustomFontsResponseCustomFontFontDisplay",
    "CreateCustomFontsResponseCustomFontFormat",
    "CreateCustomFontsResponseUpload",
    "CreateCustomFontsResponseUploadFields",
    "GetCustomFontsResponse",
    "GetCustomFontsResponseCustomFont",
    "GetCustomFontsResponseCustomFontAxesItem",
    "GetCustomFontsResponseCustomFontFontDisplay",
    "GetCustomFontsResponseCustomFontFormat",
    "ListCustomFontsResponse",
    "ListCustomFontsResponseCustomFontsItem",
    "ListCustomFontsResponseCustomFontsItemAxesItem",
    "ListCustomFontsResponseCustomFontsItemFontDisplay",
    "ListCustomFontsResponseCustomFontsItemFormat",
    "ListCustomFontsResponsePagination",
    "ReplaceFileCustomFontsRequestAxesItem",
    "ReplaceFileCustomFontsResponse",
    "ReplaceFileCustomFontsResponseCustomFont",
    "ReplaceFileCustomFontsResponseCustomFontAxesItem",
    "ReplaceFileCustomFontsResponseCustomFontFontDisplay",
    "ReplaceFileCustomFontsResponseCustomFontFormat",
    "ReplaceFileCustomFontsResponseUpload",
    "ReplaceFileCustomFontsResponseUploadFields",
    "UpdateCustomFontsRequestFontDisplay",
    "UpdateCustomFontsResponse",
    "UpdateCustomFontsResponseCustomFont",
    "UpdateCustomFontsResponseCustomFontAxesItem",
    "UpdateCustomFontsResponseCustomFontFontDisplay",
    "UpdateCustomFontsResponseCustomFontFormat",
]
