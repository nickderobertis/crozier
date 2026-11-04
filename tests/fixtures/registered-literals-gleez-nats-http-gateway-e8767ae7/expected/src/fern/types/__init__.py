



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .bucket import Bucket
    from .bucket_config import BucketConfig
    from .bucket_config_storage import BucketConfigStorage
    from .error import Error
    from .header import Header
    from .metadata import Metadata
    from .msg import Msg
    from .object_info import ObjectInfo
    from .object_info_link import ObjectInfoLink
    from .object_link import ObjectLink
    from .unknown import Unknown
    from .value import Value
    from .value_event import ValueEvent
    from .value_event_operation import ValueEventOperation
    from .value_operation import ValueOperation
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "Bucket": ".bucket",
    "BucketConfig": ".bucket_config",
    "BucketConfigStorage": ".bucket_config_storage",
    "Error": ".error",
    "Header": ".header",
    "Metadata": ".metadata",
    "Msg": ".msg",
    "ObjectInfo": ".object_info",
    "ObjectInfoLink": ".object_info_link",
    "ObjectLink": ".object_link",
    "Unknown": ".unknown",
    "Value": ".value",
    "ValueEvent": ".value_event",
    "ValueEventOperation": ".value_event_operation",
    "ValueOperation": ".value_operation",
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
    "BadRequestErrorBody",
    "Bucket",
    "BucketConfig",
    "BucketConfigStorage",
    "Error",
    "Header",
    "Metadata",
    "Msg",
    "ObjectInfo",
    "ObjectInfoLink",
    "ObjectLink",
    "Unknown",
    "Value",
    "ValueEvent",
    "ValueEventOperation",
    "ValueOperation",
]
