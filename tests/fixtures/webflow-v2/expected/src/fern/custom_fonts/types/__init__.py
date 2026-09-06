



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .batch_create_custom_fonts_request_items_item import BatchCreateCustomFontsRequestItemsItem
    from .batch_create_custom_fonts_request_items_item_axes_item import BatchCreateCustomFontsRequestItemsItemAxesItem
    from .batch_create_custom_fonts_request_items_item_font_display import (
        BatchCreateCustomFontsRequestItemsItemFontDisplay,
    )
    from .batch_create_custom_fonts_response import BatchCreateCustomFontsResponse
    from .batch_create_custom_fonts_response_created_item import BatchCreateCustomFontsResponseCreatedItem
    from .batch_create_custom_fonts_response_created_item_custom_font import (
        BatchCreateCustomFontsResponseCreatedItemCustomFont,
    )
    from .batch_create_custom_fonts_response_created_item_custom_font_axes_item import (
        BatchCreateCustomFontsResponseCreatedItemCustomFontAxesItem,
    )
    from .batch_create_custom_fonts_response_created_item_custom_font_font_display import (
        BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay,
    )
    from .batch_create_custom_fonts_response_created_item_custom_font_format import (
        BatchCreateCustomFontsResponseCreatedItemCustomFontFormat,
    )
    from .batch_create_custom_fonts_response_created_item_upload import BatchCreateCustomFontsResponseCreatedItemUpload
    from .batch_create_custom_fonts_response_created_item_upload_fields import (
        BatchCreateCustomFontsResponseCreatedItemUploadFields,
    )
    from .batch_create_custom_fonts_response_failed_item import BatchCreateCustomFontsResponseFailedItem
    from .batch_delete_custom_fonts_request_items_item import BatchDeleteCustomFontsRequestItemsItem
    from .batch_delete_custom_fonts_response import BatchDeleteCustomFontsResponse
    from .batch_delete_custom_fonts_response_deleted_item import BatchDeleteCustomFontsResponseDeletedItem
    from .batch_delete_custom_fonts_response_failed_item import BatchDeleteCustomFontsResponseFailedItem
    from .create_custom_fonts_request_axes_item import CreateCustomFontsRequestAxesItem
    from .create_custom_fonts_request_font_display import CreateCustomFontsRequestFontDisplay
    from .create_custom_fonts_response import CreateCustomFontsResponse
    from .create_custom_fonts_response_custom_font import CreateCustomFontsResponseCustomFont
    from .create_custom_fonts_response_custom_font_axes_item import CreateCustomFontsResponseCustomFontAxesItem
    from .create_custom_fonts_response_custom_font_font_display import CreateCustomFontsResponseCustomFontFontDisplay
    from .create_custom_fonts_response_custom_font_format import CreateCustomFontsResponseCustomFontFormat
    from .create_custom_fonts_response_upload import CreateCustomFontsResponseUpload
    from .create_custom_fonts_response_upload_fields import CreateCustomFontsResponseUploadFields
    from .get_custom_fonts_response import GetCustomFontsResponse
    from .get_custom_fonts_response_custom_font import GetCustomFontsResponseCustomFont
    from .get_custom_fonts_response_custom_font_axes_item import GetCustomFontsResponseCustomFontAxesItem
    from .get_custom_fonts_response_custom_font_font_display import GetCustomFontsResponseCustomFontFontDisplay
    from .get_custom_fonts_response_custom_font_format import GetCustomFontsResponseCustomFontFormat
    from .list_custom_fonts_response import ListCustomFontsResponse
    from .list_custom_fonts_response_custom_fonts_item import ListCustomFontsResponseCustomFontsItem
    from .list_custom_fonts_response_custom_fonts_item_axes_item import ListCustomFontsResponseCustomFontsItemAxesItem
    from .list_custom_fonts_response_custom_fonts_item_font_display import (
        ListCustomFontsResponseCustomFontsItemFontDisplay,
    )
    from .list_custom_fonts_response_custom_fonts_item_format import ListCustomFontsResponseCustomFontsItemFormat
    from .list_custom_fonts_response_pagination import ListCustomFontsResponsePagination
    from .replace_file_custom_fonts_request_axes_item import ReplaceFileCustomFontsRequestAxesItem
    from .replace_file_custom_fonts_response import ReplaceFileCustomFontsResponse
    from .replace_file_custom_fonts_response_custom_font import ReplaceFileCustomFontsResponseCustomFont
    from .replace_file_custom_fonts_response_custom_font_axes_item import (
        ReplaceFileCustomFontsResponseCustomFontAxesItem,
    )
    from .replace_file_custom_fonts_response_custom_font_font_display import (
        ReplaceFileCustomFontsResponseCustomFontFontDisplay,
    )
    from .replace_file_custom_fonts_response_custom_font_format import ReplaceFileCustomFontsResponseCustomFontFormat
    from .replace_file_custom_fonts_response_upload import ReplaceFileCustomFontsResponseUpload
    from .replace_file_custom_fonts_response_upload_fields import ReplaceFileCustomFontsResponseUploadFields
    from .update_custom_fonts_request_font_display import UpdateCustomFontsRequestFontDisplay
    from .update_custom_fonts_response import UpdateCustomFontsResponse
    from .update_custom_fonts_response_custom_font import UpdateCustomFontsResponseCustomFont
    from .update_custom_fonts_response_custom_font_axes_item import UpdateCustomFontsResponseCustomFontAxesItem
    from .update_custom_fonts_response_custom_font_font_display import UpdateCustomFontsResponseCustomFontFontDisplay
    from .update_custom_fonts_response_custom_font_format import UpdateCustomFontsResponseCustomFontFormat
