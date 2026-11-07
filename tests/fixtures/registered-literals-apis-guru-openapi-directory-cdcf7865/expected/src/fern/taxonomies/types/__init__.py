



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .taxonomies_list_response_item import TaxonomiesListResponseItem
    from .taxonomies_list_response_item_attributes import TaxonomiesListResponseItemAttributes
    from .taxonomies_list_response_item_links import TaxonomiesListResponseItemLinks
    from .taxonomies_read_response import TaxonomiesReadResponse
    from .taxonomies_read_response_attributes import TaxonomiesReadResponseAttributes
    from .taxonomies_read_response_links import TaxonomiesReadResponseLinks
_dynamic_imports: typing.Dict[str, str] = {
    "TaxonomiesListResponseItem": ".taxonomies_list_response_item",
    "TaxonomiesListResponseItemAttributes": ".taxonomies_list_response_item_attributes",
    "TaxonomiesListResponseItemLinks": ".taxonomies_list_response_item_links",
    "TaxonomiesReadResponse": ".taxonomies_read_response",
    "TaxonomiesReadResponseAttributes": ".taxonomies_read_response_attributes",
    "TaxonomiesReadResponseLinks": ".taxonomies_read_response_links",
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
    "TaxonomiesListResponseItem",
    "TaxonomiesListResponseItemAttributes",
    "TaxonomiesListResponseItemLinks",
    "TaxonomiesReadResponse",
    "TaxonomiesReadResponseAttributes",
    "TaxonomiesReadResponseLinks",
]
