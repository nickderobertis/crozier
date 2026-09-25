



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account import Account
    from .account_attributes import AccountAttributes
    from .account_list_response import AccountListResponse
    from .account_list_response_links import AccountListResponseLinks
    from .account_list_response_meta import AccountListResponseMeta
    from .account_response import AccountResponse
    from .error_response import ErrorResponse
    from .error_response_errors_item import ErrorResponseErrorsItem
    from .error_response_errors_item_source import ErrorResponseErrorsItemSource
    from .json_api_resource import JsonApiResource
    from .json_api_resource_links import JsonApiResourceLinks
    from .prospect import Prospect
    from .prospect_attributes import ProspectAttributes
    from .prospect_list_response import ProspectListResponse
    from .prospect_response import ProspectResponse
    from .sequence_list_response import SequenceListResponse
    from .sequence_response import SequenceResponse
    from .sequence_response_data import SequenceResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".account",
    "AccountAttributes": ".account_attributes",
    "AccountListResponse": ".account_list_response",
    "AccountListResponseLinks": ".account_list_response_links",
    "AccountListResponseMeta": ".account_list_response_meta",
    "AccountResponse": ".account_response",
    "ErrorResponse": ".error_response",
    "ErrorResponseErrorsItem": ".error_response_errors_item",
    "ErrorResponseErrorsItemSource": ".error_response_errors_item_source",
    "JsonApiResource": ".json_api_resource",
    "JsonApiResourceLinks": ".json_api_resource_links",
    "Prospect": ".prospect",
    "ProspectAttributes": ".prospect_attributes",
    "ProspectListResponse": ".prospect_list_response",
    "ProspectResponse": ".prospect_response",
    "SequenceListResponse": ".sequence_list_response",
    "SequenceResponse": ".sequence_response",
    "SequenceResponseData": ".sequence_response_data",
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
    "Account",
    "AccountAttributes",
    "AccountListResponse",
    "AccountListResponseLinks",
    "AccountListResponseMeta",
    "AccountResponse",
    "ErrorResponse",
    "ErrorResponseErrorsItem",
    "ErrorResponseErrorsItemSource",
    "JsonApiResource",
    "JsonApiResourceLinks",
    "Prospect",
    "ProspectAttributes",
    "ProspectListResponse",
    "ProspectResponse",
    "SequenceListResponse",
    "SequenceResponse",
    "SequenceResponseData",
]
