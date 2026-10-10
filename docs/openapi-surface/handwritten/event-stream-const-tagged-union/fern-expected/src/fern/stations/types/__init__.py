



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .follow_levels_response import FollowLevelsResponse, FollowLevelsResponse_Ebb, FollowLevelsResponse_Flood
    from .follow_levels_response_ebb import FollowLevelsResponseEbb
    from .follow_levels_response_flood import FollowLevelsResponseFlood
_dynamic_imports: typing.Dict[str, str] = {
    "FollowLevelsResponse": ".follow_levels_response",
    "FollowLevelsResponseEbb": ".follow_levels_response_ebb",
    "FollowLevelsResponseFlood": ".follow_levels_response_flood",
    "FollowLevelsResponse_Ebb": ".follow_levels_response",
    "FollowLevelsResponse_Flood": ".follow_levels_response",
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
    "FollowLevelsResponse",
    "FollowLevelsResponseEbb",
    "FollowLevelsResponseFlood",
    "FollowLevelsResponse_Ebb",
    "FollowLevelsResponse_Flood",
]
