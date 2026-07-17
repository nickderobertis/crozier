



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateByocTrunkRequestStatusCallbackMethod,
        CreateByocTrunkRequestVoiceFallbackMethod,
        CreateByocTrunkRequestVoiceMethod,
        ListByocTrunkResponse,
        ListByocTrunkResponseMeta,
        ListConnectionPolicyResponse,
        ListConnectionPolicyResponseMeta,
        ListConnectionPolicyTargetResponse,
        ListConnectionPolicyTargetResponseMeta,
        ListDialingPermissionsCountryResponse,
        ListDialingPermissionsCountryResponseMeta,
        ListDialingPermissionsHrsPrefixesResponse,
        ListDialingPermissionsHrsPrefixesResponseMeta,
        ListIpRecordResponse,
        ListIpRecordResponseMeta,
        ListSourceIpMappingResponse,
        ListSourceIpMappingResponseMeta,
        UpdateByocTrunkRequestStatusCallbackMethod,
        UpdateByocTrunkRequestVoiceFallbackMethod,
        UpdateByocTrunkRequestVoiceMethod,
        VoiceV1ArchivedCall,
        VoiceV1ByocTrunk,
        VoiceV1ByocTrunkStatusCallbackMethod,
        VoiceV1ByocTrunkVoiceFallbackMethod,
        VoiceV1ByocTrunkVoiceMethod,
        VoiceV1ConnectionPolicy,
        VoiceV1ConnectionPolicyConnectionPolicyTarget,
        VoiceV1DialingPermissions,
        VoiceV1DialingPermissionsDialingPermissionsCountry,
        VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate,
        VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes,
        VoiceV1DialingPermissionsDialingPermissionsCountryInstance,
        VoiceV1DialingPermissionsDialingPermissionsSettings,
        VoiceV1IpRecord,
        VoiceV1SourceIpMapping,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CreateByocTrunkRequestStatusCallbackMethod": ".types",
    "CreateByocTrunkRequestVoiceFallbackMethod": ".types",
    "CreateByocTrunkRequestVoiceMethod": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ListByocTrunkResponse": ".types",
    "ListByocTrunkResponseMeta": ".types",
    "ListConnectionPolicyResponse": ".types",
    "ListConnectionPolicyResponseMeta": ".types",
    "ListConnectionPolicyTargetResponse": ".types",
    "ListConnectionPolicyTargetResponseMeta": ".types",
    "ListDialingPermissionsCountryResponse": ".types",
    "ListDialingPermissionsCountryResponseMeta": ".types",
    "ListDialingPermissionsHrsPrefixesResponse": ".types",
    "ListDialingPermissionsHrsPrefixesResponseMeta": ".types",
    "ListIpRecordResponse": ".types",
    "ListIpRecordResponseMeta": ".types",
    "ListSourceIpMappingResponse": ".types",
    "ListSourceIpMappingResponseMeta": ".types",
    "UpdateByocTrunkRequestStatusCallbackMethod": ".types",
    "UpdateByocTrunkRequestVoiceFallbackMethod": ".types",
    "UpdateByocTrunkRequestVoiceMethod": ".types",
    "VoiceV1ArchivedCall": ".types",
    "VoiceV1ByocTrunk": ".types",
    "VoiceV1ByocTrunkStatusCallbackMethod": ".types",
    "VoiceV1ByocTrunkVoiceFallbackMethod": ".types",
    "VoiceV1ByocTrunkVoiceMethod": ".types",
    "VoiceV1ConnectionPolicy": ".types",
    "VoiceV1ConnectionPolicyConnectionPolicyTarget": ".types",
    "VoiceV1DialingPermissions": ".types",
    "VoiceV1DialingPermissionsDialingPermissionsCountry": ".types",
    "VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate": ".types",
    "VoiceV1DialingPermissionsDialingPermissionsCountryDialingPermissionsHrsPrefixes": ".types",
    "VoiceV1DialingPermissionsDialingPermissionsCountryInstance": ".types",
    "VoiceV1DialingPermissionsDialingPermissionsSettings": ".types",
    "VoiceV1IpRecord": ".types",
    "VoiceV1SourceIpMapping": ".types",
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
    "AsyncFernApi",
    "CreateByocTrunkRequestStatusCallbackMethod",
    "CreateByocTrunkRequestVoiceFallbackMethod",
    "CreateByocTrunkRequestVoiceMethod",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
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
    "__version__",
]