_dynamic_imports: typing.Dict[str, str] = {
    "BatchCreateCustomFontsRequestItemsItem": ".batch_create_custom_fonts_request_items_item",
    "BatchCreateCustomFontsRequestItemsItemAxesItem": ".batch_create_custom_fonts_request_items_item_axes_item",
    "BatchCreateCustomFontsRequestItemsItemFontDisplay": ".batch_create_custom_fonts_request_items_item_font_display",
    "BatchCreateCustomFontsResponse": ".batch_create_custom_fonts_response",
    "BatchCreateCustomFontsResponseCreatedItem": ".batch_create_custom_fonts_response_created_item",
    "BatchCreateCustomFontsResponseCreatedItemCustomFont": ".batch_create_custom_fonts_response_created_item_custom_font",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontAxesItem": ".batch_create_custom_fonts_response_created_item_custom_font_axes_item",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFontDisplay": ".batch_create_custom_fonts_response_created_item_custom_font_font_display",
    "BatchCreateCustomFontsResponseCreatedItemCustomFontFormat": ".batch_create_custom_fonts_response_created_item_custom_font_format",
    "BatchCreateCustomFontsResponseCreatedItemUpload": ".batch_create_custom_fonts_response_created_item_upload",
    "BatchCreateCustomFontsResponseCreatedItemUploadFields": ".batch_create_custom_fonts_response_created_item_upload_fields",
    "BatchCreateCustomFontsResponseFailedItem": ".batch_create_custom_fonts_response_failed_item",
    "BatchDeleteCustomFontsRequestItemsItem": ".batch_delete_custom_fonts_request_items_item",
    "BatchDeleteCustomFontsResponse": ".batch_delete_custom_fonts_response",
    "BatchDeleteCustomFontsResponseDeletedItem": ".batch_delete_custom_fonts_response_deleted_item",
    "BatchDeleteCustomFontsResponseFailedItem": ".batch_delete_custom_fonts_response_failed_item",
    "CreateCustomFontsRequestAxesItem": ".create_custom_fonts_request_axes_item",
    "CreateCustomFontsRequestFontDisplay": ".create_custom_fonts_request_font_display",
    "CreateCustomFontsResponse": ".create_custom_fonts_response",
    "CreateCustomFontsResponseCustomFont": ".create_custom_fonts_response_custom_font",
    "CreateCustomFontsResponseCustomFontAxesItem": ".create_custom_fonts_response_custom_font_axes_item",
    "CreateCustomFontsResponseCustomFontFontDisplay": ".create_custom_fonts_response_custom_font_font_display",
    "CreateCustomFontsResponseCustomFontFormat": ".create_custom_fonts_response_custom_font_format",
    "CreateCustomFontsResponseUpload": ".create_custom_fonts_response_upload",
    "CreateCustomFontsResponseUploadFields": ".create_custom_fonts_response_upload_fields",
    "GetCustomFontsResponse": ".get_custom_fonts_response",
    "GetCustomFontsResponseCustomFont": ".get_custom_fonts_response_custom_font",
    "GetCustomFontsResponseCustomFontAxesItem": ".get_custom_fonts_response_custom_font_axes_item",
    "GetCustomFontsResponseCustomFontFontDisplay": ".get_custom_fonts_response_custom_font_font_display",
    "GetCustomFontsResponseCustomFontFormat": ".get_custom_fonts_response_custom_font_format",
    "ListCustomFontsResponse": ".list_custom_fonts_response",
    "ListCustomFontsResponseCustomFontsItem": ".list_custom_fonts_response_custom_fonts_item",
    "ListCustomFontsResponseCustomFontsItemAxesItem": ".list_custom_fonts_response_custom_fonts_item_axes_item",
    "ListCustomFontsResponseCustomFontsItemFontDisplay": ".list_custom_fonts_response_custom_fonts_item_font_display",
    "ListCustomFontsResponseCustomFontsItemFormat": ".list_custom_fonts_response_custom_fonts_item_format",
    "ListCustomFontsResponsePagination": ".list_custom_fonts_response_pagination",
    "ReplaceFileCustomFontsRequestAxesItem": ".replace_file_custom_fonts_request_axes_item",
    "ReplaceFileCustomFontsResponse": ".replace_file_custom_fonts_response",
    "ReplaceFileCustomFontsResponseCustomFont": ".replace_file_custom_fonts_response_custom_font",
    "ReplaceFileCustomFontsResponseCustomFontAxesItem": ".replace_file_custom_fonts_response_custom_font_axes_item",
    "ReplaceFileCustomFontsResponseCustomFontFontDisplay": ".replace_file_custom_fonts_response_custom_font_font_display",
    "ReplaceFileCustomFontsResponseCustomFontFormat": ".replace_file_custom_fonts_response_custom_font_format",
    "ReplaceFileCustomFontsResponseUpload": ".replace_file_custom_fonts_response_upload",
    "ReplaceFileCustomFontsResponseUploadFields": ".replace_file_custom_fonts_response_upload_fields",
    "UpdateCustomFontsRequestFontDisplay": ".update_custom_fonts_request_font_display",
    "UpdateCustomFontsResponse": ".update_custom_fonts_response",
    "UpdateCustomFontsResponseCustomFont": ".update_custom_fonts_response_custom_font",
    "UpdateCustomFontsResponseCustomFontAxesItem": ".update_custom_fonts_response_custom_font_axes_item",
    "UpdateCustomFontsResponseCustomFontFontDisplay": ".update_custom_fonts_response_custom_font_font_display",
    "UpdateCustomFontsResponseCustomFontFormat": ".update_custom_fonts_response_custom_font_format",
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
