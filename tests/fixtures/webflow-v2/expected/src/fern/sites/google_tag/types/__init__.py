



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_google_tag_response import DeleteGoogleTagResponse
    from .delete_google_tag_response_google_tag_ids_item import DeleteGoogleTagResponseGoogleTagIdsItem
    from .list_google_tag_response import ListGoogleTagResponse
    from .list_google_tag_response_google_tag_ids_item import ListGoogleTagResponseGoogleTagIdsItem
    from .upsert_google_tag_request_google_tag_ids_item import UpsertGoogleTagRequestGoogleTagIdsItem
    from .upsert_google_tag_response import UpsertGoogleTagResponse
    from .upsert_google_tag_response_google_tag_ids_item import UpsertGoogleTagResponseGoogleTagIdsItem
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteGoogleTagResponse": ".delete_google_tag_response",
    "DeleteGoogleTagResponseGoogleTagIdsItem": ".delete_google_tag_response_google_tag_ids_item",
    "ListGoogleTagResponse": ".list_google_tag_response",
    "ListGoogleTagResponseGoogleTagIdsItem": ".list_google_tag_response_google_tag_ids_item",
    "UpsertGoogleTagRequestGoogleTagIdsItem": ".upsert_google_tag_request_google_tag_ids_item",
    "UpsertGoogleTagResponse": ".upsert_google_tag_response",
    "UpsertGoogleTagResponseGoogleTagIdsItem": ".upsert_google_tag_response_google_tag_ids_item",
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
    "DeleteGoogleTagResponse",
    "DeleteGoogleTagResponseGoogleTagIdsItem",
    "ListGoogleTagResponse",
    "ListGoogleTagResponseGoogleTagIdsItem",
    "UpsertGoogleTagRequestGoogleTagIdsItem",
    "UpsertGoogleTagResponse",
    "UpsertGoogleTagResponseGoogleTagIdsItem",
]
