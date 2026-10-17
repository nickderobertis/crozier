



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .error_response import ErrorResponse
    from .error_response_error import ErrorResponseError
    from .media import Media
    from .media_type import MediaType
    from .statuses import Statuses
    from .statuses_entities import StatusesEntities
    from .statuses_entities_mentions_item import StatusesEntitiesMentionsItem
    from .statuses_entities_urls_item import StatusesEntitiesUrlsItem
    from .statuses_response import StatusesResponse
    from .user import User
_dynamic_imports: typing.Dict[str, str] = {
    "ErrorResponse": ".error_response",
    "ErrorResponseError": ".error_response_error",
    "Media": ".media",
    "MediaType": ".media_type",
    "Statuses": ".statuses",
    "StatusesEntities": ".statuses_entities",
    "StatusesEntitiesMentionsItem": ".statuses_entities_mentions_item",
    "StatusesEntitiesUrlsItem": ".statuses_entities_urls_item",
    "StatusesResponse": ".statuses_response",
    "User": ".user",
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
    "ErrorResponse",
    "ErrorResponseError",
    "Media",
    "MediaType",
    "Statuses",
    "StatusesEntities",
    "StatusesEntitiesMentionsItem",
    "StatusesEntitiesUrlsItem",
    "StatusesResponse",
    "User",
]
