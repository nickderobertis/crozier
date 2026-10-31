



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .axis_section_treeless import AxisSectionTreeless
    from .axis_treeless import AxisTreeless
    from .bad_request_error_body import BadRequestErrorBody
    from .department_tree_node import DepartmentTreeNode
    from .department_tree_node_node import DepartmentTreeNodeNode
    from .internal_server_error_body import InternalServerErrorBody
    from .not_found_error_body import NotFoundErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .user import User
_dynamic_imports: typing.Dict[str, str] = {
    "AxisSectionTreeless": ".axis_section_treeless",
    "AxisTreeless": ".axis_treeless",
    "BadRequestErrorBody": ".bad_request_error_body",
    "DepartmentTreeNode": ".department_tree_node",
    "DepartmentTreeNodeNode": ".department_tree_node_node",
    "InternalServerErrorBody": ".internal_server_error_body",
    "NotFoundErrorBody": ".not_found_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "User": ".user",
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
    "AxisSectionTreeless",
    "AxisTreeless",
    "BadRequestErrorBody",
    "DepartmentTreeNode",
    "DepartmentTreeNodeNode",
    "InternalServerErrorBody",
    "NotFoundErrorBody",
    "UnauthorizedErrorBody",
    "User",
]
