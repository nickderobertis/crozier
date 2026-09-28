



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .amount import Amount
    from .authentication_decision import AuthenticationDecision
    from .authentication_decision_status import AuthenticationDecisionStatus
    from .authentication_info import AuthenticationInfo
    from .authentication_info_challenge_indicator import AuthenticationInfoChallengeIndicator
    from .authentication_info_device_channel import AuthenticationInfoDeviceChannel
    from .authentication_info_exemption_indicator import AuthenticationInfoExemptionIndicator
    from .authentication_info_message_category import AuthenticationInfoMessageCategory
    from .authentication_info_trans_status import AuthenticationInfoTransStatus
    from .authentication_info_trans_status_reason import AuthenticationInfoTransStatusReason
    from .authentication_info_type import AuthenticationInfoType
    from .authentication_notification_data import AuthenticationNotificationData
    from .authentication_notification_data_status import AuthenticationNotificationDataStatus
    from .authentication_notification_request import AuthenticationNotificationRequest
    from .authentication_notification_request_type import AuthenticationNotificationRequestType
    from .balance_platform_notification_response import BalancePlatformNotificationResponse
    from .challenge_info import ChallengeInfo
    from .challenge_info_challenge_cancel import ChallengeInfoChallengeCancel
    from .challenge_info_flow import ChallengeInfoFlow
    from .purchase import Purchase
    from .purchase_info import PurchaseInfo
    from .relayed_authentication_request import RelayedAuthenticationRequest
    from .relayed_authentication_request_type import RelayedAuthenticationRequestType
    from .relayed_authentication_response import RelayedAuthenticationResponse
    from .resource import Resource
    from .service_error import ServiceError
_dynamic_imports: typing.Dict[str, str] = {
    "Amount": ".amount",
    "AuthenticationDecision": ".authentication_decision",
    "AuthenticationDecisionStatus": ".authentication_decision_status",
    "AuthenticationInfo": ".authentication_info",
    "AuthenticationInfoChallengeIndicator": ".authentication_info_challenge_indicator",
    "AuthenticationInfoDeviceChannel": ".authentication_info_device_channel",
    "AuthenticationInfoExemptionIndicator": ".authentication_info_exemption_indicator",
    "AuthenticationInfoMessageCategory": ".authentication_info_message_category",
    "AuthenticationInfoTransStatus": ".authentication_info_trans_status",
    "AuthenticationInfoTransStatusReason": ".authentication_info_trans_status_reason",
    "AuthenticationInfoType": ".authentication_info_type",
    "AuthenticationNotificationData": ".authentication_notification_data",
    "AuthenticationNotificationDataStatus": ".authentication_notification_data_status",
    "AuthenticationNotificationRequest": ".authentication_notification_request",
    "AuthenticationNotificationRequestType": ".authentication_notification_request_type",
    "BalancePlatformNotificationResponse": ".balance_platform_notification_response",
    "ChallengeInfo": ".challenge_info",
    "ChallengeInfoChallengeCancel": ".challenge_info_challenge_cancel",
    "ChallengeInfoFlow": ".challenge_info_flow",
    "Purchase": ".purchase",
    "PurchaseInfo": ".purchase_info",
    "RelayedAuthenticationRequest": ".relayed_authentication_request",
    "RelayedAuthenticationRequestType": ".relayed_authentication_request_type",
    "RelayedAuthenticationResponse": ".relayed_authentication_response",
    "Resource": ".resource",
    "ServiceError": ".service_error",
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
    "Purchase",
    "PurchaseInfo",
    "RelayedAuthenticationRequest",
    "RelayedAuthenticationRequestType",
    "RelayedAuthenticationResponse",
    "Resource",
    "ServiceError",
]
