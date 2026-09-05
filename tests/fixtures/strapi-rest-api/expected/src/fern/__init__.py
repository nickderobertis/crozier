



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DocumentMeta,
        Entry,
        EntryListResponse,
        EntrySingleResponse,
        EntryWriteRequest,
        ErrorResponse,
        ErrorResponseError,
        GetEntryRequestPopulate,
        GetPageMetadataRequestPopulate,
        ListEntriesRequestPopulate,
        ListMeta,
        ListMetaPagination,
        ListPageMetadataRequestPopulate,
        PageMetadataAttributes,
        PageMetadataEntry,
        PageMetadataListResponse,
        PageMetadataSingleResponse,
        PageMetadataWriteRequest,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import collection_type, page_metadata, single_type
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .collection_type import GetEntryRequestStatus, ListEntriesRequestStatus
    from .environment import FernApiEnvironment
    from .page_metadata import GetPageMetadataRequestStatus, ListPageMetadataRequestStatus
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DocumentMeta": ".types",
    "Entry": ".types",
    "EntryListResponse": ".types",
    "EntrySingleResponse": ".types",
    "EntryWriteRequest": ".types",
    "ErrorResponse": ".types",
    "ErrorResponseError": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetEntryRequestPopulate": ".types",
    "GetEntryRequestStatus": ".collection_type",
    "GetPageMetadataRequestPopulate": ".types",
    "GetPageMetadataRequestStatus": ".page_metadata",
    "ListEntriesRequestPopulate": ".types",
    "ListEntriesRequestStatus": ".collection_type",
    "ListMeta": ".types",
    "ListMetaPagination": ".types",
    "ListPageMetadataRequestPopulate": ".types",
    "ListPageMetadataRequestStatus": ".page_metadata",
    "NotFoundError": ".errors",
    "PageMetadataAttributes": ".types",
    "PageMetadataEntry": ".types",
    "PageMetadataListResponse": ".types",
    "PageMetadataSingleResponse": ".types",
    "PageMetadataWriteRequest": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "collection_type": ".collection_type",
    "page_metadata": ".page_metadata",
    "single_type": ".single_type",
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
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DocumentMeta",
    "Entry",
    "EntryListResponse",
    "EntrySingleResponse",
    "EntryWriteRequest",
    "ErrorResponse",
    "ErrorResponseError",
    "FernApi",
    "FernApiEnvironment",
    "GetEntryRequestPopulate",
    "GetEntryRequestStatus",
    "GetPageMetadataRequestPopulate",
    "GetPageMetadataRequestStatus",
    "ListEntriesRequestPopulate",
    "ListEntriesRequestStatus",
    "ListMeta",
    "ListMetaPagination",
    "ListPageMetadataRequestPopulate",
    "ListPageMetadataRequestStatus",
    "NotFoundError",
    "PageMetadataAttributes",
    "PageMetadataEntry",
    "PageMetadataListResponse",
    "PageMetadataSingleResponse",
    "PageMetadataWriteRequest",
    "UnauthorizedError",
    "__version__",
    "collection_type",
    "page_metadata",
    "single_type",
]
