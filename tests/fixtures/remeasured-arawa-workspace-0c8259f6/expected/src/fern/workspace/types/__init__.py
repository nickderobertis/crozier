



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workspace_api_ocs_create_response import WorkspaceApiOcsCreateResponse
    from .workspace_api_ocs_create_response_ocs import WorkspaceApiOcsCreateResponseOcs
    from .workspace_api_ocs_edit_response import WorkspaceApiOcsEditResponse
    from .workspace_api_ocs_edit_response_ocs import WorkspaceApiOcsEditResponseOcs
    from .workspace_api_ocs_find_all_response import WorkspaceApiOcsFindAllResponse
    from .workspace_api_ocs_find_all_response_ocs import WorkspaceApiOcsFindAllResponseOcs
    from .workspace_api_ocs_find_response import WorkspaceApiOcsFindResponse
    from .workspace_api_ocs_find_response_ocs import WorkspaceApiOcsFindResponseOcs
_dynamic_imports: typing.Dict[str, str] = {
    "WorkspaceApiOcsCreateResponse": ".workspace_api_ocs_create_response",
    "WorkspaceApiOcsCreateResponseOcs": ".workspace_api_ocs_create_response_ocs",
    "WorkspaceApiOcsEditResponse": ".workspace_api_ocs_edit_response",
    "WorkspaceApiOcsEditResponseOcs": ".workspace_api_ocs_edit_response_ocs",
    "WorkspaceApiOcsFindAllResponse": ".workspace_api_ocs_find_all_response",
    "WorkspaceApiOcsFindAllResponseOcs": ".workspace_api_ocs_find_all_response_ocs",
    "WorkspaceApiOcsFindResponse": ".workspace_api_ocs_find_response",
    "WorkspaceApiOcsFindResponseOcs": ".workspace_api_ocs_find_response_ocs",
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
    "WorkspaceApiOcsCreateResponse",
    "WorkspaceApiOcsCreateResponseOcs",
    "WorkspaceApiOcsEditResponse",
    "WorkspaceApiOcsEditResponseOcs",
    "WorkspaceApiOcsFindAllResponse",
    "WorkspaceApiOcsFindAllResponseOcs",
    "WorkspaceApiOcsFindResponse",
    "WorkspaceApiOcsFindResponseOcs",
]
