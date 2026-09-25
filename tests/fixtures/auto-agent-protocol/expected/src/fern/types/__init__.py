



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .a2a_data_part import A2ADataPart
    from .a2a_message import A2AMessage
    from .a2a_message_request_configuration import A2AMessageRequestConfiguration
    from .a2a_message_response import A2AMessageResponse
    from .a2a_message_role import A2AMessageRole
    from .aap_message import AapMessage
    from .address import Address
    from .agent_card import AgentCard
    from .agent_card_capabilities import AgentCardCapabilities
    from .agent_card_provider import AgentCardProvider
    from .agent_card_supported_interfaces_item import AgentCardSupportedInterfacesItem
    from .agent_card_supported_interfaces_item_protocol_binding import AgentCardSupportedInterfacesItemProtocolBinding
    from .appointment import Appointment
    from .appointment_appointment_type import AppointmentAppointmentType
    from .consent_grant import ConsentGrant
    from .consent_grant_allowed_channels_item import ConsentGrantAllowedChannelsItem
    from .consent_grant_scope_item import ConsentGrantScopeItem
    from .customer import Customer
    from .customer_preferred_contact import CustomerPreferredContact
    from .dealer_information import DealerInformation
    from .dealer_information_request import DealerInformationRequest
    from .dealer_information_request_type import DealerInformationRequestType
    from .dealer_information_response import DealerInformationResponse
    from .dealer_information_response_type import DealerInformationResponseType
    from .error import Error
    from .error_code import ErrorCode
    from .error_type import ErrorType
    from .event import Event
    from .event_event_kind import EventEventKind
    from .event_type import EventType
    from .facets import Facets
    from .inventory_facets_request import InventoryFacetsRequest
    from .inventory_facets_request_type import InventoryFacetsRequestType
    from .inventory_facets_response import InventoryFacetsResponse
    from .inventory_facets_response_type import InventoryFacetsResponseType
    from .inventory_search_request import InventorySearchRequest
    from .inventory_search_request_pagination import InventorySearchRequestPagination
    from .inventory_search_request_privacy import InventorySearchRequestPrivacy
    from .inventory_search_request_sort import InventorySearchRequestSort
    from .inventory_search_request_sort_field import InventorySearchRequestSortField
    from .inventory_search_request_sort_order import InventorySearchRequestSortOrder
    from .inventory_search_request_type import InventorySearchRequestType
    from .inventory_search_response import InventorySearchResponse
    from .inventory_search_response_data import InventorySearchResponseData
    from .inventory_search_response_data_vehicles_item import InventorySearchResponseDataVehiclesItem
    from .inventory_search_response_data_vehicles_item_condition import InventorySearchResponseDataVehiclesItemCondition
    from .inventory_search_response_type import InventorySearchResponseType
    from .lead_submit_request import LeadSubmitRequest
    from .lead_submit_request_type import LeadSubmitRequestType
    from .lead_submit_response import LeadSubmitResponse
    from .lead_submit_response_data import LeadSubmitResponseData
    from .lead_submit_response_data_appointment import LeadSubmitResponseDataAppointment
    from .lead_submit_response_data_appointment_status import LeadSubmitResponseDataAppointmentStatus
    from .lead_submit_response_data_dealer import LeadSubmitResponseDataDealer
    from .lead_submit_response_data_status import LeadSubmitResponseDataStatus
    from .lead_submit_response_type import LeadSubmitResponseType
    from .vehicle import Vehicle
    from .vehicle_condition import VehicleCondition
    from .vehicle_detail_request import VehicleDetailRequest
    from .vehicle_detail_request_type import VehicleDetailRequestType
    from .vehicle_detail_response import VehicleDetailResponse
    from .vehicle_detail_response_data import VehicleDetailResponseData
    from .vehicle_detail_response_data_condition import VehicleDetailResponseDataCondition
    from .vehicle_detail_response_type import VehicleDetailResponseType
    from .vehicle_status import VehicleStatus
