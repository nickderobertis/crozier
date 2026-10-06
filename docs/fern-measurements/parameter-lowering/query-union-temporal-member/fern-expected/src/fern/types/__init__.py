



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_entries_request_season import ListEntriesRequestSeason
    from .list_entries_request_since import ListEntriesRequestSince
    from .list_entries_request_until import ListEntriesRequestUntil
    from .season import Season
_dynamic_imports: typing.Dict[str, str] = {
    "ListEntriesRequestSeason": ".list_entries_request_season",
    "ListEntriesRequestSince": ".list_entries_request_since",
    "ListEntriesRequestUntil": ".list_entries_request_until",
    "Season": ".season",
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


__all__ = ["ListEntriesRequestSeason", "ListEntriesRequestSince", "ListEntriesRequestUntil", "Season"]
