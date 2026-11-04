



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_ocs import BadRequestErrorBodyOcs
    from .capabilities import Capabilities
    from .capabilities_workspace import CapabilitiesWorkspace
    from .confirmation_message import ConfirmationMessage
    from .conflict_error_body import ConflictErrorBody
    from .conflict_error_body_ocs import ConflictErrorBodyOcs
    from .find_groups import FindGroups
    from .forbidden_error_body import ForbiddenErrorBody
    from .forbidden_error_body_ocs import ForbiddenErrorBodyOcs
    from .group_info import GroupInfo
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_ocs import NotFoundErrorBodyOcs
    from .ocs_meta import OcsMeta
    from .space import Space
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_ocs import UnauthorizedErrorBodyOcs
    from .user_definition import UserDefinition
    from .users_list import UsersList
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyOcs": ".bad_request_error_body_ocs",
    "Capabilities": ".capabilities",
    "CapabilitiesWorkspace": ".capabilities_workspace",
    "ConfirmationMessage": ".confirmation_message",
    "ConflictErrorBody": ".conflict_error_body",
    "ConflictErrorBodyOcs": ".conflict_error_body_ocs",
    "FindGroups": ".find_groups",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBodyOcs": ".forbidden_error_body_ocs",
    "GroupInfo": ".group_info",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyOcs": ".not_found_error_body_ocs",
    "OcsMeta": ".ocs_meta",
    "Space": ".space",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyOcs": ".unauthorized_error_body_ocs",
    "UserDefinition": ".user_definition",
    "UsersList": ".users_list",
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
    "BadRequestErrorBody",
    "BadRequestErrorBodyOcs",
    "Capabilities",
    "CapabilitiesWorkspace",
    "ConfirmationMessage",
    "ConflictErrorBody",
    "ConflictErrorBodyOcs",
    "FindGroups",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyOcs",
    "GroupInfo",
    "NotFoundErrorBody",
    "NotFoundErrorBodyOcs",
    "OcsMeta",
    "Space",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyOcs",
    "UserDefinition",
    "UsersList",
]