_dynamic_imports: typing.Dict[str, str] = {
    "A2ADataPart": ".a2a_data_part",
    "A2AMessage": ".a2a_message",
    "A2AMessageRequestConfiguration": ".a2a_message_request_configuration",
    "A2AMessageResponse": ".a2a_message_response",
    "A2AMessageRole": ".a2a_message_role",
    "AapMessage": ".aap_message",
    "Address": ".address",
    "AgentCard": ".agent_card",
    "AgentCardCapabilities": ".agent_card_capabilities",
    "AgentCardProvider": ".agent_card_provider",
    "AgentCardSupportedInterfacesItem": ".agent_card_supported_interfaces_item",
    "AgentCardSupportedInterfacesItemProtocolBinding": ".agent_card_supported_interfaces_item_protocol_binding",
    "Appointment": ".appointment",
    "AppointmentAppointmentType": ".appointment_appointment_type",
    "ConsentGrant": ".consent_grant",
    "ConsentGrantAllowedChannelsItem": ".consent_grant_allowed_channels_item",
    "ConsentGrantScopeItem": ".consent_grant_scope_item",
    "Customer": ".customer",
    "CustomerPreferredContact": ".customer_preferred_contact",
    "DealerInformation": ".dealer_information",
    "DealerInformationRequest": ".dealer_information_request",
    "DealerInformationRequestType": ".dealer_information_request_type",
    "DealerInformationResponse": ".dealer_information_response",
    "DealerInformationResponseType": ".dealer_information_response_type",
    "Error": ".error",
    "ErrorCode": ".error_code",
    "ErrorType": ".error_type",
    "Event": ".event",
    "EventEventKind": ".event_event_kind",
    "EventType": ".event_type",
    "Facets": ".facets",
    "InventoryFacetsRequest": ".inventory_facets_request",
    "InventoryFacetsRequestType": ".inventory_facets_request_type",
    "InventoryFacetsResponse": ".inventory_facets_response",
    "InventoryFacetsResponseType": ".inventory_facets_response_type",
    "InventorySearchRequest": ".inventory_search_request",
    "InventorySearchRequestPagination": ".inventory_search_request_pagination",
    "InventorySearchRequestPrivacy": ".inventory_search_request_privacy",
    "InventorySearchRequestSort": ".inventory_search_request_sort",
    "InventorySearchRequestSortField": ".inventory_search_request_sort_field",
    "InventorySearchRequestSortOrder": ".inventory_search_request_sort_order",
    "InventorySearchRequestType": ".inventory_search_request_type",
    "InventorySearchResponse": ".inventory_search_response",
    "InventorySearchResponseData": ".inventory_search_response_data",
    "InventorySearchResponseDataVehiclesItem": ".inventory_search_response_data_vehicles_item",
    "InventorySearchResponseDataVehiclesItemCondition": ".inventory_search_response_data_vehicles_item_condition",
    "InventorySearchResponseType": ".inventory_search_response_type",
    "LeadSubmitRequest": ".lead_submit_request",
    "LeadSubmitRequestType": ".lead_submit_request_type",
    "LeadSubmitResponse": ".lead_submit_response",
    "LeadSubmitResponseData": ".lead_submit_response_data",
    "LeadSubmitResponseDataAppointment": ".lead_submit_response_data_appointment",
    "LeadSubmitResponseDataAppointmentStatus": ".lead_submit_response_data_appointment_status",
    "LeadSubmitResponseDataDealer": ".lead_submit_response_data_dealer",
    "LeadSubmitResponseDataStatus": ".lead_submit_response_data_status",
    "LeadSubmitResponseType": ".lead_submit_response_type",
    "Vehicle": ".vehicle",
    "VehicleCondition": ".vehicle_condition",
    "VehicleDetailRequest": ".vehicle_detail_request",
    "VehicleDetailRequestType": ".vehicle_detail_request_type",
    "VehicleDetailResponse": ".vehicle_detail_response",
    "VehicleDetailResponseData": ".vehicle_detail_response_data",
    "VehicleDetailResponseDataCondition": ".vehicle_detail_response_data_condition",
    "VehicleDetailResponseType": ".vehicle_detail_response_type",
    "VehicleStatus": ".vehicle_status",
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
    "A2ADataPart",
    "A2AMessage",
    "A2AMessageRequestConfiguration",
    "A2AMessageResponse",
    "A2AMessageRole",
    "AapMessage",
    "Address",
    "AgentCard",
    "AgentCardCapabilities",
    "AgentCardProvider",
    "AgentCardSupportedInterfacesItem",
    "AgentCardSupportedInterfacesItemProtocolBinding",
    "Appointment",
    "AppointmentAppointmentType",
    "ConsentGrant",
    "ConsentGrantAllowedChannelsItem",
    "ConsentGrantScopeItem",
    "Customer",
    "CustomerPreferredContact",
    "DealerInformation",
    "DealerInformationRequest",
    "DealerInformationRequestType",
    "DealerInformationResponse",
    "DealerInformationResponseType",
    "Error",
    "ErrorCode",
    "ErrorType",
    "Event",
    "EventEventKind",
    "EventType",
    "Facets",
    "InventoryFacetsRequest",
    "InventoryFacetsRequestType",
    "InventoryFacetsResponse",
    "InventoryFacetsResponseType",
    "InventorySearchRequest",
    "InventorySearchRequestPagination",
    "InventorySearchRequestPrivacy",
    "InventorySearchRequestSort",
    "InventorySearchRequestSortField",
    "InventorySearchRequestSortOrder",
    "InventorySearchRequestType",
    "InventorySearchResponse",
    "InventorySearchResponseData",
    "InventorySearchResponseDataVehiclesItem",
    "InventorySearchResponseDataVehiclesItemCondition",
    "InventorySearchResponseType",
    "LeadSubmitRequest",
    "LeadSubmitRequestType",
    "LeadSubmitResponse",
    "LeadSubmitResponseData",
    "LeadSubmitResponseDataAppointment",
    "LeadSubmitResponseDataAppointmentStatus",
    "LeadSubmitResponseDataDealer",
    "LeadSubmitResponseDataStatus",
    "LeadSubmitResponseType",
    "Vehicle",
    "VehicleCondition",
    "VehicleDetailRequest",
    "VehicleDetailRequestType",
    "VehicleDetailResponse",
    "VehicleDetailResponseData",
    "VehicleDetailResponseDataCondition",
    "VehicleDetailResponseType",
    "VehicleStatus",
]
