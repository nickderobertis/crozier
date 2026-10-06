



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .address_use import AddressUse
    from .base64binary_type import Base64BinaryType
    from .base_calendar import BaseCalendar
    from .base_date_time_type import BaseDateTimeType
    from .boolean_type import BooleanType
    from .bundle import Bundle
    from .bundle_entry_component import BundleEntryComponent
    from .bundle_entry_request_component import BundleEntryRequestComponent
    from .bundle_entry_response_component import BundleEntryResponseComponent
    from .bundle_entry_search_component import BundleEntrySearchComponent
    from .bundle_link_component import BundleLinkComponent
    from .bundle_type import BundleType
    from .calendar_date import CalendarDate
    from .canonical_type import CanonicalType
    from .card_info_type import CardInfoType
    from .card_type_type import CardTypeType
    from .card_version import CardVersion
    from .cards import Cards
    from .change_pin_response import ChangePinResponse
    from .code_type import CodeType
    from .codeable_concept import CodeableConcept
    from .coding import Coding
    from .comfort_signature_status_enum import ComfortSignatureStatusEnum
    from .contact_point import ContactPoint
    from .contact_point_system import ContactPointSystem
    from .contact_point_use import ContactPointUse
    from .date import Date
    from .date1 import Date1
    from .date_time_type import DateTimeType
    from .decimal_type import DecimalType
    from .detail import Detail
    from .duration import Duration
    from .endpoint import Endpoint
    from .endpoint_status import EndpointStatus
    from .enum_factory_address_type import EnumFactoryAddressType
    from .enum_factory_address_use import EnumFactoryAddressUse
    from .enum_factory_bundle_type import EnumFactoryBundleType
    from .enum_factory_contact_point_system import EnumFactoryContactPointSystem
    from .enum_factory_contact_point_use import EnumFactoryContactPointUse
    from .enum_factory_endpoint_status import EnumFactoryEndpointStatus
    from .enum_factory_http_verb import EnumFactoryHttpVerb
    from .enum_factory_identifier_use import EnumFactoryIdentifierUse
    from .enum_factory_name_use import EnumFactoryNameUse
    from .enum_factory_narrative_status import EnumFactoryNarrativeStatus
    from .enum_factory_search_entry_mode import EnumFactorySearchEntryMode
    from .enumeration_address_type import EnumerationAddressType
    from .enumeration_address_use import EnumerationAddressUse
    from .enumeration_bundle_type import EnumerationBundleType
    from .enumeration_contact_point_system import EnumerationContactPointSystem
    from .enumeration_contact_point_use import EnumerationContactPointUse
    from .enumeration_endpoint_status import EnumerationEndpointStatus
    from .enumeration_http_verb import EnumerationHttpVerb
    from .enumeration_identifier_use import EnumerationIdentifierUse
    from .enumeration_name_use import EnumerationNameUse
    from .enumeration_narrative_status import EnumerationNarrativeStatus
    from .enumeration_search_entry_mode import EnumerationSearchEntryMode
    from .era import Era
    from .error import Error
    from .extension import Extension
    from .fhir_version_enum import FhirVersionEnum
    from .get_cards_response import GetCardsResponse
    from .get_pin_status_response import GetPinStatusResponse
    from .get_signature_mode_response_event import GetSignatureModeResponseEvent
    from .gregorian_calendar import GregorianCalendar
    from .http_verb import HttpVerb
    from .human_name import HumanName
    from .i_base_coding import IBaseCoding
    from .i_base_datatype import IBaseDatatype
    from .i_base_extension_object_object import IBaseExtensionObjectObject
    from .i_base_meta_type import IBaseMetaType
    from .i_id_type import IIdType
    from .i_primitive_type_object import IPrimitiveTypeObject
    from .i_primitive_type_string import IPrimitiveTypeString
    from .id_type import IdType
    from .identifier import Identifier
    from .identifier_use import IdentifierUse
    from .instant_type import InstantType
    from .json_value import JsonValue
    from .locale import Locale
    from .location import Location
    from .meta import Meta
    from .name_use import NameUse
    from .narrative import Narrative
    from .narrative_status import NarrativeStatus
    from .node_type import NodeType
    from .organization import Organization
    from .organization_contact_component import OrganizationContactComponent
    from .period import Period
    from .pin_result_enum import PinResultEnum
    from .pin_status_enum import PinStatusEnum
    from .positive_int_type import PositiveIntType
    from .q_name import QName
    from .reference import Reference
    from .resource import Resource
    from .resource_type import ResourceType
    from .search_entry_mode import SearchEntryMode
    from .session_info import SessionInfo
    from .signature import Signature
    from .signature_mode_enum import SignatureModeEnum
    from .status import Status
    from .string_type import StringType
    from .temporal_precision_enum import TemporalPrecisionEnum
    from .time_zone import TimeZone
    from .trace import Trace
    from .type import Type
    from .unblock_pin_response import UnblockPinResponse
    from .unsigned_int_type import UnsignedIntType
    from .uri_type import UriType
    from .url_type import UrlType
    from .value_type import ValueType
    from .verify_pin_response import VerifyPinResponse
    from .version_info_type import VersionInfoType
    from .xhtml_node import XhtmlNode
    from .xhtml_node_list import XhtmlNodeList
    from .xml_gregorian_calendar import XmlGregorianCalendar
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "AddressUse": ".address_use",
    "Base64BinaryType": ".base64binary_type",
    "BaseCalendar": ".base_calendar",
    "BaseDateTimeType": ".base_date_time_type",
    "BooleanType": ".boolean_type",
    "Bundle": ".bundle",
    "BundleEntryComponent": ".bundle_entry_component",
    "BundleEntryRequestComponent": ".bundle_entry_request_component",
    "BundleEntryResponseComponent": ".bundle_entry_response_component",
    "BundleEntrySearchComponent": ".bundle_entry_search_component",
    "BundleLinkComponent": ".bundle_link_component",
    "BundleType": ".bundle_type",
    "CalendarDate": ".calendar_date",
    "CanonicalType": ".canonical_type",
    "CardInfoType": ".card_info_type",
    "CardTypeType": ".card_type_type",
    "CardVersion": ".card_version",
    "Cards": ".cards",
    "ChangePinResponse": ".change_pin_response",
    "CodeType": ".code_type",
    "CodeableConcept": ".codeable_concept",
    "Coding": ".coding",
    "ComfortSignatureStatusEnum": ".comfort_signature_status_enum",
    "ContactPoint": ".contact_point",
    "ContactPointSystem": ".contact_point_system",
    "ContactPointUse": ".contact_point_use",
    "Date": ".date",
    "Date1": ".date1",
    "DateTimeType": ".date_time_type",
    "DecimalType": ".decimal_type",
    "Detail": ".detail",
    "Duration": ".duration",
    "Endpoint": ".endpoint",
    "EndpointStatus": ".endpoint_status",
    "EnumFactoryAddressType": ".enum_factory_address_type",
    "EnumFactoryAddressUse": ".enum_factory_address_use",
    "EnumFactoryBundleType": ".enum_factory_bundle_type",
    "EnumFactoryContactPointSystem": ".enum_factory_contact_point_system",
    "EnumFactoryContactPointUse": ".enum_factory_contact_point_use",
    "EnumFactoryEndpointStatus": ".enum_factory_endpoint_status",
    "EnumFactoryHttpVerb": ".enum_factory_http_verb",
    "EnumFactoryIdentifierUse": ".enum_factory_identifier_use",
    "EnumFactoryNameUse": ".enum_factory_name_use",
    "EnumFactoryNarrativeStatus": ".enum_factory_narrative_status",
    "EnumFactorySearchEntryMode": ".enum_factory_search_entry_mode",
    "EnumerationAddressType": ".enumeration_address_type",
    "EnumerationAddressUse": ".enumeration_address_use",
    "EnumerationBundleType": ".enumeration_bundle_type",
    "EnumerationContactPointSystem": ".enumeration_contact_point_system",
    "EnumerationContactPointUse": ".enumeration_contact_point_use",
    "EnumerationEndpointStatus": ".enumeration_endpoint_status",
    "EnumerationHttpVerb": ".enumeration_http_verb",
    "EnumerationIdentifierUse": ".enumeration_identifier_use",
    "EnumerationNameUse": ".enumeration_name_use",
    "EnumerationNarrativeStatus": ".enumeration_narrative_status",
    "EnumerationSearchEntryMode": ".enumeration_search_entry_mode",
    "Era": ".era",
    "Error": ".error",
    "Extension": ".extension",
    "FhirVersionEnum": ".fhir_version_enum",
    "GetCardsResponse": ".get_cards_response",
    "GetPinStatusResponse": ".get_pin_status_response",
    "GetSignatureModeResponseEvent": ".get_signature_mode_response_event",
    "GregorianCalendar": ".gregorian_calendar",
    "HttpVerb": ".http_verb",
    "HumanName": ".human_name",
    "IBaseCoding": ".i_base_coding",
    "IBaseDatatype": ".i_base_datatype",
    "IBaseExtensionObjectObject": ".i_base_extension_object_object",
    "IBaseMetaType": ".i_base_meta_type",
    "IIdType": ".i_id_type",
    "IPrimitiveTypeObject": ".i_primitive_type_object",
    "IPrimitiveTypeString": ".i_primitive_type_string",
    "IdType": ".id_type",
    "Identifier": ".identifier",
    "IdentifierUse": ".identifier_use",
    "InstantType": ".instant_type",
    "JsonValue": ".json_value",
    "Locale": ".locale",
    "Location": ".location",
    "Meta": ".meta",
    "NameUse": ".name_use",
    "Narrative": ".narrative",
    "NarrativeStatus": ".narrative_status",
    "NodeType": ".node_type",
    "Organization": ".organization",
    "OrganizationContactComponent": ".organization_contact_component",
    "Period": ".period",
    "PinResultEnum": ".pin_result_enum",
    "PinStatusEnum": ".pin_status_enum",
    "PositiveIntType": ".positive_int_type",
    "QName": ".q_name",
    "Reference": ".reference",
    "Resource": ".resource",
    "ResourceType": ".resource_type",
    "SearchEntryMode": ".search_entry_mode",
    "SessionInfo": ".session_info",
    "Signature": ".signature",
    "SignatureModeEnum": ".signature_mode_enum",
    "Status": ".status",
    "StringType": ".string_type",
    "TemporalPrecisionEnum": ".temporal_precision_enum",
    "TimeZone": ".time_zone",
    "Trace": ".trace",
    "Type": ".type",
    "UnblockPinResponse": ".unblock_pin_response",
    "UnsignedIntType": ".unsigned_int_type",
    "UriType": ".uri_type",
    "UrlType": ".url_type",
    "ValueType": ".value_type",
    "VerifyPinResponse": ".verify_pin_response",
    "VersionInfoType": ".version_info_type",
    "XhtmlNode": ".xhtml_node",
    "XhtmlNodeList": ".xhtml_node_list",
    "XmlGregorianCalendar": ".xml_gregorian_calendar",
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
    "Address",
    "AddressType",
    "AddressUse",
    "Base64BinaryType",
    "BaseCalendar",
    "BaseDateTimeType",
    "BooleanType",
    "Bundle",
    "BundleEntryComponent",
    "BundleEntryRequestComponent",
    "BundleEntryResponseComponent",
    "BundleEntrySearchComponent",
    "BundleLinkComponent",
    "BundleType",
    "CalendarDate",
    "CanonicalType",
    "CardInfoType",
    "CardTypeType",
    "CardVersion",
    "Cards",
    "ChangePinResponse",
    "CodeType",
    "CodeableConcept",
    "Coding",
    "ComfortSignatureStatusEnum",
    "ContactPoint",
    "ContactPointSystem",
    "ContactPointUse",
    "Date",
    "Date1",
    "DateTimeType",
    "DecimalType",
    "Detail",
    "Duration",
    "Endpoint",
    "EndpointStatus",
    "EnumFactoryAddressType",
    "EnumFactoryAddressUse",
    "EnumFactoryBundleType",
    "EnumFactoryContactPointSystem",
    "EnumFactoryContactPointUse",
    "EnumFactoryEndpointStatus",
    "EnumFactoryHttpVerb",
    "EnumFactoryIdentifierUse",
    "EnumFactoryNameUse",
    "EnumFactoryNarrativeStatus",
    "EnumFactorySearchEntryMode",
    "EnumerationAddressType",
    "EnumerationAddressUse",
    "EnumerationBundleType",
    "EnumerationContactPointSystem",
    "EnumerationContactPointUse",
    "EnumerationEndpointStatus",
    "EnumerationHttpVerb",
    "EnumerationIdentifierUse",
    "EnumerationNameUse",
    "EnumerationNarrativeStatus",
    "EnumerationSearchEntryMode",
    "Era",
    "Error",
    "Extension",
    "FhirVersionEnum",
    "GetCardsResponse",
    "GetPinStatusResponse",
    "GetSignatureModeResponseEvent",
    "GregorianCalendar",
    "HttpVerb",
    "HumanName",
    "IBaseCoding",
    "IBaseDatatype",
    "IBaseExtensionObjectObject",
    "IBaseMetaType",
    "IIdType",
    "IPrimitiveTypeObject",
    "IPrimitiveTypeString",
    "IdType",
    "Identifier",
    "IdentifierUse",
    "InstantType",
    "JsonValue",
    "Locale",
    "Location",
    "Meta",
    "NameUse",
    "Narrative",
    "NarrativeStatus",
    "NodeType",
    "Organization",
    "OrganizationContactComponent",
    "Period",
    "PinResultEnum",
    "PinStatusEnum",
    "PositiveIntType",
    "QName",
    "Reference",
    "Resource",
    "ResourceType",
    "SearchEntryMode",
    "SessionInfo",
    "Signature",
    "SignatureModeEnum",
    "Status",
    "StringType",
    "TemporalPrecisionEnum",
    "TimeZone",
    "Trace",
    "Type",
    "UnblockPinResponse",
    "UnsignedIntType",
    "UriType",
    "UrlType",
    "ValueType",
    "VerifyPinResponse",
    "VersionInfoType",
    "XhtmlNode",
    "XhtmlNodeList",
    "XmlGregorianCalendar",
]
