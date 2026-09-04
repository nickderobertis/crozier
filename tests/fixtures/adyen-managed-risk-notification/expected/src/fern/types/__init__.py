



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .amount import Amount
    from .balance_platform_notification_response import BalancePlatformNotificationResponse
    from .managed_risk_balance_block_released_notification_request import (
        ManagedRiskBalanceBlockReleasedNotificationRequest,
    )
    from .managed_risk_balance_block_released_notification_request_environment import (
        ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment,
    )
    from .managed_risk_balance_block_released_notification_request_type import (
        ManagedRiskBalanceBlockReleasedNotificationRequestType,
    )
    from .managed_risk_reserve_waiver_applied_notification_request import (
        ManagedRiskReserveWaiverAppliedNotificationRequest,
    )
    from .managed_risk_reserve_waiver_applied_notification_request_environment import (
        ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment,
    )
    from .managed_risk_reserve_waiver_applied_notification_request_type import (
        ManagedRiskReserveWaiverAppliedNotificationRequestType,
    )
    from .managed_risk_reserve_waiver_removed_notification_request import (
        ManagedRiskReserveWaiverRemovedNotificationRequest,
    )
    from .managed_risk_reserve_waiver_removed_notification_request_environment import (
        ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment,
    )
    from .managed_risk_reserve_waiver_removed_notification_request_type import (
        ManagedRiskReserveWaiverRemovedNotificationRequestType,
    )
    from .managed_risk_rolling_reserve_applied_notification_request import (
        ManagedRiskRollingReserveAppliedNotificationRequest,
    )
    from .managed_risk_rolling_reserve_applied_notification_request_environment import (
        ManagedRiskRollingReserveAppliedNotificationRequestEnvironment,
    )
    from .managed_risk_rolling_reserve_applied_notification_request_type import (
        ManagedRiskRollingReserveAppliedNotificationRequestType,
    )
    from .managed_risk_rolling_reserve_lifted_notification_request import (
        ManagedRiskRollingReserveLiftedNotificationRequest,
    )
    from .managed_risk_rolling_reserve_lifted_notification_request_environment import (
        ManagedRiskRollingReserveLiftedNotificationRequestEnvironment,
    )
    from .managed_risk_rolling_reserve_lifted_notification_request_type import (
        ManagedRiskRollingReserveLiftedNotificationRequestType,
    )
    from .managed_risk_rolling_reserve_updated_notification_request import (
        ManagedRiskRollingReserveUpdatedNotificationRequest,
    )
    from .managed_risk_rolling_reserve_updated_notification_request_environment import (
        ManagedRiskRollingReserveUpdatedNotificationRequestEnvironment,
    )
    from .managed_risk_rolling_reserve_updated_notification_request_type import (
        ManagedRiskRollingReserveUpdatedNotificationRequestType,
    )
    from .managed_risk_settlement_delay_lifted_notification_request import (
        ManagedRiskSettlementDelayLiftedNotificationRequest,
    )
    from .managed_risk_settlement_delay_lifted_notification_request_environment import (
        ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment,
    )
    from .managed_risk_settlement_delay_lifted_notification_request_type import (
        ManagedRiskSettlementDelayLiftedNotificationRequestType,
    )
    from .managed_risk_settlement_delay_notification_request import ManagedRiskSettlementDelayNotificationRequest
    from .managed_risk_settlement_delay_notification_request_environment import (
        ManagedRiskSettlementDelayNotificationRequestEnvironment,
    )
    from .managed_risk_settlement_delay_notification_request_type import (
        ManagedRiskSettlementDelayNotificationRequestType,
    )
    from .release_blocked_balance_notification_data import ReleaseBlockedBalanceNotificationData
    from .reserve_waiver_applied_notification_resource import ReserveWaiverAppliedNotificationResource
    from .reserve_waiver_removed_notification_resource import ReserveWaiverRemovedNotificationResource
    from .resource_reference import ResourceReference
    from .rolling_reserve_lifted_notification_resource import RollingReserveLiftedNotificationResource
    from .rolling_reserve_notification_resource import RollingReserveNotificationResource
    from .settlement_delay_configuration import SettlementDelayConfiguration
    from .settlement_delay_lifted_notification_resource import SettlementDelayLiftedNotificationResource
    from .settlement_delay_lifted_notification_resource_reason import SettlementDelayLiftedNotificationResourceReason
    from .settlement_delay_notification_resource import SettlementDelayNotificationResource
    from .settlement_delay_notification_resource_reason import SettlementDelayNotificationResourceReason
