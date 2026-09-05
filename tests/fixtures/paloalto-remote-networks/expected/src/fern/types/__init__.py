



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bandwidth_allocation import BandwidthAllocation
    from .bandwidth_allocation_set import BandwidthAllocationSet
    from .bandwidth_allocation_set_v2 import BandwidthAllocationSetV2
    from .bandwidth_allocation_v2 import BandwidthAllocationV2
    from .bandwidth_allocation_v2ipsec_termination_service_item import BandwidthAllocationV2IpsecTerminationServiceItem
    from .ecmp_load_balancing import EcmpLoadBalancing
    from .ecmp_load_balancing_ecmp_load_balancing_enabled import EcmpLoadBalancingEcmpLoadBalancingEnabled
    from .ecmp_load_balancing_ecmp_tunnels_item import EcmpLoadBalancingEcmpTunnelsItem
    from .ecmp_load_balancing_ecmp_tunnels_item_bgp import EcmpLoadBalancingEcmpTunnelsItemBgp
    from .ecmp_load_balancing_ecmp_tunnels_item_bgp_peering_type import EcmpLoadBalancingEcmpTunnelsItemBgpPeeringType
    from .error_detail_cause_info import ErrorDetailCauseInfo
    from .error_detail_cause_infos import ErrorDetailCauseInfos
    from .generic_error import GenericError
    from .ike import Ike
    from .ike_advanced import IkeAdvanced
    from .ike_advanced_fragmentation import IkeAdvancedFragmentation
    from .ike_advanced_nat_traversal import IkeAdvancedNatTraversal
    from .ike_authentication import IkeAuthentication
    from .ike_crypto import IkeCrypto
    from .ike_crypto_profiles import IkeCryptoProfiles
    from .ike_crypto_profiles_dh_group_item import IkeCryptoProfilesDhGroupItem
    from .ike_crypto_profiles_encryption_item import IkeCryptoProfilesEncryptionItem
    from .ike_crypto_profiles_hash_item import IkeCryptoProfilesHashItem
    from .ike_crypto_profiles_lifetime import IkeCryptoProfilesLifetime
    from .ike_crypto_profiles_lifetime_days import IkeCryptoProfilesLifetimeDays
    from .ike_crypto_profiles_lifetime_hours import IkeCryptoProfilesLifetimeHours
    from .ike_crypto_profiles_lifetime_minutes import IkeCryptoProfilesLifetimeMinutes
    from .ike_crypto_profiles_lifetime_seconds import IkeCryptoProfilesLifetimeSeconds
    from .ike_crypto_profiles_response import IkeCryptoProfilesResponse
    from .ike_crypto_profiles_set import IkeCryptoProfilesSet
    from .ike_gateways_config import IkeGatewaysConfig
    from .ike_gateways_config_authentication import IkeGatewaysConfigAuthentication
    from .ike_gateways_config_authentication_allow_id_payload_mismatch import (
        IkeGatewaysConfigAuthenticationAllowIdPayloadMismatch,
    )
    from .ike_gateways_config_authentication_allow_id_payload_mismatch_local_certificate import (
        IkeGatewaysConfigAuthenticationAllowIdPayloadMismatchLocalCertificate,
    )
    from .ike_gateways_config_authentication_pre_shared_key import IkeGatewaysConfigAuthenticationPreSharedKey
    from .ike_gateways_config_authentication_pre_shared_key_pre_shared_key import (
        IkeGatewaysConfigAuthenticationPreSharedKeyPreSharedKey,
    )
    from .ike_gateways_config_local_id import IkeGatewaysConfigLocalId
    from .ike_gateways_config_peer_address import IkeGatewaysConfigPeerAddress
    from .ike_gateways_config_peer_address_dynamic import IkeGatewaysConfigPeerAddressDynamic
    from .ike_gateways_config_peer_address_fqdn import IkeGatewaysConfigPeerAddressFqdn
    from .ike_gateways_config_peer_address_ip import IkeGatewaysConfigPeerAddressIp
    from .ike_gateways_config_peer_id import IkeGatewaysConfigPeerId
    from .ike_gateways_config_peer_id_type import IkeGatewaysConfigPeerIdType
    from .ike_gateways_config_protocol import IkeGatewaysConfigProtocol
    from .ike_gateways_config_protocol_common import IkeGatewaysConfigProtocolCommon
    from .ike_gateways_config_protocol_common_fragmentation import IkeGatewaysConfigProtocolCommonFragmentation
    from .ike_gateways_config_protocol_common_nat_traversal import IkeGatewaysConfigProtocolCommonNatTraversal
    from .ike_gateways_config_protocol_ikev1 import IkeGatewaysConfigProtocolIkev1
    from .ike_gateways_config_protocol_ikev1dpd import IkeGatewaysConfigProtocolIkev1Dpd
    from .ike_gateways_config_protocol_ikev2 import IkeGatewaysConfigProtocolIkev2
    from .ike_gateways_config_protocol_ikev2dpd import IkeGatewaysConfigProtocolIkev2Dpd
    from .ike_gateways_config_protocol_version import IkeGatewaysConfigProtocolVersion
    from .ike_local_id import IkeLocalId
    from .ike_peer_address import IkePeerAddress
    from .ike_peer_address_dynamic import IkePeerAddressDynamic
    from .ike_peer_address_fqdn import IkePeerAddressFqdn
    from .ike_peer_address_ip import IkePeerAddressIp
    from .ike_peer_id import IkePeerId
    from .ike_peer_id_type import IkePeerIdType
    from .ike_version import IkeVersion
    from .ipsec_crypto import IpsecCrypto
    from .ipsec_crypto_profiles import IpsecCryptoProfiles
    from .ipsec_crypto_profiles_ah import IpsecCryptoProfilesAh
    from .ipsec_crypto_profiles_ah_authentication_item import IpsecCryptoProfilesAhAuthenticationItem
    from .ipsec_crypto_profiles_dh_group import IpsecCryptoProfilesDhGroup
    from .ipsec_crypto_profiles_esp import IpsecCryptoProfilesEsp
    from .ipsec_crypto_profiles_esp_encryption_item import IpsecCryptoProfilesEspEncryptionItem
    from .ipsec_crypto_profiles_response import IpsecCryptoProfilesResponse
    from .ipsec_crypto_profiles_set import IpsecCryptoProfilesSet
    from .ipsec_tunnel import IpsecTunnel
    from .ipsec_tunnel_crypto import IpsecTunnelCrypto
    from .ipsec_tunnel_tunnel_monitor import IpsecTunnelTunnelMonitor
    from .lifesize import Lifesize
    from .lifesize_gb import LifesizeGb
    from .lifesize_kb import LifesizeKb
    from .lifesize_mb import LifesizeMb
    from .lifesize_tb import LifesizeTb
    from .lifetime import Lifetime
    from .lifetime_days import LifetimeDays
    from .lifetime_hours import LifetimeHours
    from .lifetime_minutes import LifetimeMinutes
    from .lifetime_seconds import LifetimeSeconds
    from .location import Location
    from .location_information_response import LocationInformationResponse
    from .location_information_set import LocationInformationSet
    from .location_region_info import LocationRegionInfo
    from .location_region_info_set import LocationRegionInfoSet
    from .public_ip import PublicIp
    from .region_cordinates import RegionCordinates
    from .remote_networks_configuration import RemoteNetworksConfiguration
    from .remote_networks_configuration_ecmp_load_balancing import RemoteNetworksConfigurationEcmpLoadBalancing
    from .remote_networks_configuration_ecmp_tunnels_item import RemoteNetworksConfigurationEcmpTunnelsItem
    from .remote_networks_configuration_ecmp_tunnels_item_protocol import (
        RemoteNetworksConfigurationEcmpTunnelsItemProtocol,
    )
    from .remote_networks_configuration_inbound_access import RemoteNetworksConfigurationInboundAccess
    from .remote_networks_configuration_inbound_access_applications_item import (
        RemoteNetworksConfigurationInboundAccessApplicationsItem,
    )
    from .remote_networks_configuration_inbound_access_applications_item_protocol import (
        RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol,
    )
    from .remote_networks_configuration_protocol import RemoteNetworksConfigurationProtocol
    from .remote_networks_configuration_protocol_bgp_peer import RemoteNetworksConfigurationProtocolBgpPeer
    from .remote_networks_ipsec_tunnel import RemoteNetworksIpsecTunnel
    from .remote_networks_ipsec_tunnel_bgp import RemoteNetworksIpsecTunnelBgp
    from .remote_networks_ipsec_tunnel_bgp_bgp_peer import RemoteNetworksIpsecTunnelBgpBgpPeer
    from .remote_networks_ipsec_tunnel_bgp_peering_type import RemoteNetworksIpsecTunnelBgpPeeringType
    from .remote_networks_ipsec_tunnel_response import RemoteNetworksIpsecTunnelResponse
    from .remote_networks_ipsec_tunnel_response_set import RemoteNetworksIpsecTunnelResponseSet
    from .remote_networks_ipsec_tunnel_set import RemoteNetworksIpsecTunnelSet
    from .remote_networks_protocol_bgp import RemoteNetworksProtocolBgp
    from .remote_networks_protocol_bgp_peering_type import RemoteNetworksProtocolBgpPeeringType
    from .remote_networks_read_result import RemoteNetworksReadResult
    from .remote_networks_response import RemoteNetworksResponse
    from .uuid_response import UuidResponse
