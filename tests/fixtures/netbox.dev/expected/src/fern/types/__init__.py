



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .aggregate import Aggregate
    from .aggregate_family import AggregateFamily
    from .aggregate_family_label import AggregateFamilyLabel
    from .asn import Asn
    from .available_ip import AvailableIp
    from .available_prefix import AvailablePrefix
    from .available_vlan import AvailableVlan
    from .cable import Cable
    from .cable_length_unit import CableLengthUnit
    from .cable_length_unit_label import CableLengthUnitLabel
    from .cable_length_unit_value import CableLengthUnitValue
    from .cable_status import CableStatus
    from .cable_status_label import CableStatusLabel
    from .cable_status_value import CableStatusValue
    from .cable_termination import CableTermination
    from .cable_termination_cable_end import CableTerminationCableEnd
    from .cable_type import CableType
    from .circuit import Circuit
    from .circuit_circuit_termination import CircuitCircuitTermination
    from .circuit_status import CircuitStatus
    from .circuit_status_label import CircuitStatusLabel
    from .circuit_status_value import CircuitStatusValue
    from .circuit_termination import CircuitTermination
    from .circuit_termination_term_side import CircuitTerminationTermSide
    from .circuit_type import CircuitType
    from .cluster import Cluster
    from .cluster_group import ClusterGroup
    from .cluster_status import ClusterStatus
    from .cluster_status_label import ClusterStatusLabel
    from .cluster_status_value import ClusterStatusValue
    from .cluster_type import ClusterType
    from .component_nested_module import ComponentNestedModule
    from .config_context import ConfigContext
    from .console_port import ConsolePort
    from .console_port_speed import ConsolePortSpeed
    from .console_port_speed_label import ConsolePortSpeedLabel
    from .console_port_template import ConsolePortTemplate
    from .console_port_template_type import ConsolePortTemplateType
    from .console_port_template_type_label import ConsolePortTemplateTypeLabel
    from .console_port_template_type_value import ConsolePortTemplateTypeValue
    from .console_port_type import ConsolePortType
    from .console_port_type_label import ConsolePortTypeLabel
    from .console_port_type_value import ConsolePortTypeValue
    from .console_server_port import ConsoleServerPort
    from .console_server_port_speed import ConsoleServerPortSpeed
    from .console_server_port_speed_label import ConsoleServerPortSpeedLabel
    from .console_server_port_template import ConsoleServerPortTemplate
    from .console_server_port_template_type import ConsoleServerPortTemplateType
    from .console_server_port_template_type_label import ConsoleServerPortTemplateTypeLabel
    from .console_server_port_template_type_value import ConsoleServerPortTemplateTypeValue
    from .console_server_port_type import ConsoleServerPortType
    from .console_server_port_type_label import ConsoleServerPortTypeLabel
    from .console_server_port_type_value import ConsoleServerPortTypeValue
    from .contact import Contact
    from .contact_assignment import ContactAssignment
    from .contact_assignment_priority import ContactAssignmentPriority
    from .contact_assignment_priority_label import ContactAssignmentPriorityLabel
    from .contact_assignment_priority_value import ContactAssignmentPriorityValue
    from .contact_group import ContactGroup
    from .contact_role import ContactRole
    from .content_type import ContentType
    from .custom_field import CustomField
    from .custom_field_filter_logic import CustomFieldFilterLogic
    from .custom_field_filter_logic_label import CustomFieldFilterLogicLabel
    from .custom_field_filter_logic_value import CustomFieldFilterLogicValue
    from .custom_field_type import CustomFieldType
    from .custom_field_type_label import CustomFieldTypeLabel
    from .custom_field_type_value import CustomFieldTypeValue
    from .custom_field_ui_visibility import CustomFieldUiVisibility
    from .custom_field_ui_visibility_label import CustomFieldUiVisibilityLabel
    from .custom_field_ui_visibility_value import CustomFieldUiVisibilityValue
    from .custom_link import CustomLink
    from .custom_link_button_class import CustomLinkButtonClass
    from .device import Device
    from .device_airflow import DeviceAirflow
    from .device_airflow_label import DeviceAirflowLabel
    from .device_airflow_value import DeviceAirflowValue
    from .device_bay import DeviceBay
    from .device_bay_template import DeviceBayTemplate
    from .device_face import DeviceFace
    from .device_face_label import DeviceFaceLabel
    from .device_face_value import DeviceFaceValue
    from .device_napalm import DeviceNapalm
    from .device_role import DeviceRole
    from .device_status import DeviceStatus
    from .device_status_label import DeviceStatusLabel
    from .device_status_value import DeviceStatusValue
    from .device_type import DeviceType
    from .device_type_airflow import DeviceTypeAirflow
    from .device_type_airflow_label import DeviceTypeAirflowLabel
    from .device_type_airflow_value import DeviceTypeAirflowValue
    from .device_type_subdevice_role import DeviceTypeSubdeviceRole
    from .device_type_subdevice_role_label import DeviceTypeSubdeviceRoleLabel
    from .device_type_subdevice_role_value import DeviceTypeSubdeviceRoleValue
    from .device_type_weight_unit import DeviceTypeWeightUnit
    from .device_type_weight_unit_label import DeviceTypeWeightUnitLabel
    from .device_type_weight_unit_value import DeviceTypeWeightUnitValue
    from .device_with_config_context import DeviceWithConfigContext
    from .device_with_config_context_airflow import DeviceWithConfigContextAirflow
    from .device_with_config_context_airflow_label import DeviceWithConfigContextAirflowLabel
    from .device_with_config_context_airflow_value import DeviceWithConfigContextAirflowValue
    from .device_with_config_context_face import DeviceWithConfigContextFace
    from .device_with_config_context_face_label import DeviceWithConfigContextFaceLabel
    from .device_with_config_context_face_value import DeviceWithConfigContextFaceValue
    from .device_with_config_context_status import DeviceWithConfigContextStatus
    from .device_with_config_context_status_label import DeviceWithConfigContextStatusLabel
    from .device_with_config_context_status_value import DeviceWithConfigContextStatusValue
    from .export_template import ExportTemplate
    from .fhrp_group import FhrpGroup
    from .fhrp_group_assignment import FhrpGroupAssignment
    from .fhrp_group_auth_type import FhrpGroupAuthType
    from .fhrp_group_protocol import FhrpGroupProtocol
    from .front_port import FrontPort
    from .front_port_rear_port import FrontPortRearPort
    from .front_port_template import FrontPortTemplate
    from .front_port_template_type import FrontPortTemplateType
    from .front_port_template_type_label import FrontPortTemplateTypeLabel
    from .front_port_template_type_value import FrontPortTemplateTypeValue
    from .front_port_type import FrontPortType
    from .front_port_type_label import FrontPortTypeLabel
    from .front_port_type_value import FrontPortTypeValue
    from .generic_object import GenericObject
    from .group import Group
    from .image_attachment import ImageAttachment
    from .interface import Interface
    from .interface_duplex import InterfaceDuplex
    from .interface_duplex_label import InterfaceDuplexLabel
    from .interface_duplex_value import InterfaceDuplexValue
    from .interface_mode import InterfaceMode
    from .interface_mode_label import InterfaceModeLabel
    from .interface_mode_value import InterfaceModeValue
    from .interface_poe_mode import InterfacePoeMode
    from .interface_poe_mode_label import InterfacePoeModeLabel
    from .interface_poe_mode_value import InterfacePoeModeValue
    from .interface_poe_type import InterfacePoeType
    from .interface_poe_type_label import InterfacePoeTypeLabel
    from .interface_poe_type_value import InterfacePoeTypeValue
    from .interface_rf_channel import InterfaceRfChannel
    from .interface_rf_channel_label import InterfaceRfChannelLabel
    from .interface_rf_channel_value import InterfaceRfChannelValue
    from .interface_rf_role import InterfaceRfRole
    from .interface_rf_role_label import InterfaceRfRoleLabel
    from .interface_rf_role_value import InterfaceRfRoleValue
    from .interface_template import InterfaceTemplate
    from .interface_template_poe_mode import InterfaceTemplatePoeMode
    from .interface_template_poe_mode_label import InterfaceTemplatePoeModeLabel
    from .interface_template_poe_mode_value import InterfaceTemplatePoeModeValue
    from .interface_template_poe_type import InterfaceTemplatePoeType
    from .interface_template_poe_type_label import InterfaceTemplatePoeTypeLabel
    from .interface_template_poe_type_value import InterfaceTemplatePoeTypeValue
    from .interface_template_type import InterfaceTemplateType
    from .interface_template_type_label import InterfaceTemplateTypeLabel
    from .interface_template_type_value import InterfaceTemplateTypeValue
    from .interface_type import InterfaceType
    from .interface_type_label import InterfaceTypeLabel
    from .interface_type_value import InterfaceTypeValue
    from .inventory_item import InventoryItem
    from .inventory_item_role import InventoryItemRole
    from .inventory_item_template import InventoryItemTemplate
    from .ip_address import IpAddress
    from .ip_address_family import IpAddressFamily
    from .ip_address_family_label import IpAddressFamilyLabel
    from .ip_address_role import IpAddressRole
    from .ip_address_role_label import IpAddressRoleLabel
    from .ip_address_role_value import IpAddressRoleValue
    from .ip_address_status import IpAddressStatus
    from .ip_address_status_label import IpAddressStatusLabel
    from .ip_address_status_value import IpAddressStatusValue
    from .ip_network import IpNetwork
    from .ip_range import IpRange
    from .ip_range_family import IpRangeFamily
    from .ip_range_family_label import IpRangeFamilyLabel
    from .ip_range_status import IpRangeStatus
    from .ip_range_status_label import IpRangeStatusLabel
    from .ip_range_status_value import IpRangeStatusValue
    from .job_result import JobResult
    from .job_result_status import JobResultStatus
    from .job_result_status_label import JobResultStatusLabel
    from .job_result_status_value import JobResultStatusValue
    from .journal_entry import JournalEntry
    from .journal_entry_kind import JournalEntryKind
    from .journal_entry_kind_label import JournalEntryKindLabel
    from .journal_entry_kind_value import JournalEntryKindValue
    from .l2vpn import L2Vpn
    from .l2vpn_termination import L2VpnTermination
    from .l2vpn_type import L2VpnType
    from .l2vpn_type_label import L2VpnTypeLabel
    from .l2vpn_type_value import L2VpnTypeValue
    from .location import Location
    from .location_status import LocationStatus
    from .location_status_label import LocationStatusLabel
    from .location_status_value import LocationStatusValue
    from .manufacturer import Manufacturer
    from .module import Module
    from .module_bay import ModuleBay
    from .module_bay_nested_module import ModuleBayNestedModule
    from .module_bay_template import ModuleBayTemplate
    from .module_nested_module_bay import ModuleNestedModuleBay
    from .module_status import ModuleStatus
    from .module_status_label import ModuleStatusLabel
    from .module_status_value import ModuleStatusValue
    from .module_type import ModuleType
    from .module_type_weight_unit import ModuleTypeWeightUnit
    from .module_type_weight_unit_label import ModuleTypeWeightUnitLabel
    from .module_type_weight_unit_value import ModuleTypeWeightUnitValue
    from .nested_asn import NestedAsn
    from .nested_cable import NestedCable
    from .nested_circuit import NestedCircuit
    from .nested_circuit_type import NestedCircuitType
    from .nested_cluster import NestedCluster
    from .nested_cluster_group import NestedClusterGroup
    from .nested_cluster_type import NestedClusterType
    from .nested_contact import NestedContact
    from .nested_contact_group import NestedContactGroup
    from .nested_contact_role import NestedContactRole
    from .nested_device import NestedDevice
    from .nested_device_role import NestedDeviceRole
    from .nested_device_type import NestedDeviceType
    from .nested_fhrp_group import NestedFhrpGroup
    from .nested_fhrp_group_protocol import NestedFhrpGroupProtocol
    from .nested_group import NestedGroup
    from .nested_interface import NestedInterface
    from .nested_inventory_item_role import NestedInventoryItemRole
    from .nested_ip_address import NestedIpAddress
    from .nested_l2vpn import NestedL2Vpn
    from .nested_l2vpn_termination import NestedL2VpnTermination
    from .nested_l2vpn_type import NestedL2VpnType
    from .nested_location import NestedLocation
    from .nested_manufacturer import NestedManufacturer
    from .nested_module import NestedModule
    from .nested_module_bay import NestedModuleBay
    from .nested_module_type import NestedModuleType
    from .nested_platform import NestedPlatform
    from .nested_power_panel import NestedPowerPanel
    from .nested_power_port import NestedPowerPort
    from .nested_power_port_template import NestedPowerPortTemplate
    from .nested_provider import NestedProvider
    from .nested_provider_network import NestedProviderNetwork
    from .nested_rack import NestedRack
    from .nested_rack_role import NestedRackRole
    from .nested_rear_port_template import NestedRearPortTemplate
    from .nested_region import NestedRegion
    from .nested_rir import NestedRir
    from .nested_role import NestedRole
    from .nested_route_target import NestedRouteTarget
    from .nested_site import NestedSite
    from .nested_site_group import NestedSiteGroup
    from .nested_tag import NestedTag
    from .nested_tenant import NestedTenant
    from .nested_tenant_group import NestedTenantGroup
    from .nested_user import NestedUser
    from .nested_virtual_chassis import NestedVirtualChassis
    from .nested_virtual_device_context import NestedVirtualDeviceContext
    from .nested_virtual_machine import NestedVirtualMachine
    from .nested_vlan import NestedVlan
    from .nested_vlan_group import NestedVlanGroup
    from .nested_vm_interface import NestedVmInterface
    from .nested_vrf import NestedVrf
    from .nested_wireless_lan import NestedWirelessLan
    from .nested_wireless_lan_group import NestedWirelessLanGroup
    from .nested_wireless_link import NestedWirelessLink
    from .object_change import ObjectChange
    from .object_change_action import ObjectChangeAction
    from .object_change_action_label import ObjectChangeActionLabel
    from .object_change_action_value import ObjectChangeActionValue
    from .object_permission import ObjectPermission
    from .platform import Platform
    from .power_feed import PowerFeed
    from .power_feed_phase import PowerFeedPhase
    from .power_feed_phase_label import PowerFeedPhaseLabel
    from .power_feed_phase_value import PowerFeedPhaseValue
    from .power_feed_status import PowerFeedStatus
    from .power_feed_status_label import PowerFeedStatusLabel
    from .power_feed_status_value import PowerFeedStatusValue
    from .power_feed_supply import PowerFeedSupply
    from .power_feed_supply_label import PowerFeedSupplyLabel
    from .power_feed_supply_value import PowerFeedSupplyValue
    from .power_feed_type import PowerFeedType
    from .power_feed_type_label import PowerFeedTypeLabel
    from .power_feed_type_value import PowerFeedTypeValue
    from .power_outlet import PowerOutlet
    from .power_outlet_feed_leg import PowerOutletFeedLeg
    from .power_outlet_feed_leg_label import PowerOutletFeedLegLabel
    from .power_outlet_feed_leg_value import PowerOutletFeedLegValue
    from .power_outlet_template import PowerOutletTemplate
    from .power_outlet_template_feed_leg import PowerOutletTemplateFeedLeg
    from .power_outlet_template_feed_leg_label import PowerOutletTemplateFeedLegLabel
    from .power_outlet_template_feed_leg_value import PowerOutletTemplateFeedLegValue
    from .power_outlet_template_type import PowerOutletTemplateType
    from .power_outlet_template_type_label import PowerOutletTemplateTypeLabel
    from .power_outlet_template_type_value import PowerOutletTemplateTypeValue
    from .power_outlet_type import PowerOutletType
    from .power_outlet_type_label import PowerOutletTypeLabel
    from .power_outlet_type_value import PowerOutletTypeValue
    from .power_panel import PowerPanel
    from .power_port import PowerPort
    from .power_port_template import PowerPortTemplate
    from .power_port_template_type import PowerPortTemplateType
    from .power_port_template_type_label import PowerPortTemplateTypeLabel
    from .power_port_template_type_value import PowerPortTemplateTypeValue
    from .power_port_type import PowerPortType
    from .power_port_type_label import PowerPortTypeLabel
    from .power_port_type_value import PowerPortTypeValue
    from .prefix import Prefix
    from .prefix_family import PrefixFamily
    from .prefix_family_label import PrefixFamilyLabel
    from .prefix_status import PrefixStatus
    from .prefix_status_label import PrefixStatusLabel
    from .prefix_status_value import PrefixStatusValue
    from .provider import Provider
    from .provider_network import ProviderNetwork
    from .rack import Rack
    from .rack_outer_unit import RackOuterUnit
    from .rack_outer_unit_label import RackOuterUnitLabel
    from .rack_outer_unit_value import RackOuterUnitValue
    from .rack_reservation import RackReservation
    from .rack_role import RackRole
    from .rack_status import RackStatus
    from .rack_status_label import RackStatusLabel
    from .rack_status_value import RackStatusValue
    from .rack_type import RackType
    from .rack_type_label import RackTypeLabel
    from .rack_type_value import RackTypeValue
    from .rack_unit import RackUnit
    from .rack_unit_face import RackUnitFace
    from .rack_unit_face_label import RackUnitFaceLabel
    from .rack_unit_face_value import RackUnitFaceValue
    from .rack_weight_unit import RackWeightUnit
    from .rack_weight_unit_label import RackWeightUnitLabel
    from .rack_weight_unit_value import RackWeightUnitValue
    from .rack_width import RackWidth
    from .rack_width_label import RackWidthLabel
    from .rear_port import RearPort
    from .rear_port_template import RearPortTemplate
    from .rear_port_template_type import RearPortTemplateType
    from .rear_port_template_type_label import RearPortTemplateTypeLabel
    from .rear_port_template_type_value import RearPortTemplateTypeValue
    from .rear_port_type import RearPortType
    from .rear_port_type_label import RearPortTypeLabel
    from .rear_port_type_value import RearPortTypeValue
    from .region import Region
    from .rir import Rir
    from .role import Role
    from .route_target import RouteTarget
    from .saved_filter import SavedFilter
    from .service import Service
    from .service_protocol import ServiceProtocol
    from .service_protocol_label import ServiceProtocolLabel
    from .service_protocol_value import ServiceProtocolValue
    from .service_template import ServiceTemplate
    from .service_template_protocol import ServiceTemplateProtocol
    from .service_template_protocol_label import ServiceTemplateProtocolLabel
    from .service_template_protocol_value import ServiceTemplateProtocolValue
    from .site import Site
    from .site_group import SiteGroup
    from .site_status import SiteStatus
    from .site_status_label import SiteStatusLabel
    from .site_status_value import SiteStatusValue
    from .tag import Tag
    from .tenant import Tenant
    from .tenant_group import TenantGroup
    from .token import Token
    from .user import User
    from .virtual_chassis import VirtualChassis
    from .virtual_device_context import VirtualDeviceContext
    from .virtual_device_context_status import VirtualDeviceContextStatus
    from .virtual_machine_with_config_context import VirtualMachineWithConfigContext
    from .virtual_machine_with_config_context_status import VirtualMachineWithConfigContextStatus
    from .virtual_machine_with_config_context_status_label import VirtualMachineWithConfigContextStatusLabel
    from .virtual_machine_with_config_context_status_value import VirtualMachineWithConfigContextStatusValue
    from .vlan import Vlan
    from .vlan_group import VlanGroup
    from .vlan_status import VlanStatus
    from .vlan_status_label import VlanStatusLabel
    from .vlan_status_value import VlanStatusValue
    from .vm_interface import VmInterface
    from .vm_interface_mode import VmInterfaceMode
    from .vm_interface_mode_label import VmInterfaceModeLabel
    from .vm_interface_mode_value import VmInterfaceModeValue
    from .vrf import Vrf
    from .webhook import Webhook
    from .webhook_http_method import WebhookHttpMethod
    from .wireless_lan import WirelessLan
    from .wireless_lan_auth_cipher import WirelessLanAuthCipher
    from .wireless_lan_auth_cipher_label import WirelessLanAuthCipherLabel
    from .wireless_lan_auth_cipher_value import WirelessLanAuthCipherValue
    from .wireless_lan_auth_type import WirelessLanAuthType
    from .wireless_lan_auth_type_label import WirelessLanAuthTypeLabel
    from .wireless_lan_auth_type_value import WirelessLanAuthTypeValue
    from .wireless_lan_group import WirelessLanGroup
    from .wireless_lan_status import WirelessLanStatus
    from .wireless_lan_status_label import WirelessLanStatusLabel
    from .wireless_lan_status_value import WirelessLanStatusValue
    from .wireless_link import WirelessLink
    from .wireless_link_auth_cipher import WirelessLinkAuthCipher
    from .wireless_link_auth_cipher_label import WirelessLinkAuthCipherLabel
    from .wireless_link_auth_cipher_value import WirelessLinkAuthCipherValue
    from .wireless_link_auth_type import WirelessLinkAuthType
    from .wireless_link_auth_type_label import WirelessLinkAuthTypeLabel
    from .wireless_link_auth_type_value import WirelessLinkAuthTypeValue
    from .wireless_link_status import WirelessLinkStatus
    from .wireless_link_status_label import WirelessLinkStatusLabel
    from .wireless_link_status_value import WirelessLinkStatusValue
    from .writable_aggregate import WritableAggregate
    from .writable_asn import WritableAsn
    from .writable_available_ip import WritableAvailableIp
    from .writable_cable import WritableCable
    from .writable_cable_length_unit import WritableCableLengthUnit
    from .writable_cable_status import WritableCableStatus
    from .writable_cable_type import WritableCableType
    from .writable_circuit import WritableCircuit
    from .writable_circuit_status import WritableCircuitStatus
    from .writable_circuit_termination import WritableCircuitTermination
    from .writable_circuit_termination_term_side import WritableCircuitTerminationTermSide
    from .writable_cluster import WritableCluster
    from .writable_cluster_status import WritableClusterStatus
    from .writable_config_context import WritableConfigContext
    from .writable_console_port import WritableConsolePort
    from .writable_console_port_template import WritableConsolePortTemplate
    from .writable_console_port_template_type import WritableConsolePortTemplateType
    from .writable_console_port_type import WritableConsolePortType
    from .writable_console_server_port import WritableConsoleServerPort
    from .writable_console_server_port_template import WritableConsoleServerPortTemplate
    from .writable_console_server_port_template_type import WritableConsoleServerPortTemplateType
    from .writable_console_server_port_type import WritableConsoleServerPortType
    from .writable_contact import WritableContact
    from .writable_contact_assignment import WritableContactAssignment
    from .writable_contact_assignment_priority import WritableContactAssignmentPriority
    from .writable_contact_group import WritableContactGroup
    from .writable_custom_field import WritableCustomField
    from .writable_custom_field_filter_logic import WritableCustomFieldFilterLogic
    from .writable_custom_field_type import WritableCustomFieldType
    from .writable_custom_field_ui_visibility import WritableCustomFieldUiVisibility
    from .writable_device_bay import WritableDeviceBay
    from .writable_device_bay_template import WritableDeviceBayTemplate
    from .writable_device_type import WritableDeviceType
    from .writable_device_type_airflow import WritableDeviceTypeAirflow
    from .writable_device_type_subdevice_role import WritableDeviceTypeSubdeviceRole
    from .writable_device_type_weight_unit import WritableDeviceTypeWeightUnit
    from .writable_device_with_config_context import WritableDeviceWithConfigContext
    from .writable_device_with_config_context_airflow import WritableDeviceWithConfigContextAirflow
    from .writable_device_with_config_context_face import WritableDeviceWithConfigContextFace
    from .writable_device_with_config_context_status import WritableDeviceWithConfigContextStatus
    from .writable_fhrp_group_assignment import WritableFhrpGroupAssignment
    from .writable_front_port import WritableFrontPort
    from .writable_front_port_template import WritableFrontPortTemplate
    from .writable_front_port_template_type import WritableFrontPortTemplateType
    from .writable_front_port_type import WritableFrontPortType
    from .writable_interface import WritableInterface
    from .writable_interface_duplex import WritableInterfaceDuplex
    from .writable_interface_mode import WritableInterfaceMode
    from .writable_interface_poe_mode import WritableInterfacePoeMode
    from .writable_interface_poe_type import WritableInterfacePoeType
    from .writable_interface_rf_channel import WritableInterfaceRfChannel
    from .writable_interface_rf_role import WritableInterfaceRfRole
    from .writable_interface_template import WritableInterfaceTemplate
    from .writable_interface_template_poe_mode import WritableInterfaceTemplatePoeMode
    from .writable_interface_template_poe_type import WritableInterfaceTemplatePoeType
    from .writable_interface_template_type import WritableInterfaceTemplateType
    from .writable_interface_type import WritableInterfaceType
    from .writable_inventory_item import WritableInventoryItem
    from .writable_inventory_item_template import WritableInventoryItemTemplate
    from .writable_ip_address import WritableIpAddress
    from .writable_ip_address_role import WritableIpAddressRole
    from .writable_ip_address_status import WritableIpAddressStatus
    from .writable_ip_range import WritableIpRange
    from .writable_ip_range_status import WritableIpRangeStatus
    from .writable_journal_entry import WritableJournalEntry
    from .writable_journal_entry_kind import WritableJournalEntryKind
    from .writable_l2vpn import WritableL2Vpn
    from .writable_l2vpn_termination import WritableL2VpnTermination
    from .writable_l2vpn_type import WritableL2VpnType
    from .writable_location import WritableLocation
    from .writable_location_status import WritableLocationStatus
    from .writable_module import WritableModule
    from .writable_module_bay import WritableModuleBay
    from .writable_module_bay_template import WritableModuleBayTemplate
    from .writable_module_status import WritableModuleStatus
    from .writable_module_type import WritableModuleType
    from .writable_module_type_weight_unit import WritableModuleTypeWeightUnit
    from .writable_object_permission import WritableObjectPermission
    from .writable_platform import WritablePlatform
    from .writable_power_feed import WritablePowerFeed
    from .writable_power_feed_phase import WritablePowerFeedPhase
    from .writable_power_feed_status import WritablePowerFeedStatus
    from .writable_power_feed_supply import WritablePowerFeedSupply
    from .writable_power_feed_type import WritablePowerFeedType
    from .writable_power_outlet import WritablePowerOutlet
    from .writable_power_outlet_feed_leg import WritablePowerOutletFeedLeg
    from .writable_power_outlet_template import WritablePowerOutletTemplate
    from .writable_power_outlet_template_feed_leg import WritablePowerOutletTemplateFeedLeg
    from .writable_power_outlet_template_type import WritablePowerOutletTemplateType
    from .writable_power_outlet_type import WritablePowerOutletType
    from .writable_power_panel import WritablePowerPanel
    from .writable_power_port import WritablePowerPort
    from .writable_power_port_template import WritablePowerPortTemplate
    from .writable_power_port_template_type import WritablePowerPortTemplateType
    from .writable_power_port_type import WritablePowerPortType
    from .writable_prefix import WritablePrefix
    from .writable_prefix_status import WritablePrefixStatus
    from .writable_provider import WritableProvider
    from .writable_provider_network import WritableProviderNetwork
    from .writable_rack import WritableRack
    from .writable_rack_outer_unit import WritableRackOuterUnit
    from .writable_rack_reservation import WritableRackReservation
    from .writable_rack_status import WritableRackStatus
    from .writable_rack_type import WritableRackType
    from .writable_rack_weight_unit import WritableRackWeightUnit
    from .writable_rear_port import WritableRearPort
    from .writable_rear_port_template import WritableRearPortTemplate
    from .writable_rear_port_template_type import WritableRearPortTemplateType
    from .writable_rear_port_type import WritableRearPortType
    from .writable_region import WritableRegion
    from .writable_route_target import WritableRouteTarget
    from .writable_service import WritableService
    from .writable_service_protocol import WritableServiceProtocol
    from .writable_service_template import WritableServiceTemplate
    from .writable_service_template_protocol import WritableServiceTemplateProtocol
    from .writable_site import WritableSite
    from .writable_site_group import WritableSiteGroup
    from .writable_site_status import WritableSiteStatus
    from .writable_tenant import WritableTenant
    from .writable_tenant_group import WritableTenantGroup
    from .writable_token import WritableToken
    from .writable_user import WritableUser
    from .writable_virtual_chassis import WritableVirtualChassis
    from .writable_virtual_device_context import WritableVirtualDeviceContext
    from .writable_virtual_device_context_status import WritableVirtualDeviceContextStatus
    from .writable_virtual_machine_with_config_context import WritableVirtualMachineWithConfigContext
    from .writable_virtual_machine_with_config_context_status import WritableVirtualMachineWithConfigContextStatus
    from .writable_vlan import WritableVlan
    from .writable_vlan_status import WritableVlanStatus
    from .writable_vm_interface import WritableVmInterface
    from .writable_vm_interface_mode import WritableVmInterfaceMode
    from .writable_vrf import WritableVrf
    from .writable_wireless_lan import WritableWirelessLan
    from .writable_wireless_lan_auth_cipher import WritableWirelessLanAuthCipher
    from .writable_wireless_lan_auth_type import WritableWirelessLanAuthType
    from .writable_wireless_lan_group import WritableWirelessLanGroup
    from .writable_wireless_lan_status import WritableWirelessLanStatus
    from .writable_wireless_link import WritableWirelessLink
    from .writable_wireless_link_auth_cipher import WritableWirelessLinkAuthCipher
    from .writable_wireless_link_auth_type import WritableWirelessLinkAuthType
    from .writable_wireless_link_status import WritableWirelessLinkStatus
