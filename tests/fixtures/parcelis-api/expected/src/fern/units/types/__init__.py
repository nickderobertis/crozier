



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .units_by_id_response import UnitsByIdResponse
    from .units_create_request_unit_type import UnitsCreateRequestUnitType
    from .units_create_response import UnitsCreateResponse
    from .units_delete_response import UnitsDeleteResponse
    from .units_list_response import UnitsListResponse
    from .units_update_request_unit_type import UnitsUpdateRequestUnitType
    from .units_update_response import UnitsUpdateResponse
_dynamic_imports: typing.Dict[str, str] = {
    "UnitsByIdResponse": ".units_by_id_response",
    "UnitsCreateRequestUnitType": ".units_create_request_unit_type",
    "UnitsCreateResponse": ".units_create_response",
    "UnitsDeleteResponse": ".units_delete_response",
    "UnitsListResponse": ".units_list_response",
    "UnitsUpdateRequestUnitType": ".units_update_request_unit_type",
    "UnitsUpdateResponse": ".units_update_response",
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
    "UnitsByIdResponse",
    "UnitsCreateRequestUnitType",
    "UnitsCreateResponse",
    "UnitsDeleteResponse",
    "UnitsListResponse",
    "UnitsUpdateRequestUnitType",
    "UnitsUpdateResponse",
]
