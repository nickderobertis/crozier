



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_byoc_trunk_request_status_callback_method import CreateByocTrunkRequestStatusCallbackMethod
    from .create_byoc_trunk_request_voice_fallback_method import CreateByocTrunkRequestVoiceFallbackMethod
    from .create_byoc_trunk_request_voice_method import CreateByocTrunkRequestVoiceMethod
    from .list_byoc_trunk_response import ListByocTrunkResponse
    from .list_byoc_trunk_response_meta import ListByocTrunkResponseMeta
    from .list_connection_policy_response import ListConnectionPolicyResponse
    from .list_connection_policy_response_meta import ListConnectionPolicyResponseMeta
    from .list_connection_policy_target_response import ListConnectionPolicyTargetResponse
    from .list_connection_policy_target_response_meta import ListConnectionPolicyTargetResponseMeta
    from .list_dialing_permissions_country_response import ListDialingPermissionsCountryResponse
    from .list_dialing_permissions_country_response_meta import ListDialingPermissionsCountryResponseMeta
    from .list_dialing_permissions_hrs_prefixes_response import ListDialingPermissionsHrsPrefixesResponse
    from .list_dialing_permissions_hrs_prefixes_response_meta import ListDialingPermissionsHrsPrefixesResponseMeta
    from .list_ip_record_response import ListIpRecordResponse
    from .list_ip_record_response_meta import ListIpRecordResponseMeta
    from .list_source_ip_mapping_response import ListSourceIpMappingResponse
    from .list_source_ip_mapping_response_meta import ListSourceIpMappingResponseMeta
    from .update_byoc_trunk_request_status_callback_method import UpdateByocTrunkRequestStatusCallbackMethod
    from .update_byoc_trunk_request_voice_fallback_method import UpdateByocTrunkRequestVoiceFallbackMethod
    from .update_byoc_trunk_request_voice_method import UpdateByocTrunkRequestVoiceMethod
    from .voice_v1archived_call import VoiceV1ArchivedCall
    from .voice_v1byoc_trunk import VoiceV1ByocTrunk
    from .voice_v1byoc_trunk_status_callback_method import VoiceV1ByocTrunkStatusCallbackMethod
    from .voice_v1byoc_trunk_voice_fallback_method import VoiceV1ByocTrunkVoiceFallbackMethod
    from .voice_v1byoc_trunk_voice_method import VoiceV1ByocTrunkVoiceMethod
    from .voice_v1connection_policy import VoiceV1ConnectionPolicy
    from .voice_v1connection_policy_connection_policy_target import VoiceV1ConnectionPolicyConnectionPolicyTarget
    from .voice_v1dialing_permissions import VoiceV1DialingPermissions
    from .voice_v1dialing_permissions_dialing_permissions_country import (
        VoiceV1DialingPermissionsDialingPermissionsCountry,
    )
    from .voice_v1dialing_permissions_dialing_permissions_country_bulk_update import (
        VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
    )
    from .voice_v1dialing_permissions_dialing_permissions_country_dialing_permissions_hrs_prefixes import (
        VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes,
    )
    from .voice_v1dialing_permissions_dialing_permissions_country_instance import (
        VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
    )
    from .voice_v1dialing_permissions_dialing_permissions_settings import (
        VoiceV1DialingPermissionsDialingPermissionsSettings,
    )
    from .voice_v1ip_record import VoiceV1IpRecord
    from .voice_v1source_ip_mapping import VoiceV1SourceIpMapping
