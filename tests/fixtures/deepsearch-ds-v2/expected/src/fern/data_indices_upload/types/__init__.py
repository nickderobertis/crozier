



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .convert_documents_request_body_conversion_settings import ConvertDocumentsRequestBodyConversionSettings
    from .convert_documents_request_body_without_operations_item import ConvertDocumentsRequestBodyWithoutOperationsItem
    from .convert_upload_documents_request_body_conversion_settings import (
        ConvertUploadDocumentsRequestBodyConversionSettings,
    )
    from .data_index_upload_file_source_conversion_settings import DataIndexUploadFileSourceConversionSettings
    from .data_index_upload_file_source_urls import DataIndexUploadFileSourceUrls
    from .upload_elastic_request_body_with_operations_item import UploadElasticRequestBodyWithOperationsItem
_dynamic_imports: typing.Dict[str, str] = {
    "ConvertDocumentsRequestBodyConversionSettings": ".convert_documents_request_body_conversion_settings",
    "ConvertDocumentsRequestBodyWithoutOperationsItem": ".convert_documents_request_body_without_operations_item",
    "ConvertUploadDocumentsRequestBodyConversionSettings": ".convert_upload_documents_request_body_conversion_settings",
    "DataIndexUploadFileSourceConversionSettings": ".data_index_upload_file_source_conversion_settings",
    "DataIndexUploadFileSourceUrls": ".data_index_upload_file_source_urls",
    "UploadElasticRequestBodyWithOperationsItem": ".upload_elastic_request_body_with_operations_item",
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
    "ConvertDocumentsRequestBodyConversionSettings",
    "ConvertDocumentsRequestBodyWithoutOperationsItem",
    "ConvertUploadDocumentsRequestBodyConversionSettings",
    "DataIndexUploadFileSourceConversionSettings",
    "DataIndexUploadFileSourceUrls",
    "UploadElasticRequestBodyWithOperationsItem",
]
