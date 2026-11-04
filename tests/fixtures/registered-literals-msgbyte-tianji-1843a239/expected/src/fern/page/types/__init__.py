



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .page_create_page_response import (
        PageCreatePageResponse,
        PageCreatePageResponse_Static,
        PageCreatePageResponse_Status,
    )
    from .page_create_page_response_static import PageCreatePageResponseStatic
    from .page_create_page_response_status import PageCreatePageResponseStatus
    from .page_create_page_response_status_monitor_list_item import PageCreatePageResponseStatusMonitorListItem
    from .page_delete_page_response import (
        PageDeletePageResponse,
        PageDeletePageResponse_Static,
        PageDeletePageResponse_Status,
    )
    from .page_delete_page_response_static import PageDeletePageResponseStatic
    from .page_delete_page_response_status import PageDeletePageResponseStatus
    from .page_delete_page_response_status_monitor_list_item import PageDeletePageResponseStatusMonitorListItem
    from .page_edit_page_response import PageEditPageResponse, PageEditPageResponse_Static, PageEditPageResponse_Status
    from .page_edit_page_response_static import PageEditPageResponseStatic
    from .page_edit_page_response_status import PageEditPageResponseStatus
    from .page_edit_page_response_status_monitor_list_item import PageEditPageResponseStatusMonitorListItem
    from .page_get_all_pages_request_type import PageGetAllPagesRequestType
    from .page_get_all_pages_response_item import (
        PageGetAllPagesResponseItem,
        PageGetAllPagesResponseItem_Static,
        PageGetAllPagesResponseItem_Status,
    )
    from .page_get_all_pages_response_item_static import PageGetAllPagesResponseItemStatic
    from .page_get_all_pages_response_item_status import PageGetAllPagesResponseItemStatus
    from .page_get_all_pages_response_item_status_monitor_list_item import (
        PageGetAllPagesResponseItemStatusMonitorListItem,
    )
    from .page_get_page_info_response import (
        PageGetPageInfoResponse,
        PageGetPageInfoResponse_Static,
        PageGetPageInfoResponse_Status,
    )
    from .page_get_page_info_response_static import PageGetPageInfoResponseStatic
    from .page_get_page_info_response_status import PageGetPageInfoResponseStatus
    from .page_get_page_info_response_status_monitor_list_item import PageGetPageInfoResponseStatusMonitorListItem
_dynamic_imports: typing.Dict[str, str] = {
    "PageCreatePageResponse": ".page_create_page_response",
    "PageCreatePageResponseStatic": ".page_create_page_response_static",
    "PageCreatePageResponseStatus": ".page_create_page_response_status",
    "PageCreatePageResponseStatusMonitorListItem": ".page_create_page_response_status_monitor_list_item",
    "PageCreatePageResponse_Static": ".page_create_page_response",
    "PageCreatePageResponse_Status": ".page_create_page_response",
    "PageDeletePageResponse": ".page_delete_page_response",
    "PageDeletePageResponseStatic": ".page_delete_page_response_static",
    "PageDeletePageResponseStatus": ".page_delete_page_response_status",
    "PageDeletePageResponseStatusMonitorListItem": ".page_delete_page_response_status_monitor_list_item",
    "PageDeletePageResponse_Static": ".page_delete_page_response",
    "PageDeletePageResponse_Status": ".page_delete_page_response",
    "PageEditPageResponse": ".page_edit_page_response",
    "PageEditPageResponseStatic": ".page_edit_page_response_static",
    "PageEditPageResponseStatus": ".page_edit_page_response_status",
    "PageEditPageResponseStatusMonitorListItem": ".page_edit_page_response_status_monitor_list_item",
    "PageEditPageResponse_Static": ".page_edit_page_response",
    "PageEditPageResponse_Status": ".page_edit_page_response",
    "PageGetAllPagesRequestType": ".page_get_all_pages_request_type",
    "PageGetAllPagesResponseItem": ".page_get_all_pages_response_item",
    "PageGetAllPagesResponseItemStatic": ".page_get_all_pages_response_item_static",
    "PageGetAllPagesResponseItemStatus": ".page_get_all_pages_response_item_status",
    "PageGetAllPagesResponseItemStatusMonitorListItem": ".page_get_all_pages_response_item_status_monitor_list_item",
    "PageGetAllPagesResponseItem_Static": ".page_get_all_pages_response_item",
    "PageGetAllPagesResponseItem_Status": ".page_get_all_pages_response_item",
    "PageGetPageInfoResponse": ".page_get_page_info_response",
    "PageGetPageInfoResponseStatic": ".page_get_page_info_response_static",
    "PageGetPageInfoResponseStatus": ".page_get_page_info_response_status",
    "PageGetPageInfoResponseStatusMonitorListItem": ".page_get_page_info_response_status_monitor_list_item",
    "PageGetPageInfoResponse_Static": ".page_get_page_info_response",
    "PageGetPageInfoResponse_Status": ".page_get_page_info_response",
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
    "PageCreatePageResponse",
    "PageCreatePageResponseStatic",
    "PageCreatePageResponseStatus",
    "PageCreatePageResponseStatusMonitorListItem",
    "PageCreatePageResponse_Static",
    "PageCreatePageResponse_Status",
    "PageDeletePageResponse",
    "PageDeletePageResponseStatic",
    "PageDeletePageResponseStatus",
    "PageDeletePageResponseStatusMonitorListItem",
    "PageDeletePageResponse_Static",
    "PageDeletePageResponse_Status",
    "PageEditPageResponse",
    "PageEditPageResponseStatic",
    "PageEditPageResponseStatus",
    "PageEditPageResponseStatusMonitorListItem",
    "PageEditPageResponse_Static",
    "PageEditPageResponse_Status",
    "PageGetAllPagesRequestType",
    "PageGetAllPagesResponseItem",
    "PageGetAllPagesResponseItemStatic",
    "PageGetAllPagesResponseItemStatus",
    "PageGetAllPagesResponseItemStatusMonitorListItem",
    "PageGetAllPagesResponseItem_Static",
    "PageGetAllPagesResponseItem_Status",
    "PageGetPageInfoResponse",
    "PageGetPageInfoResponseStatic",
    "PageGetPageInfoResponseStatus",
    "PageGetPageInfoResponseStatusMonitorListItem",
    "PageGetPageInfoResponse_Static",
    "PageGetPageInfoResponse_Status",
]
