



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .hull_request_hull import HullRequestHull, HullRequestHull_Steel, HullRequestHull_Timber
    from .hull_request_hull_steel import HullRequestHullSteel
    from .hull_request_hull_timber import HullRequestHullTimber
_dynamic_imports: typing.Dict[str, str] = {
    "HullRequestHull": ".hull_request_hull",
    "HullRequestHullSteel": ".hull_request_hull_steel",
    "HullRequestHullTimber": ".hull_request_hull_timber",
    "HullRequestHull_Steel": ".hull_request_hull",
    "HullRequestHull_Timber": ".hull_request_hull",
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
    "HullRequestHull",
    "HullRequestHullSteel",
    "HullRequestHullTimber",
    "HullRequestHull_Steel",
    "HullRequestHull_Timber",
]
