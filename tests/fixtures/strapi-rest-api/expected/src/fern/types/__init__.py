



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .document_meta import DocumentMeta
    from .entry import Entry
    from .entry_list_response import EntryListResponse
    from .entry_single_response import EntrySingleResponse
    from .entry_write_request import EntryWriteRequest
    from .error_response import ErrorResponse
    from .error_response_error import ErrorResponseError
    from .get_entry_request_populate import GetEntryRequestPopulate
    from .get_page_metadata_request_populate import GetPageMetadataRequestPopulate
    from .list_entries_request_populate import ListEntriesRequestPopulate
    from .list_meta import ListMeta
    from .list_meta_pagination import ListMetaPagination
    from .list_page_metadata_request_populate import ListPageMetadataRequestPopulate
    from .page_metadata_attributes import PageMetadataAttributes
    from .page_metadata_entry import PageMetadataEntry
    from .page_metadata_list_response import PageMetadataListResponse
    from .page_metadata_single_response import PageMetadataSingleResponse
    from .page_metadata_write_request import PageMetadataWriteRequest
_dynamic_imports: typing.Dict[str, str] = {
    "DocumentMeta": ".document_meta",
    "Entry": ".entry",
    "EntryListResponse": ".entry_list_response",
    "EntrySingleResponse": ".entry_single_response",
    "EntryWriteRequest": ".entry_write_request",
    "ErrorResponse": ".error_response",
    "ErrorResponseError": ".error_response_error",
    "GetEntryRequestPopulate": ".get_entry_request_populate",
    "GetPageMetadataRequestPopulate": ".get_page_metadata_request_populate",
    "ListEntriesRequestPopulate": ".list_entries_request_populate",
    "ListMeta": ".list_meta",
    "ListMetaPagination": ".list_meta_pagination",
    "ListPageMetadataRequestPopulate": ".list_page_metadata_request_populate",
    "PageMetadataAttributes": ".page_metadata_attributes",
    "PageMetadataEntry": ".page_metadata_entry",
    "PageMetadataListResponse": ".page_metadata_list_response",
    "PageMetadataSingleResponse": ".page_metadata_single_response",
    "PageMetadataWriteRequest": ".page_metadata_write_request",
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
    "DocumentMeta",
    "Entry",
    "EntryListResponse",
    "EntrySingleResponse",
    "EntryWriteRequest",
    "ErrorResponse",
    "ErrorResponseError",
    "GetEntryRequestPopulate",
    "GetPageMetadataRequestPopulate",
    "ListEntriesRequestPopulate",
    "ListMeta",
    "ListMetaPagination",
    "ListPageMetadataRequestPopulate",
    "PageMetadataAttributes",
    "PageMetadataEntry",
    "PageMetadataListResponse",
    "PageMetadataSingleResponse",
    "PageMetadataWriteRequest",
]
