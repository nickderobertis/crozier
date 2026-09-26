



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .manage_org_data_request_data_type import ManageOrgDataRequestDataType
    from .manage_org_data_request_mode import ManageOrgDataRequestMode
    from .manage_org_data_request_operation import ManageOrgDataRequestOperation
    from .manage_org_data_request_resource import ManageOrgDataRequestResource
_dynamic_imports: typing.Dict[str, str] = {
    "ManageOrgDataRequestDataType": ".manage_org_data_request_data_type",
    "ManageOrgDataRequestMode": ".manage_org_data_request_mode",
    "ManageOrgDataRequestOperation": ".manage_org_data_request_operation",
    "ManageOrgDataRequestResource": ".manage_org_data_request_resource",
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
    "ManageOrgDataRequestDataType",
    "ManageOrgDataRequestMode",
    "ManageOrgDataRequestOperation",
    "ManageOrgDataRequestResource",
]
