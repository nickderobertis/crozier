



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bulk_create_pronunciations_response import BulkCreatePronunciationsResponse
    from .create_pronunciation_response import CreatePronunciationResponse
    from .delete_pronunciation_response import DeletePronunciationResponse
    from .get_pronunciation_response import GetPronunciationResponse
    from .list_pronunciations_request_status import ListPronunciationsRequestStatus
    from .list_pronunciations_response import ListPronunciationsResponse
    from .update_pronunciation_response import UpdatePronunciationResponse
_dynamic_imports: typing.Dict[str, str] = {
    "BulkCreatePronunciationsResponse": ".bulk_create_pronunciations_response",
    "CreatePronunciationResponse": ".create_pronunciation_response",
    "DeletePronunciationResponse": ".delete_pronunciation_response",
    "GetPronunciationResponse": ".get_pronunciation_response",
    "ListPronunciationsRequestStatus": ".list_pronunciations_request_status",
    "ListPronunciationsResponse": ".list_pronunciations_response",
    "UpdatePronunciationResponse": ".update_pronunciation_response",
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
    "BulkCreatePronunciationsResponse",
    "CreatePronunciationResponse",
    "DeletePronunciationResponse",
    "GetPronunciationResponse",
    "ListPronunciationsRequestStatus",
    "ListPronunciationsResponse",
    "UpdatePronunciationResponse",
]
