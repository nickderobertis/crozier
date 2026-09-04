



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_name import AccountName
    from .count import Count
    from .kind import Kind
    from .limit import Limit
    from .offset import Offset
    from .resource_id import ResourceId
    from .resource_version import ResourceVersion
    from .role_type import RoleType
_dynamic_imports: typing.Dict[str, str] = {
    "AccountName": ".account_name",
    "Count": ".count",
    "Kind": ".kind",
    "Limit": ".limit",
    "Offset": ".offset",
    "ResourceId": ".resource_id",
    "ResourceVersion": ".resource_version",
    "RoleType": ".role_type",
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


__all__ = ["AccountName", "Count", "Kind", "Limit", "Offset", "ResourceId", "ResourceVersion", "RoleType"]
