



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_item_items_request_body import CreateItemItemsRequestBody
    from .create_item_items_response import CreateItemItemsResponse
    from .create_item_items_response_field_data import CreateItemItemsResponseFieldData
    from .create_item_live_items_request_body import CreateItemLiveItemsRequestBody
    from .create_item_live_items_response import CreateItemLiveItemsResponse
    from .create_item_live_items_response_field_data import CreateItemLiveItemsResponseFieldData
    from .create_items_items_request_field_data import CreateItemsItemsRequestFieldData
    from .create_items_items_response import CreateItemsItemsResponse
    from .create_items_items_response_field_data import CreateItemsItemsResponseFieldData
    from .delete_items_items_request_items_item import DeleteItemsItemsRequestItemsItem
    from .delete_items_live_items_request_items_item import DeleteItemsLiveItemsRequestItemsItem
    from .get_item_items_response import GetItemItemsResponse
    from .get_item_items_response_field_data import GetItemItemsResponseFieldData
    from .get_item_live_items_response import GetItemLiveItemsResponse
    from .get_item_live_items_response_field_data import GetItemLiveItemsResponseFieldData
    from .item_i_ds import ItemIDs
    from .item_i_ds_with_locales import ItemIDsWithLocales
    from .item_i_ds_with_locales_items_item import ItemIDsWithLocalesItemsItem
    from .list_items_items_request_filter_value import ListItemsItemsRequestFilterValue
    from .list_items_items_request_filter_value_exists import ListItemsItemsRequestFilterValueExists
    from .list_items_items_request_filter_value_in import ListItemsItemsRequestFilterValueIn
    from .list_items_items_request_filter_value_nin import ListItemsItemsRequestFilterValueNin
    from .list_items_items_request_sort_by import ListItemsItemsRequestSortBy
    from .list_items_items_request_sort_order import ListItemsItemsRequestSortOrder
    from .list_items_items_request_sort_value import ListItemsItemsRequestSortValue
    from .list_items_items_response import ListItemsItemsResponse
    from .list_items_items_response_items_item import ListItemsItemsResponseItemsItem
    from .list_items_items_response_items_item_field_data import ListItemsItemsResponseItemsItemFieldData
    from .list_items_items_response_pagination import ListItemsItemsResponsePagination
    from .list_items_live_items_request_filter_value import ListItemsLiveItemsRequestFilterValue
    from .list_items_live_items_request_filter_value_exists import ListItemsLiveItemsRequestFilterValueExists
    from .list_items_live_items_request_filter_value_in import ListItemsLiveItemsRequestFilterValueIn
    from .list_items_live_items_request_filter_value_nin import ListItemsLiveItemsRequestFilterValueNin
    from .list_items_live_items_request_sort_by import ListItemsLiveItemsRequestSortBy
    from .list_items_live_items_request_sort_order import ListItemsLiveItemsRequestSortOrder
    from .list_items_live_items_request_sort_value import ListItemsLiveItemsRequestSortValue
    from .list_items_live_items_response import ListItemsLiveItemsResponse
    from .list_items_live_items_response_items_item import ListItemsLiveItemsResponseItemsItem
    from .list_items_live_items_response_items_item_field_data import ListItemsLiveItemsResponseItemsItemFieldData
    from .list_items_live_items_response_pagination import ListItemsLiveItemsResponsePagination
    from .multiple_cms_items_item import MultipleCmsItemsItem
    from .multiple_items import MultipleItems
    from .multiple_items_items_item import MultipleItemsItemsItem
    from .multiple_items_items_item_field_data import MultipleItemsItemsItemFieldData
    from .multiple_live_items import MultipleLiveItems
    from .multiple_live_items_items_item import MultipleLiveItemsItemsItem
    from .multiple_live_items_items_item_field_data import MultipleLiveItemsItemsItemFieldData
    from .publish_item_items_request_body import PublishItemItemsRequestBody
    from .publish_item_items_response import PublishItemItemsResponse
    from .single_cms_item import SingleCmsItem
    from .single_item import SingleItem
    from .single_item_field_data import SingleItemFieldData
    from .single_live_item import SingleLiveItem
    from .single_live_item_field_data import SingleLiveItemFieldData
    from .update_item_items_request_field_data import UpdateItemItemsRequestFieldData
    from .update_item_items_response import UpdateItemItemsResponse
    from .update_item_items_response_field_data import UpdateItemItemsResponseFieldData
    from .update_item_live_items_request_field_data import UpdateItemLiveItemsRequestFieldData
    from .update_item_live_items_response import UpdateItemLiveItemsResponse
    from .update_item_live_items_response_field_data import UpdateItemLiveItemsResponseFieldData
    from .update_items_items_request_items_item import UpdateItemsItemsRequestItemsItem
    from .update_items_items_request_items_item_field_data import UpdateItemsItemsRequestItemsItemFieldData
    from .update_items_items_response import UpdateItemsItemsResponse
    from .update_items_items_response_cms_locale_id import UpdateItemsItemsResponseCmsLocaleId
    from .update_items_items_response_cms_locale_id_field_data import UpdateItemsItemsResponseCmsLocaleIdFieldData
    from .update_items_items_response_items import UpdateItemsItemsResponseItems
    from .update_items_items_response_items_items_item import UpdateItemsItemsResponseItemsItemsItem
    from .update_items_items_response_items_items_item_field_data import UpdateItemsItemsResponseItemsItemsItemFieldData
    from .update_items_items_response_items_pagination import UpdateItemsItemsResponseItemsPagination
    from .update_items_live_items_request_items_item import UpdateItemsLiveItemsRequestItemsItem
    from .update_items_live_items_request_items_item_field_data import UpdateItemsLiveItemsRequestItemsItemFieldData
    from .update_items_live_items_response import UpdateItemsLiveItemsResponse
    from .update_items_live_items_response_items_item import UpdateItemsLiveItemsResponseItemsItem
    from .update_items_live_items_response_items_item_field_data import UpdateItemsLiveItemsResponseItemsItemFieldData
