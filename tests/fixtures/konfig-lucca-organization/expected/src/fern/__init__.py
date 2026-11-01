



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AxisSectionTreeless,
        AxisTreeless,
        BadRequestErrorBody,
        DepartmentTreeNode,
        DepartmentTreeNodeNode,
        InternalServerErrorBody,
        NotFoundErrorBody,
        UnauthorizedErrorBody,
        User,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError
    from . import axis_sections, departments
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .axis_sections import (
        Axis,
        AxisSection,
        GetApiV3AxesResponse,
        GetApiV3AxesResponseData,
        GetApiV3AxisSectionsAxisSectionIdResponse,
        GetApiV3AxissectionsResponse,
        GetApiV3AxissectionsResponseData,
        PostApiV3AxisSectionsResponse,
        PutApiV3AxisSectionsAxisSectionIdResponse,
    )
    from .client import AsyncFernApi, FernApi
    from .departments import (
        Department,
        GetApiV3DepartmentsDepartmentIdResponse,
        GetApiV3DepartmentsResponse,
        GetApiV3DepartmentsResponseData,
        GetApiV3DepartmentsTreeResponse,
        GetApiV3DepartmentsTreeResponseData,
    )
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Axis": ".axis_sections",
    "AxisSection": ".axis_sections",
    "AxisSectionTreeless": ".types",
    "AxisTreeless": ".types",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Department": ".departments",
    "DepartmentTreeNode": ".types",
    "DepartmentTreeNodeNode": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetApiV3AxesResponse": ".axis_sections",
    "GetApiV3AxesResponseData": ".axis_sections",
    "GetApiV3AxisSectionsAxisSectionIdResponse": ".axis_sections",
    "GetApiV3AxissectionsResponse": ".axis_sections",
    "GetApiV3AxissectionsResponseData": ".axis_sections",
    "GetApiV3DepartmentsDepartmentIdResponse": ".departments",
    "GetApiV3DepartmentsResponse": ".departments",
    "GetApiV3DepartmentsResponseData": ".departments",
    "GetApiV3DepartmentsTreeResponse": ".departments",
    "GetApiV3DepartmentsTreeResponseData": ".departments",
    "InternalServerError": ".errors",
    "InternalServerErrorBody": ".types",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "PostApiV3AxisSectionsResponse": ".axis_sections",
    "PutApiV3AxisSectionsAxisSectionIdResponse": ".axis_sections",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "User": ".types",
    "__version__": ".version",
    "axis_sections": ".axis_sections",
    "departments": ".departments",
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
    "AsyncFernApi",
    "Axis",
    "AxisSection",
    "AxisSectionTreeless",
    "AxisTreeless",
    "BadRequestError",
    "BadRequestErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Department",
    "DepartmentTreeNode",
    "DepartmentTreeNodeNode",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetApiV3AxesResponse",
    "GetApiV3AxesResponseData",
    "GetApiV3AxisSectionsAxisSectionIdResponse",
    "GetApiV3AxissectionsResponse",
    "GetApiV3AxissectionsResponseData",
    "GetApiV3DepartmentsDepartmentIdResponse",
    "GetApiV3DepartmentsResponse",
    "GetApiV3DepartmentsResponseData",
    "GetApiV3DepartmentsTreeResponse",
    "GetApiV3DepartmentsTreeResponseData",
    "InternalServerError",
    "InternalServerErrorBody",
    "NotFoundError",
    "NotFoundErrorBody",
    "PostApiV3AxisSectionsResponse",
    "PutApiV3AxisSectionsAxisSectionIdResponse",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "User",
    "__version__",
    "axis_sections",
    "departments",
]
