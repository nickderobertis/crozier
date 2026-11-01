



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .department import Department
    from .get_api_v3departments_department_id_response import GetApiV3DepartmentsDepartmentIdResponse
    from .get_api_v3departments_response import GetApiV3DepartmentsResponse
    from .get_api_v3departments_response_data import GetApiV3DepartmentsResponseData
    from .get_api_v3departments_tree_response import GetApiV3DepartmentsTreeResponse
    from .get_api_v3departments_tree_response_data import GetApiV3DepartmentsTreeResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "Department": ".department",
    "GetApiV3DepartmentsDepartmentIdResponse": ".get_api_v3departments_department_id_response",
    "GetApiV3DepartmentsResponse": ".get_api_v3departments_response",
    "GetApiV3DepartmentsResponseData": ".get_api_v3departments_response_data",
    "GetApiV3DepartmentsTreeResponse": ".get_api_v3departments_tree_response",
    "GetApiV3DepartmentsTreeResponseData": ".get_api_v3departments_tree_response_data",
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
    "Department",
    "GetApiV3DepartmentsDepartmentIdResponse",
    "GetApiV3DepartmentsResponse",
    "GetApiV3DepartmentsResponseData",
    "GetApiV3DepartmentsTreeResponse",
    "GetApiV3DepartmentsTreeResponseData",
]
