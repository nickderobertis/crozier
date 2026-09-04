



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Amount,
        BalancePlatformNotificationResponse,
        ManagedRiskBalanceBlockReleasedNotificationRequest,
        ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment,
        ManagedRiskBalanceBlockReleasedNotificationRequestType,
        ManagedRiskReserveWaiverAppliedNotificationRequest,
        ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment,
        ManagedRiskReserveWaiverAppliedNotificationRequestType,
        ManagedRiskReserveWaiverRemovedNotificationRequest,
        ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment,
        ManagedRiskReserveWaiverRemovedNotificationRequestType,
        ManagedRiskRollingReserveAppliedNotificationRequest,
        ManagedRiskRollingReserveAppliedNotificationRequestEnvironment,
        ManagedRiskRollingReserveAppliedNotificationRequestType,
        ManagedRiskRollingReserveLiftedNotificationRequest,
        ManagedRiskRollingReserveLiftedNotificationRequestEnvironment,
        ManagedRiskRollingReserveLiftedNotificationRequestType,
        ManagedRiskRollingReserveUpdatedNotificationRequest,
        ManagedRiskRollingReserveUpdatedNotificationRequestEnvironment,
        ManagedRiskRollingReserveUpdatedNotificationRequestType,
        ManagedRiskSettlementDelayLiftedNotificationRequest,
        ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment,
        ManagedRiskSettlementDelayLiftedNotificationRequestType,
        ManagedRiskSettlementDelayNotificationRequest,
        ManagedRiskSettlementDelayNotificationRequestEnvironment,
        ManagedRiskSettlementDelayNotificationRequestType,
        ReleaseBlockedBalanceNotificationData,
        ReserveWaiverAppliedNotificationResource,
        ReserveWaiverRemovedNotificationResource,
        ResourceReference,
        RollingReserveLiftedNotificationResource,
        RollingReserveNotificationResource,
        SettlementDelayConfiguration,
        SettlementDelayLiftedNotificationResource,
        SettlementDelayLiftedNotificationResourceReason,
        SettlementDelayNotificationResource,
        SettlementDelayNotificationResourceReason,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Amount": ".types",
    "AsyncFernApi": ".client",
    "BalancePlatformNotificationResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "ManagedRiskBalanceBlockReleasedNotificationRequest": ".types",
    "ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment": ".types",
    "ManagedRiskBalanceBlockReleasedNotificationRequestType": ".types",
    "ManagedRiskReserveWaiverAppliedNotificationRequest": ".types",
    "ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment": ".types",
    "ManagedRiskReserveWaiverAppliedNotificationRequestType": ".types",
    "ManagedRiskReserveWaiverRemovedNotificationRequest": ".types",
    "ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment": ".types",
    "ManagedRiskReserveWaiverRemovedNotificationRequestType": ".types",
    "ManagedRiskRollingReserveAppliedNotificationRequest": ".types",
    "ManagedRiskRollingReserveAppliedNotificationRequestEnvironment": ".types",
    "ManagedRiskRollingReserveAppliedNotificationRequestType": ".types",
    "ManagedRiskRollingReserveLiftedNotificationRequest": ".types",
    "ManagedRiskRollingReserveLiftedNotificationRequestEnvironment": ".types",
    "ManagedRiskRollingReserveLiftedNotificationRequestType": ".types",
    "ManagedRiskRollingReserveUpdatedNotificationRequest": ".types",
    "ManagedRiskRollingReserveUpdatedNotificationRequestEnvironment": ".types",
    "ManagedRiskRollingReserveUpdatedNotificationRequestType": ".types",
    "ManagedRiskSettlementDelayLiftedNotificationRequest": ".types",
    "ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment": ".types",
    "ManagedRiskSettlementDelayLiftedNotificationRequestType": ".types",
    "ManagedRiskSettlementDelayNotificationRequest": ".types",
    "ManagedRiskSettlementDelayNotificationRequestEnvironment": ".types",
    "ManagedRiskSettlementDelayNotificationRequestType": ".types",
    "ReleaseBlockedBalanceNotificationData": ".types",
    "ReserveWaiverAppliedNotificationResource": ".types",
    "ReserveWaiverRemovedNotificationResource": ".types",
    "ResourceReference": ".types",
    "RollingReserveLiftedNotificationResource": ".types",
    "RollingReserveNotificationResource": ".types",
    "SettlementDelayConfiguration": ".types",
    "SettlementDelayLiftedNotificationResource": ".types",
    "SettlementDelayLiftedNotificationResourceReason": ".types",
    "SettlementDelayNotificationResource": ".types",
    "SettlementDelayNotificationResourceReason": ".types",
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
    "BalancePlatformNotificationResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "ManagedRiskBalanceBlockReleasedNotificationRequest",
    "ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment",
    "ManagedRiskBalanceBlockReleasedNotificationRequestType",
    "ManagedRiskReserveWaiverAppliedNotificationRequest",
    "ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment",
    "ManagedRiskReserveWaiverAppliedNotificationRequestType",
    "ManagedRiskReserveWaiverRemovedNotificationRequest",
    "ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment",
    "ManagedRiskReserveWaiverRemovedNotificationRequestType",
    "ManagedRiskRollingReserveAppliedNotificationRequest",
    "ManagedRiskRollingReserveAppliedNotificationRequestEnvironment",
    "ManagedRiskRollingReserveAppliedNotificationRequestType",
    "ManagedRiskRollingReserveLiftedNotificationRequest",
    "ManagedRiskRollingReserveLiftedNotificationRequestEnvironment",
    "ManagedRiskRollingReserveLiftedNotificationRequestType",
    "ManagedRiskRollingReserveUpdatedNotificationRequest",
    "ManagedRiskRollingReserveUpdatedNotificationRequestEnvironment",
    "ManagedRiskRollingReserveUpdatedNotificationRequestType",
    "ManagedRiskSettlementDelayLiftedNotificationRequest",
    "ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment",
    "ManagedRiskSettlementDelayLiftedNotificationRequestType",
    "ManagedRiskSettlementDelayNotificationRequest",
    "ManagedRiskSettlementDelayNotificationRequestEnvironment",
    "ManagedRiskSettlementDelayNotificationRequestType",
    "ReleaseBlockedBalanceNotificationData",
    "ReserveWaiverAppliedNotificationResource",
    "ReserveWaiverRemovedNotificationResource",
    "ResourceReference",
    "RollingReserveLiftedNotificationResource",
    "RollingReserveNotificationResource",
    "SettlementDelayConfiguration",
    "SettlementDelayLiftedNotificationResource",
    "SettlementDelayLiftedNotificationResourceReason",
    "SettlementDelayNotificationResource",
    "SettlementDelayNotificationResourceReason",
    "__version__",
]
