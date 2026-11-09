



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_profile_request import CreateProfileRequest
    from .create_profile_request_role import CreateProfileRequestRole
    from .mutation_nullable_response import MutationNullableResponse
    from .mutation_pattern_payload_region import MutationPatternPayloadRegion
    from .mutation_strict_object_payload_profile import MutationStrictObjectPayloadProfile
    from .mutation_strict_object_payload_profile_source import MutationStrictObjectPayloadProfileSource
    from .mutation_union_payload import MutationUnionPayload
    from .mutation_union_payload_contact_kind import MutationUnionPayloadContactKind
    from .ok_response import OkResponse
    from .prepare_upload_meta_request_content_type import PrepareUploadMetaRequestContentType
    from .profile_response import ProfileResponse
    from .profile_response_role import ProfileResponseRole
    from .profile_summary import ProfileSummary
    from .profile_summary_role import ProfileSummaryRole
    from .ref_parameter_candidate_request_locale import RefParameterCandidateRequestLocale
    from .search_profiles_response import SearchProfilesResponse
    from .union_candidate_request import UnionCandidateRequest
    from .update_preferences_form import UpdatePreferencesForm
    from .update_preferences_form_theme import UpdatePreferencesFormTheme
    from .update_preferences_request_theme import UpdatePreferencesRequestTheme
    from .upload_meta_form import UploadMetaForm
    from .upload_meta_form_content_type import UploadMetaFormContentType
    from .upload_meta_response import UploadMetaResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateProfileRequest": ".create_profile_request",
    "CreateProfileRequestRole": ".create_profile_request_role",
    "MutationNullableResponse": ".mutation_nullable_response",
    "MutationPatternPayloadRegion": ".mutation_pattern_payload_region",
    "MutationStrictObjectPayloadProfile": ".mutation_strict_object_payload_profile",
    "MutationStrictObjectPayloadProfileSource": ".mutation_strict_object_payload_profile_source",
    "MutationUnionPayload": ".mutation_union_payload",
    "MutationUnionPayloadContactKind": ".mutation_union_payload_contact_kind",
    "OkResponse": ".ok_response",
    "PrepareUploadMetaRequestContentType": ".prepare_upload_meta_request_content_type",
    "ProfileResponse": ".profile_response",
    "ProfileResponseRole": ".profile_response_role",
    "ProfileSummary": ".profile_summary",
    "ProfileSummaryRole": ".profile_summary_role",
    "RefParameterCandidateRequestLocale": ".ref_parameter_candidate_request_locale",
    "SearchProfilesResponse": ".search_profiles_response",
    "UnionCandidateRequest": ".union_candidate_request",
    "UpdatePreferencesForm": ".update_preferences_form",
    "UpdatePreferencesFormTheme": ".update_preferences_form_theme",
    "UpdatePreferencesRequestTheme": ".update_preferences_request_theme",
    "UploadMetaForm": ".upload_meta_form",
    "UploadMetaFormContentType": ".upload_meta_form_content_type",
    "UploadMetaResponse": ".upload_meta_response",
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
    "CreateProfileRequest",
    "CreateProfileRequestRole",
    "MutationNullableResponse",
    "MutationPatternPayloadRegion",
    "MutationStrictObjectPayloadProfile",
    "MutationStrictObjectPayloadProfileSource",
    "MutationUnionPayload",
    "MutationUnionPayloadContactKind",
    "OkResponse",
    "PrepareUploadMetaRequestContentType",
    "ProfileResponse",
    "ProfileResponseRole",
    "ProfileSummary",
    "ProfileSummaryRole",
    "RefParameterCandidateRequestLocale",
    "SearchProfilesResponse",
    "UnionCandidateRequest",
    "UpdatePreferencesForm",
    "UpdatePreferencesFormTheme",
    "UpdatePreferencesRequestTheme",
    "UploadMetaForm",
    "UploadMetaFormContentType",
    "UploadMetaResponse",
]
