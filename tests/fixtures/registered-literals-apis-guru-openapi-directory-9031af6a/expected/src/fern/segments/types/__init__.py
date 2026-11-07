



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_account_segments_response import GetAccountSegmentsResponse
    from .get_account_segments_response_data_item import GetAccountSegmentsResponseDataItem
    from .get_account_segments_response_meta import GetAccountSegmentsResponseMeta
    from .get_user_segments_response import GetUserSegmentsResponse
    from .get_user_segments_response_data_item import GetUserSegmentsResponseDataItem
    from .get_user_segments_response_meta import GetUserSegmentsResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "GetAccountSegmentsResponse": ".get_account_segments_response",
    "GetAccountSegmentsResponseDataItem": ".get_account_segments_response_data_item",
    "GetAccountSegmentsResponseMeta": ".get_account_segments_response_meta",
    "GetUserSegmentsResponse": ".get_user_segments_response",
    "GetUserSegmentsResponseDataItem": ".get_user_segments_response_data_item",
    "GetUserSegmentsResponseMeta": ".get_user_segments_response_meta",
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
    "GetAccountSegmentsResponse",
    "GetAccountSegmentsResponseDataItem",
    "GetAccountSegmentsResponseMeta",
    "GetUserSegmentsResponse",
    "GetUserSegmentsResponseDataItem",
    "GetUserSegmentsResponseMeta",
]
