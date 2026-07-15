



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .algorithm import Algorithm
    from .app_d import AppD
    from .app_d_id import AppDId
    from .app_d_version import AppDVersion
    from .app_external_cpd import AppExternalCpd
    from .app_name import AppName
    from .app_pkg_artifact_info import AppPkgArtifactInfo
    from .app_pkg_filter import AppPkgFilter
    from .app_pkg_id import AppPkgId
    from .app_pkg_info import AppPkgInfo
    from .app_pkg_info_links import AppPkgInfoLinks
    from .app_pkg_info_modifications import AppPkgInfoModifications
    from .app_pkg_info_modifications_operation_state import AppPkgInfoModificationsOperationState
    from .app_pkg_notification_id import AppPkgNotificationId
    from .app_pkg_notification_links import AppPkgNotificationLinks
    from .app_pkg_notification_type import AppPkgNotificationType
    from .app_pkg_operational_state import AppPkgOperationalState
    from .app_pkg_subscription_info import AppPkgSubscriptionInfo
    from .app_pkg_subscription_info_id import AppPkgSubscriptionInfoId
    from .app_pkg_subscription_info_links import AppPkgSubscriptionInfoLinks
    from .app_pkg_subscription_link_list import AppPkgSubscriptionLinkList
    from .app_pkg_subscription_link_list_links import AppPkgSubscriptionLinkListLinks
    from .app_pkg_subscription_type import AppPkgSubscriptionType
    from .app_pkg_sw_image_info import AppPkgSwImageInfo
    from .app_provider import AppProvider
    from .app_software_version import AppSoftwareVersion
    from .callback_uri import CallbackUri
    from .category_ref import CategoryRef
    from .change_app_instance_state_op_config import ChangeAppInstanceStateOpConfig
    from .checksum import Checksum
    from .dns_rule_descriptor import DnsRuleDescriptor
    from .feature_dependency import FeatureDependency
    from .filter_type import FilterType
    from .hash import Hash
    from .href import Href
    from .interface_descriptor import InterfaceDescriptor
    from .interface_type import InterfaceType
    from .ip_address_type import IpAddressType
    from .key_value_pairs import KeyValuePairs
    from .latency_descriptor import LatencyDescriptor
    from .link_type import LinkType
    from .not_specified import NotSpecified
    from .onboarding_state import OnboardingState
    from .problem_details import ProblemDetails
    from .security_info import SecurityInfo
    from .ser_name import SerName
    from .ser_version import SerVersion
    from .serializer_types import SerializerTypes
    from .serializers import Serializers
    from .service_dependency import ServiceDependency
    from .service_descriptor import ServiceDescriptor
    from .subscription_id import SubscriptionId
    from .subscriptions_app_pkg_subscription import SubscriptionsAppPkgSubscription
    from .subsctiption_type_app_pkg import SubsctiptionTypeAppPkg
    from .sw_image_descriptor import SwImageDescriptor
    from .terminate_app_instance_op_config import TerminateAppInstanceOpConfig
    from .time_stamp import TimeStamp
    from .traffic_filter import TrafficFilter
    from .traffic_rule_descriptor import TrafficRuleDescriptor
    from .transport_dependency import TransportDependency
    from .transport_descriptor import TransportDescriptor
    from .transport_types import TransportTypes
    from .transports_supported import TransportsSupported
    from .tunnel_info import TunnelInfo
    from .tunnel_type import TunnelType
    from .uri import Uri
    from .usage_state import UsageState
    from .virtual_compute_description import VirtualComputeDescription
    from .virtual_network_interface_requirements import VirtualNetworkInterfaceRequirements
    from .virtual_storage_descriptor import VirtualStorageDescriptor
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "Algorithm": ".algorithm",
    "AppD": ".app_d",
    "AppDId": ".app_d_id",
    "AppDVersion": ".app_d_version",
    "AppExternalCpd": ".app_external_cpd",
    "AppName": ".app_name",
    "AppPkgArtifactInfo": ".app_pkg_artifact_info",
    "AppPkgFilter": ".app_pkg_filter",
    "AppPkgId": ".app_pkg_id",
    "AppPkgInfo": ".app_pkg_info",
    "AppPkgInfoLinks": ".app_pkg_info_links",
    "AppPkgInfoModifications": ".app_pkg_info_modifications",
    "AppPkgInfoModificationsOperationState": ".app_pkg_info_modifications_operation_state",
    "AppPkgNotificationId": ".app_pkg_notification_id",
    "AppPkgNotificationLinks": ".app_pkg_notification_links",
    "AppPkgNotificationType": ".app_pkg_notification_type",
    "AppPkgOperationalState": ".app_pkg_operational_state",
    "AppPkgSubscriptionInfo": ".app_pkg_subscription_info",
    "AppPkgSubscriptionInfoId": ".app_pkg_subscription_info_id",
    "AppPkgSubscriptionInfoLinks": ".app_pkg_subscription_info_links",
    "AppPkgSubscriptionLinkList": ".app_pkg_subscription_link_list",
    "AppPkgSubscriptionLinkListLinks": ".app_pkg_subscription_link_list_links",
    "AppPkgSubscriptionType": ".app_pkg_subscription_type",
    "AppPkgSwImageInfo": ".app_pkg_sw_image_info",
    "AppProvider": ".app_provider",
    "AppSoftwareVersion": ".app_software_version",
    "CallbackUri": ".callback_uri",
    "CategoryRef": ".category_ref",
    "ChangeAppInstanceStateOpConfig": ".change_app_instance_state_op_config",
    "Checksum": ".checksum",
    "DnsRuleDescriptor": ".dns_rule_descriptor",
    "FeatureDependency": ".feature_dependency",
    "FilterType": ".filter_type",
    "Hash": ".hash",
    "Href": ".href",
    "InterfaceDescriptor": ".interface_descriptor",
    "InterfaceType": ".interface_type",
    "IpAddressType": ".ip_address_type",
    "KeyValuePairs": ".key_value_pairs",
    "LatencyDescriptor": ".latency_descriptor",
    "LinkType": ".link_type",
    "NotSpecified": ".not_specified",
    "OnboardingState": ".onboarding_state",
    "ProblemDetails": ".problem_details",
    "SecurityInfo": ".security_info",
    "SerName": ".ser_name",
    "SerVersion": ".ser_version",
    "SerializerTypes": ".serializer_types",
    "Serializers": ".serializers",
    "ServiceDependency": ".service_dependency",
    "ServiceDescriptor": ".service_descriptor",
    "SubscriptionId": ".subscription_id",
    "SubscriptionsAppPkgSubscription": ".subscriptions_app_pkg_subscription",
    "SubsctiptionTypeAppPkg": ".subsctiption_type_app_pkg",
    "SwImageDescriptor": ".sw_image_descriptor",
    "TerminateAppInstanceOpConfig": ".terminate_app_instance_op_config",
    "TimeStamp": ".time_stamp",
    "TrafficFilter": ".traffic_filter",
    "TrafficRuleDescriptor": ".traffic_rule_descriptor",
    "TransportDependency": ".transport_dependency",
    "TransportDescriptor": ".transport_descriptor",
    "TransportTypes": ".transport_types",
    "TransportsSupported": ".transports_supported",
    "TunnelInfo": ".tunnel_info",
    "TunnelType": ".tunnel_type",
    "Uri": ".uri",
    "UsageState": ".usage_state",
    "VirtualComputeDescription": ".virtual_compute_description",
    "VirtualNetworkInterfaceRequirements": ".virtual_network_interface_requirements",
    "VirtualStorageDescriptor": ".virtual_storage_descriptor",
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
    "Action",
    "Algorithm",
    "AppD",
    "AppDId",
    "AppDVersion",
    "AppExternalCpd",
    "AppName",
    "AppPkgArtifactInfo",
    "AppPkgFilter",
    "AppPkgId",
    "AppPkgInfo",
    "AppPkgInfoLinks",
    "AppPkgInfoModifications",
    "AppPkgInfoModificationsOperationState",
    "AppPkgNotificationId",
    "AppPkgNotificationLinks",
    "AppPkgNotificationType",
    "AppPkgOperationalState",
    "AppPkgSubscriptionInfo",
    "AppPkgSubscriptionInfoId",
    "AppPkgSubscriptionInfoLinks",
    "AppPkgSubscriptionLinkList",
    "AppPkgSubscriptionLinkListLinks",
    "AppPkgSubscriptionType",
    "AppPkgSwImageInfo",
    "AppProvider",
    "AppSoftwareVersion",
    "CallbackUri",
    "CategoryRef",
    "ChangeAppInstanceStateOpConfig",
    "Checksum",
    "DnsRuleDescriptor",
    "FeatureDependency",
    "FilterType",
    "Hash",
    "Href",
    "InterfaceDescriptor",
    "InterfaceType",
    "IpAddressType",
    "KeyValuePairs",
    "LatencyDescriptor",
    "LinkType",
    "NotSpecified",
    "OnboardingState",
    "ProblemDetails",
    "SecurityInfo",
    "SerName",
    "SerVersion",
    "SerializerTypes",
    "Serializers",
    "ServiceDependency",
    "ServiceDescriptor",
    "SubscriptionId",
    "SubscriptionsAppPkgSubscription",
    "SubsctiptionTypeAppPkg",
    "SwImageDescriptor",
    "TerminateAppInstanceOpConfig",
    "TimeStamp",
    "TrafficFilter",
    "TrafficRuleDescriptor",
    "TransportDependency",
    "TransportDescriptor",
    "TransportTypes",
    "TransportsSupported",
    "TunnelInfo",
    "TunnelType",
    "Uri",
    "UsageState",
    "VirtualComputeDescription",
    "VirtualNetworkInterfaceRequirements",
    "VirtualStorageDescriptor",
]
