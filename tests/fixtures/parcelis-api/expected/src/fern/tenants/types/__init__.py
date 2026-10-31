



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .tenants_complete_image_upload_response import TenantsCompleteImageUploadResponse
    from .tenants_create_image_upload_url_request_content_type import TenantsCreateImageUploadUrlRequestContentType
    from .tenants_create_image_upload_url_response import TenantsCreateImageUploadUrlResponse
    from .tenants_delete_image_response import TenantsDeleteImageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "TenantsCompleteImageUploadResponse": ".tenants_complete_image_upload_response",
    "TenantsCreateImageUploadUrlRequestContentType": ".tenants_create_image_upload_url_request_content_type",
    "TenantsCreateImageUploadUrlResponse": ".tenants_create_image_upload_url_response",
    "TenantsDeleteImageResponse": ".tenants_delete_image_response",
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
    "TenantsCompleteImageUploadResponse",
    "TenantsCreateImageUploadUrlRequestContentType",
    "TenantsCreateImageUploadUrlResponse",
    "TenantsDeleteImageResponse",
]
