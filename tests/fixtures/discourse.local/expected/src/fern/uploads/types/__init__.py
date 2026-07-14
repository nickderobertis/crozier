



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abort_multipart_response import AbortMultipartResponse
    from .batch_presign_multipart_parts_response import BatchPresignMultipartPartsResponse
    from .complete_external_upload_response import CompleteExternalUploadResponse
    from .complete_multipart_response import CompleteMultipartResponse
    from .create_multipart_upload_request_metadata import CreateMultipartUploadRequestMetadata
    from .create_multipart_upload_request_upload_type import CreateMultipartUploadRequestUploadType
    from .create_multipart_upload_response import CreateMultipartUploadResponse
    from .create_upload_request_type import CreateUploadRequestType
    from .create_upload_response import CreateUploadResponse
    from .generate_presigned_put_request_metadata import GeneratePresignedPutRequestMetadata
    from .generate_presigned_put_request_type import GeneratePresignedPutRequestType
    from .generate_presigned_put_response import GeneratePresignedPutResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AbortMultipartResponse": ".abort_multipart_response",
    "BatchPresignMultipartPartsResponse": ".batch_presign_multipart_parts_response",
    "CompleteExternalUploadResponse": ".complete_external_upload_response",
    "CompleteMultipartResponse": ".complete_multipart_response",
    "CreateMultipartUploadRequestMetadata": ".create_multipart_upload_request_metadata",
    "CreateMultipartUploadRequestUploadType": ".create_multipart_upload_request_upload_type",
    "CreateMultipartUploadResponse": ".create_multipart_upload_response",
    "CreateUploadRequestType": ".create_upload_request_type",
    "CreateUploadResponse": ".create_upload_response",
    "GeneratePresignedPutRequestMetadata": ".generate_presigned_put_request_metadata",
    "GeneratePresignedPutRequestType": ".generate_presigned_put_request_type",
    "GeneratePresignedPutResponse": ".generate_presigned_put_response",
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
    "AbortMultipartResponse",
    "BatchPresignMultipartPartsResponse",
    "CompleteExternalUploadResponse",
    "CompleteMultipartResponse",
    "CreateMultipartUploadRequestMetadata",
    "CreateMultipartUploadRequestUploadType",
    "CreateMultipartUploadResponse",
    "CreateUploadRequestType",
    "CreateUploadResponse",
    "GeneratePresignedPutRequestMetadata",
    "GeneratePresignedPutRequestType",
    "GeneratePresignedPutResponse",
]
