



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_leads_id_v3request_fields_item import GetLeadsIdV3RequestFieldsItem
    from .get_leads_id_v3response import GetLeadsIdV3Response
    from .get_leads_v3request_fields_item import GetLeadsV3RequestFieldsItem
    from .get_leads_v3request_status import GetLeadsV3RequestStatus
    from .get_leads_v3request_view import GetLeadsV3RequestView
    from .get_leads_v3response import GetLeadsV3Response
_dynamic_imports: typing.Dict[str, str] = {
    "GetLeadsIdV3RequestFieldsItem": ".get_leads_id_v3request_fields_item",
    "GetLeadsIdV3Response": ".get_leads_id_v3response",
    "GetLeadsV3RequestFieldsItem": ".get_leads_v3request_fields_item",
    "GetLeadsV3RequestStatus": ".get_leads_v3request_status",
    "GetLeadsV3RequestView": ".get_leads_v3request_view",
    "GetLeadsV3Response": ".get_leads_v3response",
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
    "GetLeadsIdV3RequestFieldsItem",
    "GetLeadsIdV3Response",
    "GetLeadsV3RequestFieldsItem",
    "GetLeadsV3RequestStatus",
    "GetLeadsV3RequestView",
    "GetLeadsV3Response",
]
