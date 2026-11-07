



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AccountResponse,
        AccountResponseProvider,
        BadRequestErrorBody,
        BadRequestErrorBodyInvalidParamsItem,
        ConflictErrorBody,
        ForbiddenErrorBody,
        FourHundredOneResponse,
        FourHundredThreeResponse,
        GetAllAccountResponse,
        MessengerAccountResponse,
        VsmAccountResponse,
        WaAccountResponse,
    )
    from .errors import BadRequestError, ConflictError, ForbiddenError, NotFoundError, UnauthorizedError
    from . import account, application, facebook_messenger, viber_service_message, whats_app
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .account import (
        GetAllAccountsRequestProvider,
        GetAllAccountsResponse,
        GetAllAccountsResponseLinks,
        GetAllAccountsResponseLinksFirst,
        GetAllAccountsResponseLinksLast,
        GetAllAccountsResponseLinksNext,
        GetAllAccountsResponseLinksPrev,
        GetAllAccountsResponseLinksSelf,
    )
    from .application import LinkApplicationRequestProvider, UnliWithoutApplicationnkApplicationRequestProvider
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .facebook_messenger import UpdateMessengerAccountResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AccountResponse": ".types",
    "AccountResponseProvider": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "BadRequestErrorBodyInvalidParamsItem": ".types",
    "ConflictError": ".errors",
    "ConflictErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "ForbiddenErrorBody": ".types",
    "FourHundredOneResponse": ".types",
    "FourHundredThreeResponse": ".types",
    "GetAllAccountResponse": ".types",
    "GetAllAccountsRequestProvider": ".account",
    "GetAllAccountsResponse": ".account",
    "GetAllAccountsResponseLinks": ".account",
    "GetAllAccountsResponseLinksFirst": ".account",
    "GetAllAccountsResponseLinksLast": ".account",
    "GetAllAccountsResponseLinksNext": ".account",
    "GetAllAccountsResponseLinksPrev": ".account",
    "GetAllAccountsResponseLinksSelf": ".account",
    "LinkApplicationRequestProvider": ".application",
    "MessengerAccountResponse": ".types",
    "NotFoundError": ".errors",
    "UnauthorizedError": ".errors",
    "UnliWithoutApplicationnkApplicationRequestProvider": ".application",
    "UpdateMessengerAccountResponse": ".facebook_messenger",
    "VsmAccountResponse": ".types",
    "WaAccountResponse": ".types",
    "__version__": ".version",
    "account": ".account",
    "application": ".application",
    "facebook_messenger": ".facebook_messenger",
    "viber_service_message": ".viber_service_message",
    "whats_app": ".whats_app",
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
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestErrorBody",
    "BadRequestErrorBodyInvalidParamsItem",
    "ConflictError",
    "ConflictErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "ForbiddenErrorBody",
    "FourHundredOneResponse",
    "FourHundredThreeResponse",
    "GetAllAccountResponse",
    "GetAllAccountsRequestProvider",
    "GetAllAccountsResponse",
    "GetAllAccountsResponseLinks",
    "GetAllAccountsResponseLinksFirst",
    "GetAllAccountsResponseLinksLast",
    "GetAllAccountsResponseLinksNext",
    "GetAllAccountsResponseLinksPrev",
    "GetAllAccountsResponseLinksSelf",
    "LinkApplicationRequestProvider",
    "MessengerAccountResponse",
    "NotFoundError",
    "UnauthorizedError",
    "UnliWithoutApplicationnkApplicationRequestProvider",
    "UpdateMessengerAccountResponse",
    "VsmAccountResponse",
    "WaAccountResponse",
    "__version__",
    "account",
    "application",
    "facebook_messenger",
    "viber_service_message",
    "whats_app",
]
