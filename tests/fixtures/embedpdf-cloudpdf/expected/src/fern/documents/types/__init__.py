



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .documents_import_from_request_dedup_mode import DocumentsImportFromRequestDedupMode
    from .documents_import_from_request_expected import DocumentsImportFromRequestExpected
    from .documents_import_from_request_mode import DocumentsImportFromRequestMode
    from .documents_import_from_request_source import (
        DocumentsImportFromRequestSource,
        DocumentsImportFromRequestSource_Connection,
        DocumentsImportFromRequestSource_Url,
    )
    from .documents_import_from_request_source_connection import DocumentsImportFromRequestSourceConnection
    from .documents_import_from_request_source_url import DocumentsImportFromRequestSourceUrl
    from .documents_init_request_dedup_mode import DocumentsInitRequestDedupMode
    from .documents_init_request_upload_preference import DocumentsInitRequestUploadPreference
    from .list_documents_request_state import ListDocumentsRequestState
_dynamic_imports: typing.Dict[str, str] = {
    "DocumentsImportFromRequestDedupMode": ".documents_import_from_request_dedup_mode",
    "DocumentsImportFromRequestExpected": ".documents_import_from_request_expected",
    "DocumentsImportFromRequestMode": ".documents_import_from_request_mode",
    "DocumentsImportFromRequestSource": ".documents_import_from_request_source",
    "DocumentsImportFromRequestSourceConnection": ".documents_import_from_request_source_connection",
    "DocumentsImportFromRequestSourceUrl": ".documents_import_from_request_source_url",
    "DocumentsImportFromRequestSource_Connection": ".documents_import_from_request_source",
    "DocumentsImportFromRequestSource_Url": ".documents_import_from_request_source",
    "DocumentsInitRequestDedupMode": ".documents_init_request_dedup_mode",
    "DocumentsInitRequestUploadPreference": ".documents_init_request_upload_preference",
    "ListDocumentsRequestState": ".list_documents_request_state",
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
    "DocumentsImportFromRequestDedupMode",
    "DocumentsImportFromRequestExpected",
    "DocumentsImportFromRequestMode",
    "DocumentsImportFromRequestSource",
    "DocumentsImportFromRequestSourceConnection",
    "DocumentsImportFromRequestSourceUrl",
    "DocumentsImportFromRequestSource_Connection",
    "DocumentsImportFromRequestSource_Url",
    "DocumentsInitRequestDedupMode",
    "DocumentsInitRequestUploadPreference",
    "ListDocumentsRequestState",
]
