



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ContextDescription,
        ContextUuid,
        ContextsResponse,
        ContextsResponseItem,
        CustomIdentifier,
        DeletionDeniedReason,
        DeletionDeniedResponse,
        DeletionReadyResponse,
        DeletionReadyResponseDeletionFeedback,
        DeletionRequestGrounds,
        DeletionRequestResponse,
        DeletionRequestUuid,
        EmailAddress,
        ExportPartialReadyResponse,
        ExportReadyResponse,
        ExportRequestResponse,
        ExportRequestUuid,
        GovernmentIdNumber,
        RequiredAuth,
        RequiredAuthItemItem,
        SuppliedAuth,
        SuppliedAuthCustomIdentifier,
        SuppliedAuthGovernmentIdNumber,
        TelephoneNumber,
    )
    from .errors import BadRequestError, ForbiddenError, NotFoundError, UnavailableForLegalReasonsError
    from . import deletion, export, flags
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ContextDescription": ".types",
    "ContextUuid": ".types",
    "ContextsResponse": ".types",
    "ContextsResponseItem": ".types",
    "CustomIdentifier": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeletionDeniedReason": ".types",
    "DeletionDeniedResponse": ".types",
    "DeletionReadyResponse": ".types",
    "DeletionReadyResponseDeletionFeedback": ".types",
    "DeletionRequestGrounds": ".types",
    "DeletionRequestResponse": ".types",
    "DeletionRequestUuid": ".types",
    "EmailAddress": ".types",
    "ExportPartialReadyResponse": ".types",
    "ExportReadyResponse": ".types",
    "ExportRequestResponse": ".types",
    "ExportRequestUuid": ".types",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "GovernmentIdNumber": ".types",
    "NotFoundError": ".errors",
    "RequiredAuth": ".types",
    "RequiredAuthItemItem": ".types",
    "SuppliedAuth": ".types",
    "SuppliedAuthCustomIdentifier": ".types",
    "SuppliedAuthGovernmentIdNumber": ".types",
    "TelephoneNumber": ".types",
    "UnavailableForLegalReasonsError": ".errors",
    "__version__": ".version",
    "deletion": ".deletion",
    "export": ".export",
    "flags": ".flags",
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
    "BadRequestError",
    "ContextDescription",
    "ContextUuid",
    "ContextsResponse",
    "ContextsResponseItem",
    "CustomIdentifier",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeletionDeniedReason",
    "DeletionDeniedResponse",
    "DeletionReadyResponse",
    "DeletionReadyResponseDeletionFeedback",
    "DeletionRequestGrounds",
    "DeletionRequestResponse",
    "DeletionRequestUuid",
    "EmailAddress",
    "ExportPartialReadyResponse",
    "ExportReadyResponse",
    "ExportRequestResponse",
    "ExportRequestUuid",
    "FernApi",
    "ForbiddenError",
    "GovernmentIdNumber",
    "NotFoundError",
    "RequiredAuth",
    "RequiredAuthItemItem",
    "SuppliedAuth",
    "SuppliedAuthCustomIdentifier",
    "SuppliedAuthGovernmentIdNumber",
    "TelephoneNumber",
    "UnavailableForLegalReasonsError",
    "__version__",
    "deletion",
    "export",
    "flags",
]