_dynamic_imports: typing.Dict[str, str] = {
    "BandwidthAllocation": ".bandwidth_allocation",
    "BandwidthAllocationSet": ".bandwidth_allocation_set",
    "BandwidthAllocationSetV2": ".bandwidth_allocation_set_v2",
    "BandwidthAllocationV2": ".bandwidth_allocation_v2",
    "BandwidthAllocationV2IpsecTerminationServiceItem": ".bandwidth_allocation_v2ipsec_termination_service_item",
    "EcmpLoadBalancing": ".ecmp_load_balancing",
    "EcmpLoadBalancingEcmpLoadBalancingEnabled": ".ecmp_load_balancing_ecmp_load_balancing_enabled",
    "EcmpLoadBalancingEcmpTunnelsItem": ".ecmp_load_balancing_ecmp_tunnels_item",
    "EcmpLoadBalancingEcmpTunnelsItemBgp": ".ecmp_load_balancing_ecmp_tunnels_item_bgp",
    "EcmpLoadBalancingEcmpTunnelsItemBgpPeeringType": ".ecmp_load_balancing_ecmp_tunnels_item_bgp_peering_type",
    "ErrorDetailCauseInfo": ".error_detail_cause_info",
    "ErrorDetailCauseInfos": ".error_detail_cause_infos",
    "GenericError": ".generic_error",
    "Ike": ".ike",
    "IkeAdvanced": ".ike_advanced",
    "IkeAdvancedFragmentation": ".ike_advanced_fragmentation",
    "IkeAdvancedNatTraversal": ".ike_advanced_nat_traversal",
    "IkeAuthentication": ".ike_authentication",
    "IkeCrypto": ".ike_crypto",
    "IkeCryptoProfiles": ".ike_crypto_profiles",
    "IkeCryptoProfilesDhGroupItem": ".ike_crypto_profiles_dh_group_item",
    "IkeCryptoProfilesEncryptionItem": ".ike_crypto_profiles_encryption_item",
    "IkeCryptoProfilesHashItem": ".ike_crypto_profiles_hash_item",
    "IkeCryptoProfilesLifetime": ".ike_crypto_profiles_lifetime",
    "IkeCryptoProfilesLifetimeDays": ".ike_crypto_profiles_lifetime_days",
    "IkeCryptoProfilesLifetimeHours": ".ike_crypto_profiles_lifetime_hours",
    "IkeCryptoProfilesLifetimeMinutes": ".ike_crypto_profiles_lifetime_minutes",
    "IkeCryptoProfilesLifetimeSeconds": ".ike_crypto_profiles_lifetime_seconds",
    "IkeCryptoProfilesResponse": ".ike_crypto_profiles_response",
    "IkeCryptoProfilesSet": ".ike_crypto_profiles_set",
    "IkeGatewaysConfig": ".ike_gateways_config",
    "IkeGatewaysConfigAuthentication": ".ike_gateways_config_authentication",
    "IkeGatewaysConfigAuthenticationAllowIdPayloadMismatch": ".ike_gateways_config_authentication_allow_id_payload_mismatch",
    "IkeGatewaysConfigAuthenticationAllowIdPayloadMismatchLocalCertificate": ".ike_gateways_config_authentication_allow_id_payload_mismatch_local_certificate",
    "IkeGatewaysConfigAuthenticationPreSharedKey": ".ike_gateways_config_authentication_pre_shared_key",
    "IkeGatewaysConfigAuthenticationPreSharedKeyPreSharedKey": ".ike_gateways_config_authentication_pre_shared_key_pre_shared_key",
    "IkeGatewaysConfigLocalId": ".ike_gateways_config_local_id",
    "IkeGatewaysConfigPeerAddress": ".ike_gateways_config_peer_address",
    "IkeGatewaysConfigPeerAddressDynamic": ".ike_gateways_config_peer_address_dynamic",
    "IkeGatewaysConfigPeerAddressFqdn": ".ike_gateways_config_peer_address_fqdn",
    "IkeGatewaysConfigPeerAddressIp": ".ike_gateways_config_peer_address_ip",
    "IkeGatewaysConfigPeerId": ".ike_gateways_config_peer_id",
    "IkeGatewaysConfigPeerIdType": ".ike_gateways_config_peer_id_type",
    "IkeGatewaysConfigProtocol": ".ike_gateways_config_protocol",
    "IkeGatewaysConfigProtocolCommon": ".ike_gateways_config_protocol_common",
    "IkeGatewaysConfigProtocolCommonFragmentation": ".ike_gateways_config_protocol_common_fragmentation",
    "IkeGatewaysConfigProtocolCommonNatTraversal": ".ike_gateways_config_protocol_common_nat_traversal",
    "IkeGatewaysConfigProtocolIkev1": ".ike_gateways_config_protocol_ikev1",
    "IkeGatewaysConfigProtocolIkev1Dpd": ".ike_gateways_config_protocol_ikev1dpd",
    "IkeGatewaysConfigProtocolIkev2": ".ike_gateways_config_protocol_ikev2",
    "IkeGatewaysConfigProtocolIkev2Dpd": ".ike_gateways_config_protocol_ikev2dpd",
    "IkeGatewaysConfigProtocolVersion": ".ike_gateways_config_protocol_version",
    "IkeLocalId": ".ike_local_id",
    "IkePeerAddress": ".ike_peer_address",
    "IkePeerAddressDynamic": ".ike_peer_address_dynamic",
    "IkePeerAddressFqdn": ".ike_peer_address_fqdn",
    "IkePeerAddressIp": ".ike_peer_address_ip",
    "IkePeerId": ".ike_peer_id",
    "IkePeerIdType": ".ike_peer_id_type",
    "IkeVersion": ".ike_version",
    "IpsecCrypto": ".ipsec_crypto",
    "IpsecCryptoProfiles": ".ipsec_crypto_profiles",
    "IpsecCryptoProfilesAh": ".ipsec_crypto_profiles_ah",
    "IpsecCryptoProfilesAhAuthenticationItem": ".ipsec_crypto_profiles_ah_authentication_item",
    "IpsecCryptoProfilesDhGroup": ".ipsec_crypto_profiles_dh_group",
    "IpsecCryptoProfilesEsp": ".ipsec_crypto_profiles_esp",
    "IpsecCryptoProfilesEspEncryptionItem": ".ipsec_crypto_profiles_esp_encryption_item",
    "IpsecCryptoProfilesResponse": ".ipsec_crypto_profiles_response",
    "IpsecCryptoProfilesSet": ".ipsec_crypto_profiles_set",
    "IpsecTunnel": ".ipsec_tunnel",
    "IpsecTunnelCrypto": ".ipsec_tunnel_crypto",
    "IpsecTunnelTunnelMonitor": ".ipsec_tunnel_tunnel_monitor",
    "Lifesize": ".lifesize",
    "LifesizeGb": ".lifesize_gb",
    "LifesizeKb": ".lifesize_kb",
    "LifesizeMb": ".lifesize_mb",
    "LifesizeTb": ".lifesize_tb",
    "Lifetime": ".lifetime",
    "LifetimeDays": ".lifetime_days",
    "LifetimeHours": ".lifetime_hours",
    "LifetimeMinutes": ".lifetime_minutes",
    "LifetimeSeconds": ".lifetime_seconds",
    "Location": ".location",
    "LocationInformationResponse": ".location_information_response",
    "LocationInformationSet": ".location_information_set",
    "LocationRegionInfo": ".location_region_info",
    "LocationRegionInfoSet": ".location_region_info_set",
    "PublicIp": ".public_ip",
    "RegionCordinates": ".region_cordinates",
    "RemoteNetworksConfiguration": ".remote_networks_configuration",
    "RemoteNetworksConfigurationEcmpLoadBalancing": ".remote_networks_configuration_ecmp_load_balancing",
    "RemoteNetworksConfigurationEcmpTunnelsItem": ".remote_networks_configuration_ecmp_tunnels_item",
    "RemoteNetworksConfigurationEcmpTunnelsItemProtocol": ".remote_networks_configuration_ecmp_tunnels_item_protocol",
    "RemoteNetworksConfigurationInboundAccess": ".remote_networks_configuration_inbound_access",
    "RemoteNetworksConfigurationInboundAccessApplicationsItem": ".remote_networks_configuration_inbound_access_applications_item",
    "RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol": ".remote_networks_configuration_inbound_access_applications_item_protocol",
    "RemoteNetworksConfigurationProtocol": ".remote_networks_configuration_protocol",
    "RemoteNetworksConfigurationProtocolBgpPeer": ".remote_networks_configuration_protocol_bgp_peer",
    "RemoteNetworksIpsecTunnel": ".remote_networks_ipsec_tunnel",
    "RemoteNetworksIpsecTunnelBgp": ".remote_networks_ipsec_tunnel_bgp",
    "RemoteNetworksIpsecTunnelBgpBgpPeer": ".remote_networks_ipsec_tunnel_bgp_bgp_peer",
    "RemoteNetworksIpsecTunnelBgpPeeringType": ".remote_networks_ipsec_tunnel_bgp_peering_type",
    "RemoteNetworksIpsecTunnelResponse": ".remote_networks_ipsec_tunnel_response",
    "RemoteNetworksIpsecTunnelResponseSet": ".remote_networks_ipsec_tunnel_response_set",
    "RemoteNetworksIpsecTunnelSet": ".remote_networks_ipsec_tunnel_set",
    "RemoteNetworksProtocolBgp": ".remote_networks_protocol_bgp",
    "RemoteNetworksProtocolBgpPeeringType": ".remote_networks_protocol_bgp_peering_type",
    "RemoteNetworksReadResult": ".remote_networks_read_result",
    "RemoteNetworksResponse": ".remote_networks_response",
    "UuidResponse": ".uuid_response",
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
    "BandwidthAllocation",
    "BandwidthAllocationSet",
    "BandwidthAllocationSetV2",
    "BandwidthAllocationV2",
    "BandwidthAllocationV2IpsecTerminationServiceItem",
    "EcmpLoadBalancing",
    "EcmpLoadBalancingEcmpLoadBalancingEnabled",
    "EcmpLoadBalancingEcmpTunnelsItem",
    "EcmpLoadBalancingEcmpTunnelsItemBgp",
    "EcmpLoadBalancingEcmpTunnelsItemBgpPeeringType",
    "ErrorDetailCauseInfo",
    "ErrorDetailCauseInfos",
    "GenericError",
    "Ike",
    "IkeAdvanced",
    "IkeAdvancedFragmentation",
    "IkeAdvancedNatTraversal",
    "IkeAuthentication",
    "IkeCrypto",
    "IkeCryptoProfiles",
    "IkeCryptoProfilesDhGroupItem",
    "IkeCryptoProfilesEncryptionItem",
    "IkeCryptoProfilesHashItem",
    "IkeCryptoProfilesLifetime",
    "IkeCryptoProfilesLifetimeDays",
    "IkeCryptoProfilesLifetimeHours",
    "IkeCryptoProfilesLifetimeMinutes",
    "IkeCryptoProfilesLifetimeSeconds",
    "IkeCryptoProfilesResponse",
    "IkeCryptoProfilesSet",
    "IkeGatewaysConfig",
    "IkeGatewaysConfigAuthentication",
    "IkeGatewaysConfigAuthenticationAllowIdPayloadMismatch",
    "IkeGatewaysConfigAuthenticationAllowIdPayloadMismatchLocalCertificate",
    "IkeGatewaysConfigAuthenticationPreSharedKey",
    "IkeGatewaysConfigAuthenticationPreSharedKeyPreSharedKey",
    "IkeGatewaysConfigLocalId",
    "IkeGatewaysConfigPeerAddress",
    "IkeGatewaysConfigPeerAddressDynamic",
    "IkeGatewaysConfigPeerAddressFqdn",
    "IkeGatewaysConfigPeerAddressIp",
    "IkeGatewaysConfigPeerId",
    "IkeGatewaysConfigPeerIdType",
    "IkeGatewaysConfigProtocol",
    "IkeGatewaysConfigProtocolCommon",
    "IkeGatewaysConfigProtocolCommonFragmentation",
    "IkeGatewaysConfigProtocolCommonNatTraversal",
    "IkeGatewaysConfigProtocolIkev1",
    "IkeGatewaysConfigProtocolIkev1Dpd",
    "IkeGatewaysConfigProtocolIkev2",
    "IkeGatewaysConfigProtocolIkev2Dpd",
    "IkeGatewaysConfigProtocolVersion",
    "IkeLocalId",
    "IkePeerAddress",
    "IkePeerAddressDynamic",
    "IkePeerAddressFqdn",
    "IkePeerAddressIp",
    "IkePeerId",
    "IkePeerIdType",
    "IkeVersion",
    "IpsecCrypto",
    "IpsecCryptoProfiles",
    "IpsecCryptoProfilesAh",
    "IpsecCryptoProfilesAhAuthenticationItem",
    "IpsecCryptoProfilesDhGroup",
    "IpsecCryptoProfilesEsp",
    "IpsecCryptoProfilesEspEncryptionItem",
    "IpsecCryptoProfilesResponse",
    "IpsecCryptoProfilesSet",
    "IpsecTunnel",
    "IpsecTunnelCrypto",
    "IpsecTunnelTunnelMonitor",
    "Lifesize",
    "LifesizeGb",
    "LifesizeKb",
    "LifesizeMb",
    "LifesizeTb",
    "Lifetime",
    "LifetimeDays",
    "LifetimeHours",
    "LifetimeMinutes",
    "LifetimeSeconds",
    "Location",
    "LocationInformationResponse",
    "LocationInformationSet",
    "LocationRegionInfo",
    "LocationRegionInfoSet",
    "PublicIp",
    "RegionCordinates",
    "RemoteNetworksConfiguration",
    "RemoteNetworksConfigurationEcmpLoadBalancing",
    "RemoteNetworksConfigurationEcmpTunnelsItem",
    "RemoteNetworksConfigurationEcmpTunnelsItemProtocol",
    "RemoteNetworksConfigurationInboundAccess",
    "RemoteNetworksConfigurationInboundAccessApplicationsItem",
    "RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol",
    "RemoteNetworksConfigurationProtocol",
    "RemoteNetworksConfigurationProtocolBgpPeer",
    "RemoteNetworksIpsecTunnel",
    "RemoteNetworksIpsecTunnelBgp",
    "RemoteNetworksIpsecTunnelBgpBgpPeer",
    "RemoteNetworksIpsecTunnelBgpPeeringType",
    "RemoteNetworksIpsecTunnelResponse",
    "RemoteNetworksIpsecTunnelResponseSet",
    "RemoteNetworksIpsecTunnelSet",
    "RemoteNetworksProtocolBgp",
    "RemoteNetworksProtocolBgpPeeringType",
    "RemoteNetworksReadResult",
    "RemoteNetworksResponse",
    "UuidResponse",
]