_dynamic_imports: typing.Dict[str, str] = {
    "Aggregate": ".aggregate",
    "AggregateFamily": ".aggregate_family",
    "AggregateFamilyLabel": ".aggregate_family_label",
    "Asn": ".asn",
    "AvailableIp": ".available_ip",
    "AvailablePrefix": ".available_prefix",
    "AvailableVlan": ".available_vlan",
    "Cable": ".cable",
    "CableLengthUnit": ".cable_length_unit",
    "CableLengthUnitLabel": ".cable_length_unit_label",
    "CableLengthUnitValue": ".cable_length_unit_value",
    "CableStatus": ".cable_status",
    "CableStatusLabel": ".cable_status_label",
    "CableStatusValue": ".cable_status_value",
    "CableTermination": ".cable_termination",
    "CableTerminationCableEnd": ".cable_termination_cable_end",
    "CableType": ".cable_type",
    "Circuit": ".circuit",
    "CircuitCircuitTermination": ".circuit_circuit_termination",
    "CircuitStatus": ".circuit_status",
    "CircuitStatusLabel": ".circuit_status_label",
    "CircuitStatusValue": ".circuit_status_value",
    "CircuitTermination": ".circuit_termination",
    "CircuitTerminationTermSide": ".circuit_termination_term_side",
    "CircuitType": ".circuit_type",
    "Cluster": ".cluster",
    "ClusterGroup": ".cluster_group",
    "ClusterStatus": ".cluster_status",
    "ClusterStatusLabel": ".cluster_status_label",
    "ClusterStatusValue": ".cluster_status_value",
    "ClusterType": ".cluster_type",
    "ComponentNestedModule": ".component_nested_module",
    "ConfigContext": ".config_context",
    "ConsolePort": ".console_port",
    "ConsolePortSpeed": ".console_port_speed",
    "ConsolePortSpeedLabel": ".console_port_speed_label",
    "ConsolePortTemplate": ".console_port_template",
    "ConsolePortTemplateType": ".console_port_template_type",
    "ConsolePortTemplateTypeLabel": ".console_port_template_type_label",
    "ConsolePortTemplateTypeValue": ".console_port_template_type_value",
    "ConsolePortType": ".console_port_type",
    "ConsolePortTypeLabel": ".console_port_type_label",
    "ConsolePortTypeValue": ".console_port_type_value",
    "ConsoleServerPort": ".console_server_port",
    "ConsoleServerPortSpeed": ".console_server_port_speed",
    "ConsoleServerPortSpeedLabel": ".console_server_port_speed_label",
    "ConsoleServerPortTemplate": ".console_server_port_template",
    "ConsoleServerPortTemplateType": ".console_server_port_template_type",
    "ConsoleServerPortTemplateTypeLabel": ".console_server_port_template_type_label",
    "ConsoleServerPortTemplateTypeValue": ".console_server_port_template_type_value",
    "ConsoleServerPortType": ".console_server_port_type",
    "ConsoleServerPortTypeLabel": ".console_server_port_type_label",
    "ConsoleServerPortTypeValue": ".console_server_port_type_value",
    "Contact": ".contact",
    "ContactAssignment": ".contact_assignment",
    "ContactAssignmentPriority": ".contact_assignment_priority",
    "ContactAssignmentPriorityLabel": ".contact_assignment_priority_label",
    "ContactAssignmentPriorityValue": ".contact_assignment_priority_value",
    "ContactGroup": ".contact_group",
    "ContactRole": ".contact_role",
    "ContentType": ".content_type",
    "CustomField": ".custom_field",
    "CustomFieldFilterLogic": ".custom_field_filter_logic",
    "CustomFieldFilterLogicLabel": ".custom_field_filter_logic_label",
    "CustomFieldFilterLogicValue": ".custom_field_filter_logic_value",
    "CustomFieldType": ".custom_field_type",
    "CustomFieldTypeLabel": ".custom_field_type_label",
    "CustomFieldTypeValue": ".custom_field_type_value",
    "CustomFieldUiVisibility": ".custom_field_ui_visibility",
    "CustomFieldUiVisibilityLabel": ".custom_field_ui_visibility_label",
    "CustomFieldUiVisibilityValue": ".custom_field_ui_visibility_value",
    "CustomLink": ".custom_link",
    "CustomLinkButtonClass": ".custom_link_button_class",
    "Device": ".device",
    "DeviceAirflow": ".device_airflow",
    "DeviceAirflowLabel": ".device_airflow_label",
    "DeviceAirflowValue": ".device_airflow_value",
    "DeviceBay": ".device_bay",
    "DeviceBayTemplate": ".device_bay_template",
    "DeviceFace": ".device_face",
    "DeviceFaceLabel": ".device_face_label",
    "DeviceFaceValue": ".device_face_value",
    "DeviceNapalm": ".device_napalm",
    "DeviceRole": ".device_role",
    "DeviceStatus": ".device_status",
    "DeviceStatusLabel": ".device_status_label",
    "DeviceStatusValue": ".device_status_value",
    "DeviceType": ".device_type",
    "DeviceTypeAirflow": ".device_type_airflow",
    "DeviceTypeAirflowLabel": ".device_type_airflow_label",
    "DeviceTypeAirflowValue": ".device_type_airflow_value",
    "DeviceTypeSubdeviceRole": ".device_type_subdevice_role",
    "DeviceTypeSubdeviceRoleLabel": ".device_type_subdevice_role_label",
    "DeviceTypeSubdeviceRoleValue": ".device_type_subdevice_role_value",
    "DeviceTypeWeightUnit": ".device_type_weight_unit",
    "DeviceTypeWeightUnitLabel": ".device_type_weight_unit_label",
    "DeviceTypeWeightUnitValue": ".device_type_weight_unit_value",
    "DeviceWithConfigContext": ".device_with_config_context",
    "DeviceWithConfigContextAirflow": ".device_with_config_context_airflow",
    "DeviceWithConfigContextAirflowLabel": ".device_with_config_context_airflow_label",
    "DeviceWithConfigContextAirflowValue": ".device_with_config_context_airflow_value",
    "DeviceWithConfigContextFace": ".device_with_config_context_face",
    "DeviceWithConfigContextFaceLabel": ".device_with_config_context_face_label",
    "DeviceWithConfigContextFaceValue": ".device_with_config_context_face_value",
    "DeviceWithConfigContextStatus": ".device_with_config_context_status",
    "DeviceWithConfigContextStatusLabel": ".device_with_config_context_status_label",
    "DeviceWithConfigContextStatusValue": ".device_with_config_context_status_value",
    "ExportTemplate": ".export_template",
    "FhrpGroup": ".fhrp_group",
    "FhrpGroupAssignment": ".fhrp_group_assignment",
    "FhrpGroupAuthType": ".fhrp_group_auth_type",
    "FhrpGroupProtocol": ".fhrp_group_protocol",
    "FrontPort": ".front_port",
    "FrontPortRearPort": ".front_port_rear_port",
    "FrontPortTemplate": ".front_port_template",
    "FrontPortTemplateType": ".front_port_template_type",
    "FrontPortTemplateTypeLabel": ".front_port_template_type_label",
    "FrontPortTemplateTypeValue": ".front_port_template_type_value",
    "FrontPortType": ".front_port_type",
    "FrontPortTypeLabel": ".front_port_type_label",
    "FrontPortTypeValue": ".front_port_type_value",
    "GenericObject": ".generic_object",
    "Group": ".group",
    "ImageAttachment": ".image_attachment",
    "Interface": ".interface",
    "InterfaceDuplex": ".interface_duplex",
    "InterfaceDuplexLabel": ".interface_duplex_label",
    "InterfaceDuplexValue": ".interface_duplex_value",
    "InterfaceMode": ".interface_mode",
    "InterfaceModeLabel": ".interface_mode_label",
    "InterfaceModeValue": ".interface_mode_value",
    "InterfacePoeMode": ".interface_poe_mode",
    "InterfacePoeModeLabel": ".interface_poe_mode_label",
    "InterfacePoeModeValue": ".interface_poe_mode_value",
    "InterfacePoeType": ".interface_poe_type",
    "InterfacePoeTypeLabel": ".interface_poe_type_label",
    "InterfacePoeTypeValue": ".interface_poe_type_value",
    "InterfaceRfChannel": ".interface_rf_channel",
    "InterfaceRfChannelLabel": ".interface_rf_channel_label",
    "InterfaceRfChannelValue": ".interface_rf_channel_value",
    "InterfaceRfRole": ".interface_rf_role",
    "InterfaceRfRoleLabel": ".interface_rf_role_label",
    "InterfaceRfRoleValue": ".interface_rf_role_value",
    "InterfaceTemplate": ".interface_template",
    "InterfaceTemplatePoeMode": ".interface_template_poe_mode",
    "InterfaceTemplatePoeModeLabel": ".interface_template_poe_mode_label",
    "InterfaceTemplatePoeModeValue": ".interface_template_poe_mode_value",
    "InterfaceTemplatePoeType": ".interface_template_poe_type",
    "InterfaceTemplatePoeTypeLabel": ".interface_template_poe_type_label",
    "InterfaceTemplatePoeTypeValue": ".interface_template_poe_type_value",
    "InterfaceTemplateType": ".interface_template_type",
    "InterfaceTemplateTypeLabel": ".interface_template_type_label",
    "InterfaceTemplateTypeValue": ".interface_template_type_value",
    "InterfaceType": ".interface_type",
    "InterfaceTypeLabel": ".interface_type_label",
    "InterfaceTypeValue": ".interface_type_value",
    "InventoryItem": ".inventory_item",
    "InventoryItemRole": ".inventory_item_role",
    "InventoryItemTemplate": ".inventory_item_template",
    "IpAddress": ".ip_address",
    "IpAddressFamily": ".ip_address_family",
    "IpAddressFamilyLabel": ".ip_address_family_label",
    "IpAddressRole": ".ip_address_role",
    "IpAddressRoleLabel": ".ip_address_role_label",
    "IpAddressRoleValue": ".ip_address_role_value",
    "IpAddressStatus": ".ip_address_status",
    "IpAddressStatusLabel": ".ip_address_status_label",
    "IpAddressStatusValue": ".ip_address_status_value",
    "IpNetwork": ".ip_network",
    "IpRange": ".ip_range",
    "IpRangeFamily": ".ip_range_family",
    "IpRangeFamilyLabel": ".ip_range_family_label",
    "IpRangeStatus": ".ip_range_status",
    "IpRangeStatusLabel": ".ip_range_status_label",
    "IpRangeStatusValue": ".ip_range_status_value",
    "JobResult": ".job_result",
    "JobResultStatus": ".job_result_status",
    "JobResultStatusLabel": ".job_result_status_label",
    "JobResultStatusValue": ".job_result_status_value",
    "JournalEntry": ".journal_entry",
    "JournalEntryKind": ".journal_entry_kind",
    "JournalEntryKindLabel": ".journal_entry_kind_label",
    "JournalEntryKindValue": ".journal_entry_kind_value",
    "L2Vpn": ".l2vpn",
    "L2VpnTermination": ".l2vpn_termination",
    "L2VpnType": ".l2vpn_type",
    "L2VpnTypeLabel": ".l2vpn_type_label",
    "L2VpnTypeValue": ".l2vpn_type_value",
    "Location": ".location",
    "LocationStatus": ".location_status",
    "LocationStatusLabel": ".location_status_label",
    "LocationStatusValue": ".location_status_value",
    "Manufacturer": ".manufacturer",
    "Module": ".module",
    "ModuleBay": ".module_bay",
    "ModuleBayNestedModule": ".module_bay_nested_module",
    "ModuleBayTemplate": ".module_bay_template",
    "ModuleNestedModuleBay": ".module_nested_module_bay",
    "ModuleStatus": ".module_status",
    "ModuleStatusLabel": ".module_status_label",
    "ModuleStatusValue": ".module_status_value",
    "ModuleType": ".module_type",
    "ModuleTypeWeightUnit": ".module_type_weight_unit",
    "ModuleTypeWeightUnitLabel": ".module_type_weight_unit_label",
    "ModuleTypeWeightUnitValue": ".module_type_weight_unit_value",
    "NestedAsn": ".nested_asn",
    "NestedCable": ".nested_cable",
    "NestedCircuit": ".nested_circuit",
    "NestedCircuitType": ".nested_circuit_type",
    "NestedCluster": ".nested_cluster",
    "NestedClusterGroup": ".nested_cluster_group",
    "NestedClusterType": ".nested_cluster_type",
    "NestedContact": ".nested_contact",
    "NestedContactGroup": ".nested_contact_group",
    "NestedContactRole": ".nested_contact_role",
    "NestedDevice": ".nested_device",
    "NestedDeviceRole": ".nested_device_role",
    "NestedDeviceType": ".nested_device_type",
    "NestedFhrpGroup": ".nested_fhrp_group",
    "NestedFhrpGroupProtocol": ".nested_fhrp_group_protocol",
    "NestedGroup": ".nested_group",
    "NestedInterface": ".nested_interface",
    "NestedInventoryItemRole": ".nested_inventory_item_role",
    "NestedIpAddress": ".nested_ip_address",
    "NestedL2Vpn": ".nested_l2vpn",
    "NestedL2VpnTermination": ".nested_l2vpn_termination",
    "NestedL2VpnType": ".nested_l2vpn_type",
    "NestedLocation": ".nested_location",
    "NestedManufacturer": ".nested_manufacturer",
    "NestedModule": ".nested_module",
    "NestedModuleBay": ".nested_module_bay",
    "NestedModuleType": ".nested_module_type",
    "NestedPlatform": ".nested_platform",
    "NestedPowerPanel": ".nested_power_panel",
    "NestedPowerPort": ".nested_power_port",
    "NestedPowerPortTemplate": ".nested_power_port_template",
    "NestedProvider": ".nested_provider",
    "NestedProviderNetwork": ".nested_provider_network",
    "NestedRack": ".nested_rack",
    "NestedRackRole": ".nested_rack_role",
    "NestedRearPortTemplate": ".nested_rear_port_template",
    "NestedRegion": ".nested_region",
    "NestedRir": ".nested_rir",
    "NestedRole": ".nested_role",
    "NestedRouteTarget": ".nested_route_target",
    "NestedSite": ".nested_site",
    "NestedSiteGroup": ".nested_site_group",
    "NestedTag": ".nested_tag",
    "NestedTenant": ".nested_tenant",
    "NestedTenantGroup": ".nested_tenant_group",
    "NestedUser": ".nested_user",
    "NestedVirtualChassis": ".nested_virtual_chassis",
    "NestedVirtualDeviceContext": ".nested_virtual_device_context",
    "NestedVirtualMachine": ".nested_virtual_machine",
    "NestedVlan": ".nested_vlan",
    "NestedVlanGroup": ".nested_vlan_group",
    "NestedVmInterface": ".nested_vm_interface",
    "NestedVrf": ".nested_vrf",
    "NestedWirelessLan": ".nested_wireless_lan",
    "NestedWirelessLanGroup": ".nested_wireless_lan_group",
    "NestedWirelessLink": ".nested_wireless_link",
    "ObjectChange": ".object_change",
    "ObjectChangeAction": ".object_change_action",
    "ObjectChangeActionLabel": ".object_change_action_label",
    "ObjectChangeActionValue": ".object_change_action_value",
    "ObjectPermission": ".object_permission",
    "Platform": ".platform",
    "PowerFeed": ".power_feed",
    "PowerFeedPhase": ".power_feed_phase",
    "PowerFeedPhaseLabel": ".power_feed_phase_label",
    "PowerFeedPhaseValue": ".power_feed_phase_value",
    "PowerFeedStatus": ".power_feed_status",
    "PowerFeedStatusLabel": ".power_feed_status_label",
    "PowerFeedStatusValue": ".power_feed_status_value",
    "PowerFeedSupply": ".power_feed_supply",
    "PowerFeedSupplyLabel": ".power_feed_supply_label",
    "PowerFeedSupplyValue": ".power_feed_supply_value",
    "PowerFeedType": ".power_feed_type",
    "PowerFeedTypeLabel": ".power_feed_type_label",
    "PowerFeedTypeValue": ".power_feed_type_value",
    "PowerOutlet": ".power_outlet",
    "PowerOutletFeedLeg": ".power_outlet_feed_leg",
    "PowerOutletFeedLegLabel": ".power_outlet_feed_leg_label",
    "PowerOutletFeedLegValue": ".power_outlet_feed_leg_value",
    "PowerOutletTemplate": ".power_outlet_template",
    "PowerOutletTemplateFeedLeg": ".power_outlet_template_feed_leg",
    "PowerOutletTemplateFeedLegLabel": ".power_outlet_template_feed_leg_label",
    "PowerOutletTemplateFeedLegValue": ".power_outlet_template_feed_leg_value",
    "PowerOutletTemplateType": ".power_outlet_template_type",
    "PowerOutletTemplateTypeLabel": ".power_outlet_template_type_label",
    "PowerOutletTemplateTypeValue": ".power_outlet_template_type_value",
    "PowerOutletType": ".power_outlet_type",
    "PowerOutletTypeLabel": ".power_outlet_type_label",
    "PowerOutletTypeValue": ".power_outlet_type_value",
    "PowerPanel": ".power_panel",
    "PowerPort": ".power_port",
    "PowerPortTemplate": ".power_port_template",
    "PowerPortTemplateType": ".power_port_template_type",
    "PowerPortTemplateTypeLabel": ".power_port_template_type_label",
    "PowerPortTemplateTypeValue": ".power_port_template_type_value",
    "PowerPortType": ".power_port_type",
    "PowerPortTypeLabel": ".power_port_type_label",
    "PowerPortTypeValue": ".power_port_type_value",
    "Prefix": ".prefix",
    "PrefixFamily": ".prefix_family",
    "PrefixFamilyLabel": ".prefix_family_label",
    "PrefixStatus": ".prefix_status",
    "PrefixStatusLabel": ".prefix_status_label",
    "PrefixStatusValue": ".prefix_status_value",
    "Provider": ".provider",
    "ProviderNetwork": ".provider_network",
    "Rack": ".rack",
    "RackOuterUnit": ".rack_outer_unit",
    "RackOuterUnitLabel": ".rack_outer_unit_label",
    "RackOuterUnitValue": ".rack_outer_unit_value",
    "RackReservation": ".rack_reservation",
    "RackRole": ".rack_role",
    "RackStatus": ".rack_status",
    "RackStatusLabel": ".rack_status_label",
    "RackStatusValue": ".rack_status_value",
    "RackType": ".rack_type",
    "RackTypeLabel": ".rack_type_label",
    "RackTypeValue": ".rack_type_value",
    "RackUnit": ".rack_unit",
    "RackUnitFace": ".rack_unit_face",
    "RackUnitFaceLabel": ".rack_unit_face_label",
    "RackUnitFaceValue": ".rack_unit_face_value",
    "RackWeightUnit": ".rack_weight_unit",
    "RackWeightUnitLabel": ".rack_weight_unit_label",
    "RackWeightUnitValue": ".rack_weight_unit_value",
    "RackWidth": ".rack_width",
    "RackWidthLabel": ".rack_width_label",
    "RearPort": ".rear_port",
    "RearPortTemplate": ".rear_port_template",
    "RearPortTemplateType": ".rear_port_template_type",
    "RearPortTemplateTypeLabel": ".rear_port_template_type_label",
    "RearPortTemplateTypeValue": ".rear_port_template_type_value",
    "RearPortType": ".rear_port_type",
    "RearPortTypeLabel": ".rear_port_type_label",
    "RearPortTypeValue": ".rear_port_type_value",
    "Region": ".region",
    "Rir": ".rir",
    "Role": ".role",
    "RouteTarget": ".route_target",
    "SavedFilter": ".saved_filter",
    "Service": ".service",
    "ServiceProtocol": ".service_protocol",
    "ServiceProtocolLabel": ".service_protocol_label",
    "ServiceProtocolValue": ".service_protocol_value",
    "ServiceTemplate": ".service_template",
    "ServiceTemplateProtocol": ".service_template_protocol",
    "ServiceTemplateProtocolLabel": ".service_template_protocol_label",
    "ServiceTemplateProtocolValue": ".service_template_protocol_value",
    "Site": ".site",
    "SiteGroup": ".site_group",
    "SiteStatus": ".site_status",
    "SiteStatusLabel": ".site_status_label",
    "SiteStatusValue": ".site_status_value",
    "Tag": ".tag",
    "Tenant": ".tenant",
    "TenantGroup": ".tenant_group",
    "Token": ".token",
    "User": ".user",
    "VirtualChassis": ".virtual_chassis",
    "VirtualDeviceContext": ".virtual_device_context",
    "VirtualDeviceContextStatus": ".virtual_device_context_status",
    "VirtualMachineWithConfigContext": ".virtual_machine_with_config_context",
    "VirtualMachineWithConfigContextStatus": ".virtual_machine_with_config_context_status",
    "VirtualMachineWithConfigContextStatusLabel": ".virtual_machine_with_config_context_status_label",
    "VirtualMachineWithConfigContextStatusValue": ".virtual_machine_with_config_context_status_value",
    "Vlan": ".vlan",
    "VlanGroup": ".vlan_group",
    "VlanStatus": ".vlan_status",
    "VlanStatusLabel": ".vlan_status_label",
    "VlanStatusValue": ".vlan_status_value",
    "VmInterface": ".vm_interface",
    "VmInterfaceMode": ".vm_interface_mode",
    "VmInterfaceModeLabel": ".vm_interface_mode_label",
    "VmInterfaceModeValue": ".vm_interface_mode_value",
    "Vrf": ".vrf",
    "Webhook": ".webhook",
    "WebhookHttpMethod": ".webhook_http_method",
    "WirelessLan": ".wireless_lan",
    "WirelessLanAuthCipher": ".wireless_lan_auth_cipher",
    "WirelessLanAuthCipherLabel": ".wireless_lan_auth_cipher_label",
    "WirelessLanAuthCipherValue": ".wireless_lan_auth_cipher_value",
    "WirelessLanAuthType": ".wireless_lan_auth_type",
    "WirelessLanAuthTypeLabel": ".wireless_lan_auth_type_label",
    "WirelessLanAuthTypeValue": ".wireless_lan_auth_type_value",
    "WirelessLanGroup": ".wireless_lan_group",
    "WirelessLanStatus": ".wireless_lan_status",
    "WirelessLanStatusLabel": ".wireless_lan_status_label",
    "WirelessLanStatusValue": ".wireless_lan_status_value",
    "WirelessLink": ".wireless_link",
    "WirelessLinkAuthCipher": ".wireless_link_auth_cipher",
    "WirelessLinkAuthCipherLabel": ".wireless_link_auth_cipher_label",
    "WirelessLinkAuthCipherValue": ".wireless_link_auth_cipher_value",
    "WirelessLinkAuthType": ".wireless_link_auth_type",
    "WirelessLinkAuthTypeLabel": ".wireless_link_auth_type_label",
    "WirelessLinkAuthTypeValue": ".wireless_link_auth_type_value",
    "WirelessLinkStatus": ".wireless_link_status",
    "WirelessLinkStatusLabel": ".wireless_link_status_label",
    "WirelessLinkStatusValue": ".wireless_link_status_value",
    "WritableAggregate": ".writable_aggregate",
    "WritableAsn": ".writable_asn",
    "WritableAvailableIp": ".writable_available_ip",
    "WritableCable": ".writable_cable",
    "WritableCableLengthUnit": ".writable_cable_length_unit",
    "WritableCableStatus": ".writable_cable_status",
    "WritableCableType": ".writable_cable_type",
    "WritableCircuit": ".writable_circuit",
    "WritableCircuitStatus": ".writable_circuit_status",
    "WritableCircuitTermination": ".writable_circuit_termination",
    "WritableCircuitTerminationTermSide": ".writable_circuit_termination_term_side",
    "WritableCluster": ".writable_cluster",
    "WritableClusterStatus": ".writable_cluster_status",
    "WritableConfigContext": ".writable_config_context",
    "WritableConsolePort": ".writable_console_port",
    "WritableConsolePortTemplate": ".writable_console_port_template",
    "WritableConsolePortTemplateType": ".writable_console_port_template_type",
    "WritableConsolePortType": ".writable_console_port_type",
    "WritableConsoleServerPort": ".writable_console_server_port",
    "WritableConsoleServerPortTemplate": ".writable_console_server_port_template",
    "WritableConsoleServerPortTemplateType": ".writable_console_server_port_template_type",
    "WritableConsoleServerPortType": ".writable_console_server_port_type",
    "WritableContact": ".writable_contact",
    "WritableContactAssignment": ".writable_contact_assignment",
    "WritableContactAssignmentPriority": ".writable_contact_assignment_priority",
    "WritableContactGroup": ".writable_contact_group",
    "WritableCustomField": ".writable_custom_field",
    "WritableCustomFieldFilterLogic": ".writable_custom_field_filter_logic",
    "WritableCustomFieldType": ".writable_custom_field_type",
    "WritableCustomFieldUiVisibility": ".writable_custom_field_ui_visibility",
    "WritableDeviceBay": ".writable_device_bay",
    "WritableDeviceBayTemplate": ".writable_device_bay_template",
    "WritableDeviceType": ".writable_device_type",
    "WritableDeviceTypeAirflow": ".writable_device_type_airflow",
    "WritableDeviceTypeSubdeviceRole": ".writable_device_type_subdevice_role",
    "WritableDeviceTypeWeightUnit": ".writable_device_type_weight_unit",
    "WritableDeviceWithConfigContext": ".writable_device_with_config_context",
    "WritableDeviceWithConfigContextAirflow": ".writable_device_with_config_context_airflow",
    "WritableDeviceWithConfigContextFace": ".writable_device_with_config_context_face",
    "WritableDeviceWithConfigContextStatus": ".writable_device_with_config_context_status",
    "WritableFhrpGroupAssignment": ".writable_fhrp_group_assignment",
    "WritableFrontPort": ".writable_front_port",
    "WritableFrontPortTemplate": ".writable_front_port_template",
    "WritableFrontPortTemplateType": ".writable_front_port_template_type",
    "WritableFrontPortType": ".writable_front_port_type",
    "WritableInterface": ".writable_interface",
    "WritableInterfaceDuplex": ".writable_interface_duplex",
    "WritableInterfaceMode": ".writable_interface_mode",
    "WritableInterfacePoeMode": ".writable_interface_poe_mode",
    "WritableInterfacePoeType": ".writable_interface_poe_type",
    "WritableInterfaceRfChannel": ".writable_interface_rf_channel",
    "WritableInterfaceRfRole": ".writable_interface_rf_role",
    "WritableInterfaceTemplate": ".writable_interface_template",
    "WritableInterfaceTemplatePoeMode": ".writable_interface_template_poe_mode",
    "WritableInterfaceTemplatePoeType": ".writable_interface_template_poe_type",
    "WritableInterfaceTemplateType": ".writable_interface_template_type",
    "WritableInterfaceType": ".writable_interface_type",
    "WritableInventoryItem": ".writable_inventory_item",
    "WritableInventoryItemTemplate": ".writable_inventory_item_template",
    "WritableIpAddress": ".writable_ip_address",
    "WritableIpAddressRole": ".writable_ip_address_role",
    "WritableIpAddressStatus": ".writable_ip_address_status",
    "WritableIpRange": ".writable_ip_range",
    "WritableIpRangeStatus": ".writable_ip_range_status",
    "WritableJournalEntry": ".writable_journal_entry",
    "WritableJournalEntryKind": ".writable_journal_entry_kind",
    "WritableL2Vpn": ".writable_l2vpn",
    "WritableL2VpnTermination": ".writable_l2vpn_termination",
    "WritableL2VpnType": ".writable_l2vpn_type",
    "WritableLocation": ".writable_location",
    "WritableLocationStatus": ".writable_location_status",
    "WritableModule": ".writable_module",
    "WritableModuleBay": ".writable_module_bay",
    "WritableModuleBayTemplate": ".writable_module_bay_template",
    "WritableModuleStatus": ".writable_module_status",
    "WritableModuleType": ".writable_module_type",
    "WritableModuleTypeWeightUnit": ".writable_module_type_weight_unit",
    "WritableObjectPermission": ".writable_object_permission",
    "WritablePlatform": ".writable_platform",
    "WritablePowerFeed": ".writable_power_feed",
    "WritablePowerFeedPhase": ".writable_power_feed_phase",
    "WritablePowerFeedStatus": ".writable_power_feed_status",
    "WritablePowerFeedSupply": ".writable_power_feed_supply",
    "WritablePowerFeedType": ".writable_power_feed_type",
    "WritablePowerOutlet": ".writable_power_outlet",
    "WritablePowerOutletFeedLeg": ".writable_power_outlet_feed_leg",
    "WritablePowerOutletTemplate": ".writable_power_outlet_template",
    "WritablePowerOutletTemplateFeedLeg": ".writable_power_outlet_template_feed_leg",
    "WritablePowerOutletTemplateType": ".writable_power_outlet_template_type",
    "WritablePowerOutletType": ".writable_power_outlet_type",
    "WritablePowerPanel": ".writable_power_panel",
    "WritablePowerPort": ".writable_power_port",
    "WritablePowerPortTemplate": ".writable_power_port_template",
    "WritablePowerPortTemplateType": ".writable_power_port_template_type",
    "WritablePowerPortType": ".writable_power_port_type",
    "WritablePrefix": ".writable_prefix",
    "WritablePrefixStatus": ".writable_prefix_status",
    "WritableProvider": ".writable_provider",
    "WritableProviderNetwork": ".writable_provider_network",
    "WritableRack": ".writable_rack",
    "WritableRackOuterUnit": ".writable_rack_outer_unit",
    "WritableRackReservation": ".writable_rack_reservation",
    "WritableRackStatus": ".writable_rack_status",
    "WritableRackType": ".writable_rack_type",
    "WritableRackWeightUnit": ".writable_rack_weight_unit",
    "WritableRearPort": ".writable_rear_port",
    "WritableRearPortTemplate": ".writable_rear_port_template",
    "WritableRearPortTemplateType": ".writable_rear_port_template_type",
    "WritableRearPortType": ".writable_rear_port_type",
    "WritableRegion": ".writable_region",
    "WritableRouteTarget": ".writable_route_target",
    "WritableService": ".writable_service",
    "WritableServiceProtocol": ".writable_service_protocol",
    "WritableServiceTemplate": ".writable_service_template",
    "WritableServiceTemplateProtocol": ".writable_service_template_protocol",
    "WritableSite": ".writable_site",
    "WritableSiteGroup": ".writable_site_group",
    "WritableSiteStatus": ".writable_site_status",
    "WritableTenant": ".writable_tenant",
    "WritableTenantGroup": ".writable_tenant_group",
    "WritableToken": ".writable_token",
    "WritableUser": ".writable_user",
    "WritableVirtualChassis": ".writable_virtual_chassis",
    "WritableVirtualDeviceContext": ".writable_virtual_device_context",
    "WritableVirtualDeviceContextStatus": ".writable_virtual_device_context_status",
    "WritableVirtualMachineWithConfigContext": ".writable_virtual_machine_with_config_context",
    "WritableVirtualMachineWithConfigContextStatus": ".writable_virtual_machine_with_config_context_status",
    "WritableVlan": ".writable_vlan",
    "WritableVlanStatus": ".writable_vlan_status",
    "WritableVmInterface": ".writable_vm_interface",
    "WritableVmInterfaceMode": ".writable_vm_interface_mode",
    "WritableVrf": ".writable_vrf",
    "WritableWirelessLan": ".writable_wireless_lan",
    "WritableWirelessLanAuthCipher": ".writable_wireless_lan_auth_cipher",
    "WritableWirelessLanAuthType": ".writable_wireless_lan_auth_type",
    "WritableWirelessLanGroup": ".writable_wireless_lan_group",
    "WritableWirelessLanStatus": ".writable_wireless_lan_status",
    "WritableWirelessLink": ".writable_wireless_link",
    "WritableWirelessLinkAuthCipher": ".writable_wireless_link_auth_cipher",
    "WritableWirelessLinkAuthType": ".writable_wireless_link_auth_type",
    "WritableWirelessLinkStatus": ".writable_wireless_link_status",
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
    "Aggregate",
    "AggregateFamily",
    "AggregateFamilyLabel",
    "Asn",
    "AvailableIp",
    "AvailablePrefix",
    "AvailableVlan",
    "Cable",
    "CableLengthUnit",
    "CableLengthUnitLabel",
    "CableLengthUnitValue",
    "CableStatus",
    "CableStatusLabel",
    "CableStatusValue",
    "CableTermination",
    "CableTerminationCableEnd",
    "CableType",
    "Circuit",
    "CircuitCircuitTermination",
    "CircuitStatus",
    "CircuitStatusLabel",
    "CircuitStatusValue",
    "CircuitTermination",
    "CircuitTerminationTermSide",
    "CircuitType",
    "Cluster",
    "ClusterGroup",
    "ClusterStatus",
    "ClusterStatusLabel",
    "ClusterStatusValue",
    "ClusterType",
    "ComponentNestedModule",
    "ConfigContext",
    "ConsolePort",
    "ConsolePortSpeed",
    "ConsolePortSpeedLabel",
    "ConsolePortTemplate",
    "ConsolePortTemplateType",
    "ConsolePortTemplateTypeLabel",
    "ConsolePortTemplateTypeValue",
    "ConsolePortType",
    "ConsolePortTypeLabel",
    "ConsolePortTypeValue",
    "ConsoleServerPort",
    "ConsoleServerPortSpeed",
    "ConsoleServerPortSpeedLabel",
    "ConsoleServerPortTemplate",
    "ConsoleServerPortTemplateType",
    "ConsoleServerPortTemplateTypeLabel",
    "ConsoleServerPortTemplateTypeValue",
    "ConsoleServerPortType",
    "ConsoleServerPortTypeLabel",
    "ConsoleServerPortTypeValue",
    "Contact",
    "ContactAssignment",
    "ContactAssignmentPriority",
    "ContactAssignmentPriorityLabel",
    "ContactAssignmentPriorityValue",
    "ContactGroup",
    "ContactRole",
    "ContentType",
    "CustomField",
    "CustomFieldFilterLogic",
    "CustomFieldFilterLogicLabel",
    "CustomFieldFilterLogicValue",
    "CustomFieldType",
    "CustomFieldTypeLabel",
    "CustomFieldTypeValue",
    "CustomFieldUiVisibility",
    "CustomFieldUiVisibilityLabel",
    "CustomFieldUiVisibilityValue",
    "CustomLink",
    "CustomLinkButtonClass",
    "Device",
    "DeviceAirflow",
    "DeviceAirflowLabel",
    "DeviceAirflowValue",
    "DeviceBay",
    "DeviceBayTemplate",
    "DeviceFace",
    "DeviceFaceLabel",
    "DeviceFaceValue",
    "DeviceNapalm",
    "DeviceRole",
    "DeviceStatus",
    "DeviceStatusLabel",
    "DeviceStatusValue",
    "DeviceType",
    "DeviceTypeAirflow",
    "DeviceTypeAirflowLabel",
    "DeviceTypeAirflowValue",
    "DeviceTypeSubdeviceRole",
    "DeviceTypeSubdeviceRoleLabel",
    "DeviceTypeSubdeviceRoleValue",
    "DeviceTypeWeightUnit",
    "DeviceTypeWeightUnitLabel",
    "DeviceTypeWeightUnitValue",
    "DeviceWithConfigContext",
    "DeviceWithConfigContextAirflow",
    "DeviceWithConfigContextAirflowLabel",
    "DeviceWithConfigContextAirflowValue",
    "DeviceWithConfigContextFace",
    "DeviceWithConfigContextFaceLabel",
    "DeviceWithConfigContextFaceValue",
    "DeviceWithConfigContextStatus",
    "DeviceWithConfigContextStatusLabel",
    "DeviceWithConfigContextStatusValue",
    "ExportTemplate",
    "FhrpGroup",
    "FhrpGroupAssignment",
    "FhrpGroupAuthType",
    "FhrpGroupProtocol",
    "FrontPort",
    "FrontPortRearPort",
    "FrontPortTemplate",
    "FrontPortTemplateType",
    "FrontPortTemplateTypeLabel",
    "FrontPortTemplateTypeValue",
    "FrontPortType",
    "FrontPortTypeLabel",
    "FrontPortTypeValue",
    "GenericObject",
    "Group",
    "ImageAttachment",
    "Interface",
    "InterfaceDuplex",
    "InterfaceDuplexLabel",
    "InterfaceDuplexValue",
    "InterfaceMode",
    "InterfaceModeLabel",
    "InterfaceModeValue",
    "InterfacePoeMode",
    "InterfacePoeModeLabel",
    "InterfacePoeModeValue",
    "InterfacePoeType",
    "InterfacePoeTypeLabel",
    "InterfacePoeTypeValue",
    "InterfaceRfChannel",
    "InterfaceRfChannelLabel",
    "InterfaceRfChannelValue",
    "InterfaceRfRole",
    "InterfaceRfRoleLabel",
    "InterfaceRfRoleValue",
    "InterfaceTemplate",
    "InterfaceTemplatePoeMode",
    "InterfaceTemplatePoeModeLabel",
    "InterfaceTemplatePoeModeValue",
    "InterfaceTemplatePoeType",
    "InterfaceTemplatePoeTypeLabel",
    "InterfaceTemplatePoeTypeValue",
    "InterfaceTemplateType",
    "InterfaceTemplateTypeLabel",
    "InterfaceTemplateTypeValue",
    "InterfaceType",
    "InterfaceTypeLabel",
    "InterfaceTypeValue",
    "InventoryItem",
    "InventoryItemRole",
    "InventoryItemTemplate",
    "IpAddress",
    "IpAddressFamily",
    "IpAddressFamilyLabel",
    "IpAddressRole",
    "IpAddressRoleLabel",
    "IpAddressRoleValue",
    "IpAddressStatus",
    "IpAddressStatusLabel",
    "IpAddressStatusValue",
    "IpNetwork",
    "IpRange",
    "IpRangeFamily",
    "IpRangeFamilyLabel",
    "IpRangeStatus",
    "IpRangeStatusLabel",
    "IpRangeStatusValue",
    "JobResult",
    "JobResultStatus",
    "JobResultStatusLabel",
    "JobResultStatusValue",
    "JournalEntry",
    "JournalEntryKind",
    "JournalEntryKindLabel",
    "JournalEntryKindValue",
    "L2Vpn",
    "L2VpnTermination",
    "L2VpnType",
    "L2VpnTypeLabel",
    "L2VpnTypeValue",
    "Location",
    "LocationStatus",
    "LocationStatusLabel",
    "LocationStatusValue",
    "Manufacturer",
    "Module",
    "ModuleBay",
    "ModuleBayNestedModule",
    "ModuleBayTemplate",
    "ModuleNestedModuleBay",
    "ModuleStatus",
    "ModuleStatusLabel",
    "ModuleStatusValue",
    "ModuleType",
    "ModuleTypeWeightUnit",
    "ModuleTypeWeightUnitLabel",
    "ModuleTypeWeightUnitValue",
    "NestedAsn",
    "NestedCable",
    "NestedCircuit",
    "NestedCircuitType",
    "NestedCluster",
    "NestedClusterGroup",
    "NestedClusterType",
    "NestedContact",
    "NestedContactGroup",
    "NestedContactRole",
    "NestedDevice",
    "NestedDeviceRole",
    "NestedDeviceType",
    "NestedFhrpGroup",
    "NestedFhrpGroupProtocol",
    "NestedGroup",
    "NestedInterface",
    "NestedInventoryItemRole",
    "NestedIpAddress",
    "NestedL2Vpn",
    "NestedL2VpnTermination",
    "NestedL2VpnType",
    "NestedLocation",
    "NestedManufacturer",
    "NestedModule",
    "NestedModuleBay",
    "NestedModuleType",
    "NestedPlatform",
    "NestedPowerPanel",
    "NestedPowerPort",
    "NestedPowerPortTemplate",
    "NestedProvider",
    "NestedProviderNetwork",
    "NestedRack",
    "NestedRackRole",
    "NestedRearPortTemplate",
    "NestedRegion",
    "NestedRir",
    "NestedRole",
    "NestedRouteTarget",
    "NestedSite",
    "NestedSiteGroup",
    "NestedTag",
    "NestedTenant",
    "NestedTenantGroup",
    "NestedUser",
    "NestedVirtualChassis",
    "NestedVirtualDeviceContext",
    "NestedVirtualMachine",
    "NestedVlan",
    "NestedVlanGroup",
    "NestedVmInterface",
    "NestedVrf",
    "NestedWirelessLan",
    "NestedWirelessLanGroup",
    "NestedWirelessLink",
    "ObjectChange",
    "ObjectChangeAction",
    "ObjectChangeActionLabel",
    "ObjectChangeActionValue",
    "ObjectPermission",
    "Platform",
    "PowerFeed",
    "PowerFeedPhase",
    "PowerFeedPhaseLabel",
    "PowerFeedPhaseValue",
    "PowerFeedStatus",
    "PowerFeedStatusLabel",
    "PowerFeedStatusValue",
    "PowerFeedSupply",
    "PowerFeedSupplyLabel",
    "PowerFeedSupplyValue",
    "PowerFeedType",
    "PowerFeedTypeLabel",
    "PowerFeedTypeValue",
    "PowerOutlet",
    "PowerOutletFeedLeg",
    "PowerOutletFeedLegLabel",
    "PowerOutletFeedLegValue",
    "PowerOutletTemplate",
    "PowerOutletTemplateFeedLeg",
    "PowerOutletTemplateFeedLegLabel",
    "PowerOutletTemplateFeedLegValue",
    "PowerOutletTemplateType",
    "PowerOutletTemplateTypeLabel",
    "PowerOutletTemplateTypeValue",
    "PowerOutletType",
    "PowerOutletTypeLabel",
    "PowerOutletTypeValue",
    "PowerPanel",
    "PowerPort",
    "PowerPortTemplate",
    "PowerPortTemplateType",
    "PowerPortTemplateTypeLabel",
    "PowerPortTemplateTypeValue",
    "PowerPortType",
    "PowerPortTypeLabel",
    "PowerPortTypeValue",
    "Prefix",
    "PrefixFamily",
    "PrefixFamilyLabel",
    "PrefixStatus",
    "PrefixStatusLabel",
    "PrefixStatusValue",
    "Provider",
    "ProviderNetwork",
    "Rack",
    "RackOuterUnit",
    "RackOuterUnitLabel",
    "RackOuterUnitValue",
    "RackReservation",
    "RackRole",
    "RackStatus",
    "RackStatusLabel",
    "RackStatusValue",
    "RackType",
    "RackTypeLabel",
    "RackTypeValue",
    "RackUnit",
    "RackUnitFace",
    "RackUnitFaceLabel",
    "RackUnitFaceValue",
    "RackWeightUnit",
    "RackWeightUnitLabel",
    "RackWeightUnitValue",
    "RackWidth",
    "RackWidthLabel",
    "RearPort",
    "RearPortTemplate",
    "RearPortTemplateType",
    "RearPortTemplateTypeLabel",
    "RearPortTemplateTypeValue",
    "RearPortType",
    "RearPortTypeLabel",
    "RearPortTypeValue",
    "Region",
    "Rir",
    "Role",
    "RouteTarget",
    "SavedFilter",
    "Service",
    "ServiceProtocol",
    "ServiceProtocolLabel",
    "ServiceProtocolValue",
    "ServiceTemplate",
    "ServiceTemplateProtocol",
    "ServiceTemplateProtocolLabel",
    "ServiceTemplateProtocolValue",
    "Site",
    "SiteGroup",
    "SiteStatus",
    "SiteStatusLabel",
    "SiteStatusValue",
    "Tag",
    "Tenant",
    "TenantGroup",
    "Token",
    "User",
    "VirtualChassis",
    "VirtualDeviceContext",
    "VirtualDeviceContextStatus",
    "VirtualMachineWithConfigContext",
    "VirtualMachineWithConfigContextStatus",
    "VirtualMachineWithConfigContextStatusLabel",
    "VirtualMachineWithConfigContextStatusValue",
    "Vlan",
    "VlanGroup",
    "VlanStatus",
    "VlanStatusLabel",
    "VlanStatusValue",
    "VmInterface",
    "VmInterfaceMode",
    "VmInterfaceModeLabel",
    "VmInterfaceModeValue",
    "Vrf",
    "Webhook",
    "WebhookHttpMethod",
    "WirelessLan",
    "WirelessLanAuthCipher",
    "WirelessLanAuthCipherLabel",
    "WirelessLanAuthCipherValue",
    "WirelessLanAuthType",
    "WirelessLanAuthTypeLabel",
    "WirelessLanAuthTypeValue",
    "WirelessLanGroup",
    "WirelessLanStatus",
    "WirelessLanStatusLabel",
    "WirelessLanStatusValue",
    "WirelessLink",
    "WirelessLinkAuthCipher",
    "WirelessLinkAuthCipherLabel",
    "WirelessLinkAuthCipherValue",
    "WirelessLinkAuthType",
    "WirelessLinkAuthTypeLabel",
    "WirelessLinkAuthTypeValue",
    "WirelessLinkStatus",
    "WirelessLinkStatusLabel",
    "WirelessLinkStatusValue",
    "WritableAggregate",
    "WritableAsn",
    "WritableAvailableIp",
    "WritableCable",
    "WritableCableLengthUnit",
    "WritableCableStatus",
    "WritableCableType",
    "WritableCircuit",
    "WritableCircuitStatus",
    "WritableCircuitTermination",
    "WritableCircuitTerminationTermSide",
    "WritableCluster",
    "WritableClusterStatus",
    "WritableConfigContext",
    "WritableConsolePort",
    "WritableConsolePortTemplate",
    "WritableConsolePortTemplateType",
    "WritableConsolePortType",
    "WritableConsoleServerPort",
    "WritableConsoleServerPortTemplate",
    "WritableConsoleServerPortTemplateType",
    "WritableConsoleServerPortType",
    "WritableContact",
    "WritableContactAssignment",
    "WritableContactAssignmentPriority",
    "WritableContactGroup",
    "WritableCustomField",
    "WritableCustomFieldFilterLogic",
    "WritableCustomFieldType",
    "WritableCustomFieldUiVisibility",
    "WritableDeviceBay",
    "WritableDeviceBayTemplate",
    "WritableDeviceType",
    "WritableDeviceTypeAirflow",
    "WritableDeviceTypeSubdeviceRole",
    "WritableDeviceTypeWeightUnit",
    "WritableDeviceWithConfigContext",
    "WritableDeviceWithConfigContextAirflow",
    "WritableDeviceWithConfigContextFace",
    "WritableDeviceWithConfigContextStatus",
    "WritableFhrpGroupAssignment",
    "WritableFrontPort",
    "WritableFrontPortTemplate",
    "WritableFrontPortTemplateType",
    "WritableFrontPortType",
    "WritableInterface",
    "WritableInterfaceDuplex",
    "WritableInterfaceMode",
    "WritableInterfacePoeMode",
    "WritableInterfacePoeType",
    "WritableInterfaceRfChannel",
    "WritableInterfaceRfRole",
    "WritableInterfaceTemplate",
    "WritableInterfaceTemplatePoeMode",
    "WritableInterfaceTemplatePoeType",
    "WritableInterfaceTemplateType",
    "WritableInterfaceType",
    "WritableInventoryItem",
    "WritableInventoryItemTemplate",
    "WritableIpAddress",
    "WritableIpAddressRole",
    "WritableIpAddressStatus",
    "WritableIpRange",
    "WritableIpRangeStatus",
    "WritableJournalEntry",
    "WritableJournalEntryKind",
    "WritableL2Vpn",
    "WritableL2VpnTermination",
    "WritableL2VpnType",
    "WritableLocation",
    "WritableLocationStatus",
    "WritableModule",
    "WritableModuleBay",
    "WritableModuleBayTemplate",
    "WritableModuleStatus",
    "WritableModuleType",
    "WritableModuleTypeWeightUnit",
    "WritableObjectPermission",
    "WritablePlatform",
    "WritablePowerFeed",
    "WritablePowerFeedPhase",
    "WritablePowerFeedStatus",
    "WritablePowerFeedSupply",
    "WritablePowerFeedType",
    "WritablePowerOutlet",
    "WritablePowerOutletFeedLeg",
    "WritablePowerOutletTemplate",
    "WritablePowerOutletTemplateFeedLeg",
    "WritablePowerOutletTemplateType",
    "WritablePowerOutletType",
    "WritablePowerPanel",
    "WritablePowerPort",
    "WritablePowerPortTemplate",
    "WritablePowerPortTemplateType",
    "WritablePowerPortType",
    "WritablePrefix",
    "WritablePrefixStatus",
    "WritableProvider",
    "WritableProviderNetwork",
    "WritableRack",
    "WritableRackOuterUnit",
    "WritableRackReservation",
    "WritableRackStatus",
    "WritableRackType",
    "WritableRackWeightUnit",
    "WritableRearPort",
    "WritableRearPortTemplate",
    "WritableRearPortTemplateType",
    "WritableRearPortType",
    "WritableRegion",
    "WritableRouteTarget",
    "WritableService",
    "WritableServiceProtocol",
    "WritableServiceTemplate",
    "WritableServiceTemplateProtocol",
    "WritableSite",
    "WritableSiteGroup",
    "WritableSiteStatus",
    "WritableTenant",
    "WritableTenantGroup",
    "WritableToken",
    "WritableUser",
    "WritableVirtualChassis",
    "WritableVirtualDeviceContext",
    "WritableVirtualDeviceContextStatus",
    "WritableVirtualMachineWithConfigContext",
    "WritableVirtualMachineWithConfigContextStatus",
    "WritableVlan",
    "WritableVlanStatus",
    "WritableVmInterface",
    "WritableVmInterfaceMode",
    "WritableVrf",
    "WritableWirelessLan",
    "WritableWirelessLanAuthCipher",
    "WritableWirelessLanAuthType",
    "WritableWirelessLanGroup",
    "WritableWirelessLanStatus",
    "WritableWirelessLink",
    "WritableWirelessLinkAuthCipher",
    "WritableWirelessLinkAuthType",
    "WritableWirelessLinkStatus",
]