_dynamic_imports: typing.Dict[str, str] = {
    "CreateItemItemsRequestBody": ".create_item_items_request_body",
    "CreateItemItemsResponse": ".create_item_items_response",
    "CreateItemItemsResponseFieldData": ".create_item_items_response_field_data",
    "CreateItemLiveItemsRequestBody": ".create_item_live_items_request_body",
    "CreateItemLiveItemsResponse": ".create_item_live_items_response",
    "CreateItemLiveItemsResponseFieldData": ".create_item_live_items_response_field_data",
    "CreateItemsItemsRequestFieldData": ".create_items_items_request_field_data",
    "CreateItemsItemsResponse": ".create_items_items_response",
    "CreateItemsItemsResponseFieldData": ".create_items_items_response_field_data",
    "DeleteItemsItemsRequestItemsItem": ".delete_items_items_request_items_item",
    "DeleteItemsLiveItemsRequestItemsItem": ".delete_items_live_items_request_items_item",
    "GetItemItemsResponse": ".get_item_items_response",
    "GetItemItemsResponseFieldData": ".get_item_items_response_field_data",
    "GetItemLiveItemsResponse": ".get_item_live_items_response",
    "GetItemLiveItemsResponseFieldData": ".get_item_live_items_response_field_data",
    "ItemIDs": ".item_i_ds",
    "ItemIDsWithLocales": ".item_i_ds_with_locales",
    "ItemIDsWithLocalesItemsItem": ".item_i_ds_with_locales_items_item",
    "ListItemsItemsRequestFilterValue": ".list_items_items_request_filter_value",
    "ListItemsItemsRequestFilterValueExists": ".list_items_items_request_filter_value_exists",
    "ListItemsItemsRequestFilterValueIn": ".list_items_items_request_filter_value_in",
    "ListItemsItemsRequestFilterValueNin": ".list_items_items_request_filter_value_nin",
    "ListItemsItemsRequestSortBy": ".list_items_items_request_sort_by",
    "ListItemsItemsRequestSortOrder": ".list_items_items_request_sort_order",
    "ListItemsItemsRequestSortValue": ".list_items_items_request_sort_value",
    "ListItemsItemsResponse": ".list_items_items_response",
    "ListItemsItemsResponseItemsItem": ".list_items_items_response_items_item",
    "ListItemsItemsResponseItemsItemFieldData": ".list_items_items_response_items_item_field_data",
    "ListItemsItemsResponsePagination": ".list_items_items_response_pagination",
    "ListItemsLiveItemsRequestFilterValue": ".list_items_live_items_request_filter_value",
    "ListItemsLiveItemsRequestFilterValueExists": ".list_items_live_items_request_filter_value_exists",
    "ListItemsLiveItemsRequestFilterValueIn": ".list_items_live_items_request_filter_value_in",
    "ListItemsLiveItemsRequestFilterValueNin": ".list_items_live_items_request_filter_value_nin",
    "ListItemsLiveItemsRequestSortBy": ".list_items_live_items_request_sort_by",
    "ListItemsLiveItemsRequestSortOrder": ".list_items_live_items_request_sort_order",
    "ListItemsLiveItemsRequestSortValue": ".list_items_live_items_request_sort_value",
    "ListItemsLiveItemsResponse": ".list_items_live_items_response",
    "ListItemsLiveItemsResponseItemsItem": ".list_items_live_items_response_items_item",
    "ListItemsLiveItemsResponseItemsItemFieldData": ".list_items_live_items_response_items_item_field_data",
    "ListItemsLiveItemsResponsePagination": ".list_items_live_items_response_pagination",
    "MultipleCmsItemsItem": ".multiple_cms_items_item",
    "MultipleItems": ".multiple_items",
    "MultipleItemsItemsItem": ".multiple_items_items_item",
    "MultipleItemsItemsItemFieldData": ".multiple_items_items_item_field_data",
    "MultipleLiveItems": ".multiple_live_items",
    "MultipleLiveItemsItemsItem": ".multiple_live_items_items_item",
    "MultipleLiveItemsItemsItemFieldData": ".multiple_live_items_items_item_field_data",
    "PublishItemItemsRequestBody": ".publish_item_items_request_body",
    "PublishItemItemsResponse": ".publish_item_items_response",
    "SingleCmsItem": ".single_cms_item",
    "SingleItem": ".single_item",
    "SingleItemFieldData": ".single_item_field_data",
    "SingleLiveItem": ".single_live_item",
    "SingleLiveItemFieldData": ".single_live_item_field_data",
    "UpdateItemItemsRequestFieldData": ".update_item_items_request_field_data",
    "UpdateItemItemsResponse": ".update_item_items_response",
    "UpdateItemItemsResponseFieldData": ".update_item_items_response_field_data",
    "UpdateItemLiveItemsRequestFieldData": ".update_item_live_items_request_field_data",
    "UpdateItemLiveItemsResponse": ".update_item_live_items_response",
    "UpdateItemLiveItemsResponseFieldData": ".update_item_live_items_response_field_data",
    "UpdateItemsItemsRequestItemsItem": ".update_items_items_request_items_item",
    "UpdateItemsItemsRequestItemsItemFieldData": ".update_items_items_request_items_item_field_data",
    "UpdateItemsItemsResponse": ".update_items_items_response",
    "UpdateItemsItemsResponseCmsLocaleId": ".update_items_items_response_cms_locale_id",
    "UpdateItemsItemsResponseCmsLocaleIdFieldData": ".update_items_items_response_cms_locale_id_field_data",
    "UpdateItemsItemsResponseItems": ".update_items_items_response_items",
    "UpdateItemsItemsResponseItemsItemsItem": ".update_items_items_response_items_items_item",
    "UpdateItemsItemsResponseItemsItemsItemFieldData": ".update_items_items_response_items_items_item_field_data",
    "UpdateItemsItemsResponseItemsPagination": ".update_items_items_response_items_pagination",
    "UpdateItemsLiveItemsRequestItemsItem": ".update_items_live_items_request_items_item",
    "UpdateItemsLiveItemsRequestItemsItemFieldData": ".update_items_live_items_request_items_item_field_data",
    "UpdateItemsLiveItemsResponse": ".update_items_live_items_response",
    "UpdateItemsLiveItemsResponseItemsItem": ".update_items_live_items_response_items_item",
    "UpdateItemsLiveItemsResponseItemsItemFieldData": ".update_items_live_items_response_items_item_field_data",
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
    "CreateItemItemsRequestBody",
    "CreateItemItemsResponse",
    "CreateItemItemsResponseFieldData",
    "CreateItemLiveItemsRequestBody",
    "CreateItemLiveItemsResponse",
    "CreateItemLiveItemsResponseFieldData",
    "CreateItemsItemsRequestFieldData",
    "CreateItemsItemsResponse",
    "CreateItemsItemsResponseFieldData",
    "DeleteItemsItemsRequestItemsItem",
    "DeleteItemsLiveItemsRequestItemsItem",
    "GetItemItemsResponse",
    "GetItemItemsResponseFieldData",
    "GetItemLiveItemsResponse",
    "GetItemLiveItemsResponseFieldData",
    "ItemIDs",
    "ItemIDsWithLocales",
    "ItemIDsWithLocalesItemsItem",
    "ListItemsItemsRequestFilterValue",
    "ListItemsItemsRequestFilterValueExists",
    "ListItemsItemsRequestFilterValueIn",
    "ListItemsItemsRequestFilterValueNin",
    "ListItemsItemsRequestSortBy",
    "ListItemsItemsRequestSortOrder",
    "ListItemsItemsRequestSortValue",
    "ListItemsItemsResponse",
    "ListItemsItemsResponseItemsItem",
    "ListItemsItemsResponseItemsItemFieldData",
    "ListItemsItemsResponsePagination",
    "ListItemsLiveItemsRequestFilterValue",
    "ListItemsLiveItemsRequestFilterValueExists",
    "ListItemsLiveItemsRequestFilterValueIn",
    "ListItemsLiveItemsRequestFilterValueNin",
    "ListItemsLiveItemsRequestSortBy",
    "ListItemsLiveItemsRequestSortOrder",
    "ListItemsLiveItemsRequestSortValue",
    "ListItemsLiveItemsResponse",
    "ListItemsLiveItemsResponseItemsItem",
    "ListItemsLiveItemsResponseItemsItemFieldData",
    "ListItemsLiveItemsResponsePagination",
    "MultipleCmsItemsItem",
    "MultipleItems",
    "MultipleItemsItemsItem",
    "MultipleItemsItemsItemFieldData",
    "MultipleLiveItems",
    "MultipleLiveItemsItemsItem",
    "MultipleLiveItemsItemsItemFieldData",
    "PublishItemItemsRequestBody",
    "PublishItemItemsResponse",
    "SingleCmsItem",
    "SingleItem",
    "SingleItemFieldData",
    "SingleLiveItem",
    "SingleLiveItemFieldData",
    "UpdateItemItemsRequestFieldData",
    "UpdateItemItemsResponse",
    "UpdateItemItemsResponseFieldData",
    "UpdateItemLiveItemsRequestFieldData",
    "UpdateItemLiveItemsResponse",
    "UpdateItemLiveItemsResponseFieldData",
    "UpdateItemsItemsRequestItemsItem",
    "UpdateItemsItemsRequestItemsItemFieldData",
    "UpdateItemsItemsResponse",
    "UpdateItemsItemsResponseCmsLocaleId",
    "UpdateItemsItemsResponseCmsLocaleIdFieldData",
    "UpdateItemsItemsResponseItems",
    "UpdateItemsItemsResponseItemsItemsItem",
    "UpdateItemsItemsResponseItemsItemsItemFieldData",
    "UpdateItemsItemsResponseItemsPagination",
    "UpdateItemsLiveItemsRequestItemsItem",
    "UpdateItemsLiveItemsRequestItemsItemFieldData",
    "UpdateItemsLiveItemsResponse",
    "UpdateItemsLiveItemsResponseItemsItem",
    "UpdateItemsLiveItemsResponseItemsItemFieldData",
]
