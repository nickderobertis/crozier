



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_catalogue_response import GetApiCatalogueResponse
    from .post_api_catalogue_response import PostApiCatalogueResponse
    from .put_api_catalogue_quantity_response import PutApiCatalogueQuantityResponse
    from .put_api_catalogue_quantity_response_articles_item import PutApiCatalogueQuantityResponseArticlesItem
    from .update_item_items_item import UpdateItemItemsItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiCatalogueResponse": ".get_api_catalogue_response",
    "PostApiCatalogueResponse": ".post_api_catalogue_response",
    "PutApiCatalogueQuantityResponse": ".put_api_catalogue_quantity_response",
    "PutApiCatalogueQuantityResponseArticlesItem": ".put_api_catalogue_quantity_response_articles_item",
    "UpdateItemItemsItem": ".update_item_items_item",
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
    "GetApiCatalogueResponse",
    "PostApiCatalogueResponse",
    "PutApiCatalogueQuantityResponse",
    "PutApiCatalogueQuantityResponseArticlesItem",
    "UpdateItemItemsItem",
]
