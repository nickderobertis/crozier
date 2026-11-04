



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PageCreatePageResponse,
        PageCreatePageResponseStatic,
        PageCreatePageResponseStatus,
        PageCreatePageResponseStatusMonitorListItem,
        PageCreatePageResponse_Static,
        PageCreatePageResponse_Status,
        PageDeletePageResponse,
        PageDeletePageResponseStatic,
        PageDeletePageResponseStatus,
        PageDeletePageResponseStatusMonitorListItem,
        PageDeletePageResponse_Static,
        PageDeletePageResponse_Status,
        PageEditPageResponse,
        PageEditPageResponseStatic,
        PageEditPageResponseStatus,
        PageEditPageResponseStatusMonitorListItem,
        PageEditPageResponse_Static,
        PageEditPageResponse_Status,
        PageGetAllPagesRequestType,
        PageGetAllPagesResponseItem,
        PageGetAllPagesResponseItemStatic,
        PageGetAllPagesResponseItemStatus,
        PageGetAllPagesResponseItemStatusMonitorListItem,
        PageGetAllPagesResponseItem_Static,
        PageGetAllPagesResponseItem_Status,
        PageGetPageInfoResponse,
        PageGetPageInfoResponseStatic,
        PageGetPageInfoResponseStatus,
        PageGetPageInfoResponseStatusMonitorListItem,
        PageGetPageInfoResponse_Static,
        PageGetPageInfoResponse_Status,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PageCreatePageResponse": ".types",
    "PageCreatePageResponseStatic": ".types",
    "PageCreatePageResponseStatus": ".types",
    "PageCreatePageResponseStatusMonitorListItem": ".types",
    "PageCreatePageResponse_Static": ".types",
    "PageCreatePageResponse_Status": ".types",
    "PageDeletePageResponse": ".types",
    "PageDeletePageResponseStatic": ".types",
    "PageDeletePageResponseStatus": ".types",
    "PageDeletePageResponseStatusMonitorListItem": ".types",
    "PageDeletePageResponse_Static": ".types",
    "PageDeletePageResponse_Status": ".types",
    "PageEditPageResponse": ".types",
    "PageEditPageResponseStatic": ".types",
    "PageEditPageResponseStatus": ".types",
    "PageEditPageResponseStatusMonitorListItem": ".types",
    "PageEditPageResponse_Static": ".types",
    "PageEditPageResponse_Status": ".types",
    "PageGetAllPagesRequestType": ".types",
    "PageGetAllPagesResponseItem": ".types",
    "PageGetAllPagesResponseItemStatic": ".types",
    "PageGetAllPagesResponseItemStatus": ".types",
    "PageGetAllPagesResponseItemStatusMonitorListItem": ".types",
    "PageGetAllPagesResponseItem_Static": ".types",
    "PageGetAllPagesResponseItem_Status": ".types",
    "PageGetPageInfoResponse": ".types",
    "PageGetPageInfoResponseStatic": ".types",
    "PageGetPageInfoResponseStatus": ".types",
    "PageGetPageInfoResponseStatusMonitorListItem": ".types",
    "PageGetPageInfoResponse_Static": ".types",
    "PageGetPageInfoResponse_Status": ".types",
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
