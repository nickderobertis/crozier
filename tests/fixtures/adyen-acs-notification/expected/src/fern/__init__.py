



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Amount,
        AuthenticationDecision,
        AuthenticationDecisionStatus,
        AuthenticationInfo,
        AuthenticationInfoChallengeIndicator,
        AuthenticationInfoDeviceChannel,
        AuthenticationInfoExemptionIndicator,
        AuthenticationInfoMessageCategory,
        AuthenticationInfoTransStatus,
        AuthenticationInfoTransStatusReason,
        AuthenticationInfoType,
        AuthenticationNotificationData,
        AuthenticationNotificationDataStatus,
        AuthenticationNotificationRequest,
        AuthenticationNotificationRequestType,
        BalancePlatformNotificationResponse,
        ChallengeInfo,
        ChallengeInfoChallengeCancel,
        ChallengeInfoFlow,
        Purchase,
        PurchaseInfo,
        RelayedAuthenticationRequest,
        RelayedAuthenticationRequestType,
        RelayedAuthenticationResponse,
        Resource,
        ServiceError,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Amount": ".types",
    "AsyncFernApi": ".client",
    "AuthenticationDecision": ".types",
    "AuthenticationDecisionStatus": ".types",
    "AuthenticationInfo": ".types",
    "AuthenticationInfoChallengeIndicator": ".types",
    "AuthenticationInfoDeviceChannel": ".types",
    "AuthenticationInfoExemptionIndicator": ".types",
    "AuthenticationInfoMessageCategory": ".types",
    "AuthenticationInfoTransStatus": ".types",
    "AuthenticationInfoTransStatusReason": ".types",
    "AuthenticationInfoType": ".types",
    "AuthenticationNotificationData": ".types",
    "AuthenticationNotificationDataStatus": ".types",
    "AuthenticationNotificationRequest": ".types",
    "AuthenticationNotificationRequestType": ".types",
    "BalancePlatformNotificationResponse": ".types",
    "ChallengeInfo": ".types",
    "ChallengeInfoChallengeCancel": ".types",
    "ChallengeInfoFlow": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "Purchase": ".types",
    "PurchaseInfo": ".types",
    "RelayedAuthenticationRequest": ".types",
    "RelayedAuthenticationRequestType": ".types",
    "RelayedAuthenticationResponse": ".types",
    "Resource": ".types",
    "ServiceError": ".types",
    "__version__": ".version",
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
    "Amount",
    "AsyncFernApi",
    "AuthenticationDecision",
    "AuthenticationDecisionStatus",
    "AuthenticationInfo",
    "AuthenticationInfoChallengeIndicator",
    "AuthenticationInfoDeviceChannel",
    "AuthenticationInfoExemptionIndicator",
    "AuthenticationInfoMessageCategory",
    "AuthenticationInfoTransStatus",
    "AuthenticationInfoTransStatusReason",
    "AuthenticationInfoType",
    "AuthenticationNotificationData",
    "AuthenticationNotificationDataStatus",
    "AuthenticationNotificationRequest",
    "AuthenticationNotificationRequestType",
    "BalancePlatformNotificationResponse",
    "ChallengeInfo",
    "ChallengeInfoChallengeCancel",
    "ChallengeInfoFlow",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "Purchase",
    "PurchaseInfo",
    "RelayedAuthenticationRequest",
    "RelayedAuthenticationRequestType",
    "RelayedAuthenticationResponse",
    "Resource",
    "ServiceError",
    "__version__",
]
