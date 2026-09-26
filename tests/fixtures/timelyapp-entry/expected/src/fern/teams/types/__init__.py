



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete11account_id_teams_id_response import Delete11AccountIdTeamsIdResponse
    from .v1teams_create_team import V1TeamsCreateTeam
    from .v1teams_patch_team import V1TeamsPatchTeam
    from .v1teams_update_team import V1TeamsUpdateTeam
_dynamic_imports: typing.Dict[str, str] = {
    "Delete11AccountIdTeamsIdResponse": ".delete11account_id_teams_id_response",
    "V1TeamsCreateTeam": ".v1teams_create_team",
    "V1TeamsPatchTeam": ".v1teams_patch_team",
    "V1TeamsUpdateTeam": ".v1teams_update_team",
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


__all__ = ["Delete11AccountIdTeamsIdResponse", "V1TeamsCreateTeam", "V1TeamsPatchTeam", "V1TeamsUpdateTeam"]
