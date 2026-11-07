



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetFileAuthorsRequestStatus,
        GetFileCopyrightsRequestStatus,
        GetFileEccsRequestStatus,
        GetFileEmailsRequestStatus,
        GetFileIprasRequestStatus,
        GetFileKeywordsRequestStatus,
        GetFileScanCodeAuthorRequestStatus,
        GetFileScanCodeCopyrightsRequestStatus,
        GetFileScanCodeEmailRequestStatus,
        GetFileScanCodeUrlRequestStatus,
        GetFileUrlsRequestStatus,
        GetFileUserCopyrightsRequestStatus,
        GetTotalFileCopyrightsRequestStatus,
        GetTotalFileCopyrightsResponseItem,
        GetTotalFileUserCopyrightsRequestStatus,
        GetTotalFileUserCopyrightsResponseItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetFileAuthorsRequestStatus": ".types",
    "GetFileCopyrightsRequestStatus": ".types",
    "GetFileEccsRequestStatus": ".types",
    "GetFileEmailsRequestStatus": ".types",
    "GetFileIprasRequestStatus": ".types",
    "GetFileKeywordsRequestStatus": ".types",
    "GetFileScanCodeAuthorRequestStatus": ".types",
    "GetFileScanCodeCopyrightsRequestStatus": ".types",
    "GetFileScanCodeEmailRequestStatus": ".types",
    "GetFileScanCodeUrlRequestStatus": ".types",
    "GetFileUrlsRequestStatus": ".types",
    "GetFileUserCopyrightsRequestStatus": ".types",
    "GetTotalFileCopyrightsRequestStatus": ".types",
    "GetTotalFileCopyrightsResponseItem": ".types",
    "GetTotalFileUserCopyrightsRequestStatus": ".types",
    "GetTotalFileUserCopyrightsResponseItem": ".types",
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
    "GetFileAuthorsRequestStatus",
    "GetFileCopyrightsRequestStatus",
    "GetFileEccsRequestStatus",
    "GetFileEmailsRequestStatus",
    "GetFileIprasRequestStatus",
    "GetFileKeywordsRequestStatus",
    "GetFileScanCodeAuthorRequestStatus",
    "GetFileScanCodeCopyrightsRequestStatus",
    "GetFileScanCodeEmailRequestStatus",
    "GetFileScanCodeUrlRequestStatus",
    "GetFileUrlsRequestStatus",
    "GetFileUserCopyrightsRequestStatus",
    "GetTotalFileCopyrightsRequestStatus",
    "GetTotalFileCopyrightsResponseItem",
    "GetTotalFileUserCopyrightsRequestStatus",
    "GetTotalFileUserCopyrightsResponseItem",
]
