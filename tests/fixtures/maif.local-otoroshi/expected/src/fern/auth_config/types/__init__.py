



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_global_auth_module_request import CreateGlobalAuthModuleRequest
    from .create_global_auth_module_response import CreateGlobalAuthModuleResponse
    from .find_all_global_auth_modules_response_item import FindAllGlobalAuthModulesResponseItem
    from .find_global_auth_module_by_id_response import FindGlobalAuthModuleByIdResponse
    from .patch_global_auth_module_response import PatchGlobalAuthModuleResponse
    from .update_global_auth_module_request_body import UpdateGlobalAuthModuleRequestBody
    from .update_global_auth_module_response import UpdateGlobalAuthModuleResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateGlobalAuthModuleRequest": ".create_global_auth_module_request",
    "CreateGlobalAuthModuleResponse": ".create_global_auth_module_response",
    "FindAllGlobalAuthModulesResponseItem": ".find_all_global_auth_modules_response_item",
    "FindGlobalAuthModuleByIdResponse": ".find_global_auth_module_by_id_response",
    "PatchGlobalAuthModuleResponse": ".patch_global_auth_module_response",
    "UpdateGlobalAuthModuleRequestBody": ".update_global_auth_module_request_body",
    "UpdateGlobalAuthModuleResponse": ".update_global_auth_module_response",
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
    "CreateGlobalAuthModuleRequest",
    "CreateGlobalAuthModuleResponse",
    "FindAllGlobalAuthModulesResponseItem",
    "FindGlobalAuthModuleByIdResponse",
    "PatchGlobalAuthModuleResponse",
    "UpdateGlobalAuthModuleRequestBody",
    "UpdateGlobalAuthModuleResponse",
]
