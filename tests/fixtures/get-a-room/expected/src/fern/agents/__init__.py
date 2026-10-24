



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        UseAgentInvitationRequest,
        UseAgentInvitationRequest_Check,
        UseAgentInvitationRequest_Close,
        UseAgentInvitationRequest_Collect,
        UseAgentInvitationRequest_Final,
        UseAgentInvitationRequest_Finish,
        UseAgentInvitationRequest_Join,
        UseAgentInvitationRequest_Say,
        UseAgentInvitationResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "UseAgentInvitationRequest": ".types",
    "UseAgentInvitationRequest_Check": ".types",
    "UseAgentInvitationRequest_Close": ".types",
    "UseAgentInvitationRequest_Collect": ".types",
    "UseAgentInvitationRequest_Final": ".types",
    "UseAgentInvitationRequest_Finish": ".types",
    "UseAgentInvitationRequest_Join": ".types",
    "UseAgentInvitationRequest_Say": ".types",
    "UseAgentInvitationResponse": ".types",
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
    "UseAgentInvitationRequest",
    "UseAgentInvitationRequest_Check",
    "UseAgentInvitationRequest_Close",
    "UseAgentInvitationRequest_Collect",
    "UseAgentInvitationRequest_Final",
    "UseAgentInvitationRequest_Finish",
    "UseAgentInvitationRequest_Join",
    "UseAgentInvitationRequest_Say",
    "UseAgentInvitationResponse",
]
