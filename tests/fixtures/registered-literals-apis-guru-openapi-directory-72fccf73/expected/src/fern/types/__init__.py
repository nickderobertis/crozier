



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_response import AccountResponse
    from .account_response_provider import AccountResponseProvider
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_invalid_params_item import BadRequestErrorBodyInvalidParamsItem
    from .conflict_error_body import ConflictErrorBody
    from .forbidden_error_body import ForbiddenErrorBody
    from .four_hundred_one_response import FourHundredOneResponse
    from .four_hundred_three_response import FourHundredThreeResponse
    from .get_all_account_response import GetAllAccountResponse
    from .messenger_account_response import MessengerAccountResponse
    from .vsm_account_response import VsmAccountResponse
    from .wa_account_response import WaAccountResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AccountResponse": ".account_response",
    "AccountResponseProvider": ".account_response_provider",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyInvalidParamsItem": ".bad_request_error_body_invalid_params_item",
    "ConflictErrorBody": ".conflict_error_body",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "FourHundredOneResponse": ".four_hundred_one_response",
    "FourHundredThreeResponse": ".four_hundred_three_response",
    "GetAllAccountResponse": ".get_all_account_response",
    "MessengerAccountResponse": ".messenger_account_response",
    "VsmAccountResponse": ".vsm_account_response",
    "WaAccountResponse": ".wa_account_response",
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
    "AccountResponse",
    "AccountResponseProvider",
    "BadRequestErrorBody",
    "BadRequestErrorBodyInvalidParamsItem",
    "ConflictErrorBody",
    "ForbiddenErrorBody",
    "FourHundredOneResponse",
    "FourHundredThreeResponse",
    "GetAllAccountResponse",
    "MessengerAccountResponse",
    "VsmAccountResponse",
    "WaAccountResponse",
]
