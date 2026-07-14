



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_classes_index_features_request_index import GetApiClassesIndexFeaturesRequestIndex
    from .get_api_classes_index_proficiencies_request_index import GetApiClassesIndexProficienciesRequestIndex
    from .get_api_classes_index_spells_request_index import GetApiClassesIndexSpellsRequestIndex
    from .get_api_classes_index_subclasses_request_index import GetApiClassesIndexSubclassesRequestIndex
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiClassesIndexFeaturesRequestIndex": ".get_api_classes_index_features_request_index",
    "GetApiClassesIndexProficienciesRequestIndex": ".get_api_classes_index_proficiencies_request_index",
    "GetApiClassesIndexSpellsRequestIndex": ".get_api_classes_index_spells_request_index",
    "GetApiClassesIndexSubclassesRequestIndex": ".get_api_classes_index_subclasses_request_index",
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
    "GetApiClassesIndexFeaturesRequestIndex",
    "GetApiClassesIndexProficienciesRequestIndex",
    "GetApiClassesIndexSpellsRequestIndex",
    "GetApiClassesIndexSubclassesRequestIndex",
]
