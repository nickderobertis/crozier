



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_file_authors_request_status import GetFileAuthorsRequestStatus
    from .get_file_copyrights_request_status import GetFileCopyrightsRequestStatus
    from .get_file_eccs_request_status import GetFileEccsRequestStatus
    from .get_file_emails_request_status import GetFileEmailsRequestStatus
    from .get_file_ipras_request_status import GetFileIprasRequestStatus
    from .get_file_keywords_request_status import GetFileKeywordsRequestStatus
    from .get_file_scan_code_author_request_status import GetFileScanCodeAuthorRequestStatus
    from .get_file_scan_code_copyrights_request_status import GetFileScanCodeCopyrightsRequestStatus
    from .get_file_scan_code_email_request_status import GetFileScanCodeEmailRequestStatus
    from .get_file_scan_code_url_request_status import GetFileScanCodeUrlRequestStatus
    from .get_file_urls_request_status import GetFileUrlsRequestStatus
    from .get_file_user_copyrights_request_status import GetFileUserCopyrightsRequestStatus
    from .get_total_file_copyrights_request_status import GetTotalFileCopyrightsRequestStatus
    from .get_total_file_copyrights_response_item import GetTotalFileCopyrightsResponseItem
    from .get_total_file_user_copyrights_request_status import GetTotalFileUserCopyrightsRequestStatus
    from .get_total_file_user_copyrights_response_item import GetTotalFileUserCopyrightsResponseItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetFileAuthorsRequestStatus": ".get_file_authors_request_status",
    "GetFileCopyrightsRequestStatus": ".get_file_copyrights_request_status",
    "GetFileEccsRequestStatus": ".get_file_eccs_request_status",
    "GetFileEmailsRequestStatus": ".get_file_emails_request_status",
    "GetFileIprasRequestStatus": ".get_file_ipras_request_status",
    "GetFileKeywordsRequestStatus": ".get_file_keywords_request_status",
    "GetFileScanCodeAuthorRequestStatus": ".get_file_scan_code_author_request_status",
    "GetFileScanCodeCopyrightsRequestStatus": ".get_file_scan_code_copyrights_request_status",
    "GetFileScanCodeEmailRequestStatus": ".get_file_scan_code_email_request_status",
    "GetFileScanCodeUrlRequestStatus": ".get_file_scan_code_url_request_status",
    "GetFileUrlsRequestStatus": ".get_file_urls_request_status",
    "GetFileUserCopyrightsRequestStatus": ".get_file_user_copyrights_request_status",
    "GetTotalFileCopyrightsRequestStatus": ".get_total_file_copyrights_request_status",
    "GetTotalFileCopyrightsResponseItem": ".get_total_file_copyrights_response_item",
    "GetTotalFileUserCopyrightsRequestStatus": ".get_total_file_user_copyrights_request_status",
    "GetTotalFileUserCopyrightsResponseItem": ".get_total_file_user_copyrights_response_item",
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