_dynamic_imports: typing.Dict[str, str] = {
    "CreateByocTrunkRequestStatusCallbackMethod": ".create_byoc_trunk_request_status_callback_method",
    "CreateByocTrunkRequestVoiceFallbackMethod": ".create_byoc_trunk_request_voice_fallback_method",
    "CreateByocTrunkRequestVoiceMethod": ".create_byoc_trunk_request_voice_method",
    "ListByocTrunkResponse": ".list_byoc_trunk_response",
    "ListByocTrunkResponseMeta": ".list_byoc_trunk_response_meta",
    "ListConnectionPolicyResponse": ".list_connection_policy_response",
    "ListConnectionPolicyResponseMeta": ".list_connection_policy_response_meta",
    "ListConnectionPolicyTargetResponse": ".list_connection_policy_target_response",
    "ListConnectionPolicyTargetResponseMeta": ".list_connection_policy_target_response_meta",
    "ListDialingPermissionsCountryResponse": ".list_dialing_permissions_country_response",
    "ListDialingPermissionsCountryResponseMeta": ".list_dialing_permissions_country_response_meta",
    "ListDialingPermissionsHrsPrefixesResponse": ".list_dialing_permissions_hrs_prefixes_response",
    "ListDialingPermissionsHrsPrefixesResponseMeta": ".list_dialing_permissions_hrs_prefixes_response_meta",
    "ListIpRecordResponse": ".list_ip_record_response",
    "ListIpRecordResponseMeta": ".list_ip_record_response_meta",
    "ListSourceIpMappingResponse": ".list_source_ip_mapping_response",
    "ListSourceIpMappingResponseMeta": ".list_source_ip_mapping_response_meta",
    "UpdateByocTrunkRequestStatusCallbackMethod": ".update_byoc_trunk_request_status_callback_method",
    "UpdateByocTrunkRequestVoiceFallbackMethod": ".update_byoc_trunk_request_voice_fallback_method",
    "UpdateByocTrunkRequestVoiceMethod": ".update_byoc_trunk_request_voice_method",
    "VoiceV1ArchivedCall": ".voice_v1archived_call",
    "VoiceV1ByocTrunk": ".voice_v1byoc_trunk",
    "VoiceV1ByocTrunkStatusCallbackMethod": ".voice_v1byoc_trunk_status_callback_method",
    "VoiceV1ByocTrunkVoiceFallbackMethod": ".voice_v1byoc_trunk_voice_fallback_method",
    "VoiceV1ByocTrunkVoiceMethod": ".voice_v1byoc_trunk_voice_method",
    "VoiceV1ConnectionPolicy": ".voice_v1connection_policy",
    "VoiceV1ConnectionPolicyConnectionPolicyTarget": ".voice_v1connection_policy_connection_policy_target",
    "VoiceV1DialingPermissions": ".voice_v1dialing_permissions",
    "VoiceV1DialingPermissionsDialingPermissionsCountry": ".voice_v1dialing_permissions_dialing_permissions_country",
    "VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate": ".voice_v1dialing_permissions_dialing_permissions_country_bulk_update",
    "VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes": ".voice_v1dialing_permissions_dialing_permissions_country_dialing_permissions_hrs_prefixes",
    "VoiceV1DialingPermissionsDialingPermissionsCountryInstance": ".voice_v1dialing_permissions_dialing_permissions_country_instance",
    "VoiceV1DialingPermissionsDialingPermissionsSettings": ".voice_v1dialing_permissions_dialing_permissions_settings",
    "VoiceV1IpRecord": ".voice_v1ip_record",
    "VoiceV1SourceIpMapping": ".voice_v1source_ip_mapping",
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
    "CreateByocTrunkRequestStatusCallbackMethod",
    "CreateByocTrunkRequestVoiceFallbackMethod",
    "CreateByocTrunkRequestVoiceMethod",
    "ListByocTrunkResponse",
    "ListByocTrunkResponseMeta",
    "ListConnectionPolicyResponse",
    "ListConnectionPolicyResponseMeta",
    "ListConnectionPolicyTargetResponse",
    "ListConnectionPolicyTargetResponseMeta",
    "ListDialingPermissionsCountryResponse",
    "ListDialingPermissionsCountryResponseMeta",
    "ListDialingPermissionsHrsPrefixesResponse",
    "ListDialingPermissionsHrsPrefixesResponseMeta",
    "ListIpRecordResponse",
    "ListIpRecordResponseMeta",
    "ListSourceIpMappingResponse",
    "ListSourceIpMappingResponseMeta",
    "UpdateByocTrunkRequestStatusCallbackMethod",
    "UpdateByocTrunkRequestVoiceFallbackMethod",
    "UpdateByocTrunkRequestVoiceMethod",
    "VoiceV1ArchivedCall",
    "VoiceV1ByocTrunk",
    "VoiceV1ByocTrunkStatusCallbackMethod",
    "VoiceV1ByocTrunkVoiceFallbackMethod",
    "VoiceV1ByocTrunkVoiceMethod",
    "VoiceV1ConnectionPolicy",
    "VoiceV1ConnectionPolicyConnectionPolicyTarget",
    "VoiceV1DialingPermissions",
    "VoiceV1DialingPermissionsDialingPermissionsCountry",
    "VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate",
    "VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes",
    "VoiceV1DialingPermissionsDialingPermissionsCountryInstance",
    "VoiceV1DialingPermissionsDialingPermissionsSettings",
    "VoiceV1IpRecord",
    "VoiceV1SourceIpMapping",
]
