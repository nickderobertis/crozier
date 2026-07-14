



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_subclasses_index_features_request_index import GetApiSubclassesIndexFeaturesRequestIndex
    from .get_api_subclasses_index_levels_request_index import GetApiSubclassesIndexLevelsRequestIndex
    from .get_api_subclasses_index_levels_subclass_level_features_request_index import (
        GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
    )
    from .get_api_subclasses_index_levels_subclass_level_request_index import (
        GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
    )
    from .get_api_subclasses_index_request_index import GetApiSubclassesIndexRequestIndex
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiSubclassesIndexFeaturesRequestIndex": ".get_api_subclasses_index_features_request_index",
    "GetApiSubclassesIndexLevelsRequestIndex": ".get_api_subclasses_index_levels_request_index",
    "GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex": ".get_api_subclasses_index_levels_subclass_level_features_request_index",
    "GetApiSubclassesIndexLevelsSubclassLevelRequestIndex": ".get_api_subclasses_index_levels_subclass_level_request_index",
    "GetApiSubclassesIndexRequestIndex": ".get_api_subclasses_index_request_index",
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
    "GetApiSubclassesIndexFeaturesRequestIndex",
    "GetApiSubclassesIndexLevelsRequestIndex",
    "GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex",
    "GetApiSubclassesIndexLevelsSubclassLevelRequestIndex",
    "GetApiSubclassesIndexRequestIndex",
]
