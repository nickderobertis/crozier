



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workspace_api_ocs_create_sub_group_response import WorkspaceApiOcsCreateSubGroupResponse
    from .workspace_api_ocs_create_sub_group_response_ocs import WorkspaceApiOcsCreateSubGroupResponseOcs
    from .workspace_api_ocs_find_groups_by_space_id_response import WorkspaceApiOcsFindGroupsBySpaceIdResponse
    from .workspace_api_ocs_find_groups_by_space_id_response_ocs import WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs
_dynamic_imports: typing.Dict[str, str] = {
    "WorkspaceApiOcsCreateSubGroupResponse": ".workspace_api_ocs_create_sub_group_response",
    "WorkspaceApiOcsCreateSubGroupResponseOcs": ".workspace_api_ocs_create_sub_group_response_ocs",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponse": ".workspace_api_ocs_find_groups_by_space_id_response",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs": ".workspace_api_ocs_find_groups_by_space_id_response_ocs",
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
    "WorkspaceApiOcsCreateSubGroupResponse",
    "WorkspaceApiOcsCreateSubGroupResponseOcs",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponse",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs",
]
