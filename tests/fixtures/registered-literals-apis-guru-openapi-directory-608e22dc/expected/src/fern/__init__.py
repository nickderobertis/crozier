



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ConflictErrorBody,
        ForbiddenErrorBody,
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer,
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned,
        InvalidNumberTransferErrorResponse,
        ListBalanceTransfersResponse,
        ListBalanceTransfersResponseEmbedded,
        ListCreditTransfersResponse,
        ListCreditTransfersResponseEmbedded,
        NotFoundErrorBody,
        ShortcodeNotFound,
        SubaccountCreateResponse,
        SubaccountResponse,
        SubaccountsAllResponse,
        SubaccountsAllResponseEmbedded,
        TransferBalanceOrCreditRequest,
        TransferBalanceResponse,
        TransferCreditResponse,
        TransferNumberResponse,
        UnauthorizedErrorBody,
        UnprocessableEntityErrorBody,
        UnprocessableEntityErrorBodyInvalidParametersItem,
        UnprovisionedErrorResponse,
    )
    from .errors import ConflictError, ForbiddenError, NotFoundError, UnauthorizedError, UnprocessableEntityError
    from . import subaccount_management, transfers
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "ConflictError": ".errors",
    "ConflictErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "ForbiddenErrorBody": ".types",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer": ".types",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned": ".types",
    "InvalidNumberTransferErrorResponse": ".types",
    "ListBalanceTransfersResponse": ".types",
    "ListBalanceTransfersResponseEmbedded": ".types",
    "ListCreditTransfersResponse": ".types",
    "ListCreditTransfersResponseEmbedded": ".types",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "ShortcodeNotFound": ".types",
    "SubaccountCreateResponse": ".types",
    "SubaccountResponse": ".types",
    "SubaccountsAllResponse": ".types",
    "SubaccountsAllResponseEmbedded": ".types",
    "TransferBalanceOrCreditRequest": ".types",
    "TransferBalanceResponse": ".types",
    "TransferCreditResponse": ".types",
    "TransferNumberResponse": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "UnprocessableEntityError": ".errors",
    "UnprocessableEntityErrorBody": ".types",
    "UnprocessableEntityErrorBodyInvalidParametersItem": ".types",
    "UnprovisionedErrorResponse": ".types",
    "__version__": ".version",
    "subaccount_management": ".subaccount_management",
    "transfers": ".transfers",
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
    "AsyncFernApi",
    "ConflictError",
    "ConflictErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "ForbiddenErrorBody",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned",
    "InvalidNumberTransferErrorResponse",
    "ListBalanceTransfersResponse",
    "ListBalanceTransfersResponseEmbedded",
    "ListCreditTransfersResponse",
    "ListCreditTransfersResponseEmbedded",
    "NotFoundError",
    "NotFoundErrorBody",
    "ShortcodeNotFound",
    "SubaccountCreateResponse",
    "SubaccountResponse",
    "SubaccountsAllResponse",
    "SubaccountsAllResponseEmbedded",
    "TransferBalanceOrCreditRequest",
    "TransferBalanceResponse",
    "TransferCreditResponse",
    "TransferNumberResponse",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "UnprocessableEntityError",
    "UnprocessableEntityErrorBody",
    "UnprocessableEntityErrorBodyInvalidParametersItem",
    "UnprovisionedErrorResponse",
    "__version__",
    "subaccount_management",
    "transfers",
]
