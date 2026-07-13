



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .fireteam_get_active_private_clan_fireteam_count_response import (
        FireteamGetActivePrivateClanFireteamCountResponse,
    )
    from .fireteam_get_available_clan_fireteams_response import FireteamGetAvailableClanFireteamsResponse
    from .fireteam_get_clan_fireteam_response import FireteamGetClanFireteamResponse
    from .fireteam_get_my_clan_fireteams_response import FireteamGetMyClanFireteamsResponse
    from .fireteam_search_public_available_clan_fireteams_response import (
        FireteamSearchPublicAvailableClanFireteamsResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "FireteamGetActivePrivateClanFireteamCountResponse": ".fireteam_get_active_private_clan_fireteam_count_response",
    "FireteamGetAvailableClanFireteamsResponse": ".fireteam_get_available_clan_fireteams_response",
    "FireteamGetClanFireteamResponse": ".fireteam_get_clan_fireteam_response",
    "FireteamGetMyClanFireteamsResponse": ".fireteam_get_my_clan_fireteams_response",
    "FireteamSearchPublicAvailableClanFireteamsResponse": ".fireteam_search_public_available_clan_fireteams_response",
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
    "FireteamGetActivePrivateClanFireteamCountResponse",
    "FireteamGetAvailableClanFireteamsResponse",
    "FireteamGetClanFireteamResponse",
    "FireteamGetMyClanFireteamsResponse",
    "FireteamSearchPublicAvailableClanFireteamsResponse",
]
