



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin_chunks_request_mode import AdminChunksRequestMode
    from .admin_chunks_response import AdminChunksResponse
    from .admin_chunks_response_data_item import AdminChunksResponseDataItem
    from .admin_config_request_mode import AdminConfigRequestMode
    from .admin_config_response import AdminConfigResponse
    from .admin_init_response import AdminInitResponse
    from .admin_init_response_data_item import AdminInitResponseDataItem
    from .admin_status_request_modes_item import AdminStatusRequestModesItem
    from .admin_status_response import AdminStatusResponse
    from .admin_status_response_data_item import AdminStatusResponseDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "AdminChunksRequestMode": ".admin_chunks_request_mode",
    "AdminChunksResponse": ".admin_chunks_response",
    "AdminChunksResponseDataItem": ".admin_chunks_response_data_item",
    "AdminConfigRequestMode": ".admin_config_request_mode",
    "AdminConfigResponse": ".admin_config_response",
    "AdminInitResponse": ".admin_init_response",
    "AdminInitResponseDataItem": ".admin_init_response_data_item",
    "AdminStatusRequestModesItem": ".admin_status_request_modes_item",
    "AdminStatusResponse": ".admin_status_response",
    "AdminStatusResponseDataItem": ".admin_status_response_data_item",
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
    "AdminChunksRequestMode",
    "AdminChunksResponse",
    "AdminChunksResponseDataItem",
    "AdminConfigRequestMode",
    "AdminConfigResponse",
    "AdminInitResponse",
    "AdminInitResponseDataItem",
    "AdminStatusRequestModesItem",
    "AdminStatusResponse",
    "AdminStatusResponseDataItem",
]