_dynamic_imports: typing.Dict[str, str] = {
    "Amount": ".amount",
    "BalancePlatformNotificationResponse": ".balance_platform_notification_response",
    "ManagedRiskBalanceBlockReleasedNotificationRequest": ".managed_risk_balance_block_released_notification_request",
    "ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment": ".managed_risk_balance_block_released_notification_request_environment",
    "ManagedRiskBalanceBlockReleasedNotificationRequestType": ".managed_risk_balance_block_released_notification_request_type",
    "ManagedRiskReserveWaiverAppliedNotificationRequest": ".managed_risk_reserve_waiver_applied_notification_request",
    "ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment": ".managed_risk_reserve_waiver_applied_notification_request_environment",
    "ManagedRiskReserveWaiverAppliedNotificationRequestType": ".managed_risk_reserve_waiver_applied_notification_request_type",
    "ManagedRiskReserveWaiverRemovedNotificationRequest": ".managed_risk_reserve_waiver_removed_notification_request",
    "ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment": ".managed_risk_reserve_waiver_removed_notification_request_environment",
    "ManagedRiskReserveWaiverRemovedNotificationRequestType": ".managed_risk_reserve_waiver_removed_notification_request_type",
    "ManagedRiskRollingReserveAppliedNotificationRequest": ".managed_risk_rolling_reserve_applied_notification_request",
    "ManagedRiskRollingReserveAppliedNotificationRequestEnvironment": ".managed_risk_rolling_reserve_applied_notification_request_environment",
    "ManagedRiskRollingReserveAppliedNotificationRequestType": ".managed_risk_rolling_reserve_applied_notification_request_type",
    "ManagedRiskRollingReserveLiftedNotificationRequest": ".managed_risk_rolling_reserve_lifted_notification_request",
    "ManagedRiskRollingReserveLiftedNotificationRequestEnvironment": ".managed_risk_rolling_reserve_lifted_notification_request_environment",
    "ManagedRiskRollingReserveLiftedNotificationRequestType": ".managed_risk_rolling_reserve_lifted_notification_request_type",
    "ManagedRiskRollingReserveUpdatedNotificationRequest": ".managed_risk_rolling_reserve_updated_notification_request",
    "ManagedRiskRollingReserveUpdatedNotificationRequestEnvironment": ".managed_risk_rolling_reserve_updated_notification_request_environment",
    "ManagedRiskRollingReserveUpdatedNotificationRequestType": ".managed_risk_rolling_reserve_updated_notification_request_type",
    "ManagedRiskSettlementDelayLiftedNotificationRequest": ".managed_risk_settlement_delay_lifted_notification_request",
    "ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment": ".managed_risk_settlement_delay_lifted_notification_request_environment",
    "ManagedRiskSettlementDelayLiftedNotificationRequestType": ".managed_risk_settlement_delay_lifted_notification_request_type",
    "ManagedRiskSettlementDelayNotificationRequest": ".managed_risk_settlement_delay_notification_request",
    "ManagedRiskSettlementDelayNotificationRequestEnvironment": ".managed_risk_settlement_delay_notification_request_environment",
    "ManagedRiskSettlementDelayNotificationRequestType": ".managed_risk_settlement_delay_notification_request_type",
    "ReleaseBlockedBalanceNotificationData": ".release_blocked_balance_notification_data",
    "ReserveWaiverAppliedNotificationResource": ".reserve_waiver_applied_notification_resource",
    "ReserveWaiverRemovedNotificationResource": ".reserve_waiver_removed_notification_resource",
    "ResourceReference": ".resource_reference",
    "RollingReserveLiftedNotificationResource": ".rolling_reserve_lifted_notification_resource",
    "RollingReserveNotificationResource": ".rolling_reserve_notification_resource",
    "SettlementDelayConfiguration": ".settlement_delay_configuration",
    "SettlementDelayLiftedNotificationResource": ".settlement_delay_lifted_notification_resource",
    "SettlementDelayLiftedNotificationResourceReason": ".settlement_delay_lifted_notification_resource_reason",
    "SettlementDelayNotificationResource": ".settlement_delay_notification_resource",
    "SettlementDelayNotificationResourceReason": ".settlement_delay_notification_resource_reason",
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
    "BalancePlatformNotificationResponse",
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
]
