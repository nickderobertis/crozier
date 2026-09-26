



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_code_playground_response import AddCodePlaygroundResponse
    from .add_linkifier_response import AddLinkifierResponse
    from .add_realm_domain_response import AddRealmDomainResponse
    from .add_realm_domain_response_new_domain_item import AddRealmDomainResponseNewDomainItem
    from .create_custom_profile_field_response import CreateCustomProfileFieldResponse
    from .export_realm_request_export_type import ExportRealmRequestExportType
    from .export_realm_response import ExportRealmResponse
    from .get_custom_emoji_response import GetCustomEmojiResponse
    from .get_custom_profile_fields_response import GetCustomProfileFieldsResponse
    from .get_linkifiers_response import GetLinkifiersResponse
    from .get_linkifiers_response_linkifiers_item import GetLinkifiersResponseLinkifiersItem
    from .get_presence_response import GetPresenceResponse
    from .get_realm_domains_response import GetRealmDomainsResponse
    from .get_realm_export_consents_response import GetRealmExportConsentsResponse
    from .get_realm_export_consents_response_export_consents_item import (
        GetRealmExportConsentsResponseExportConsentsItem,
    )
    from .get_realm_exports_response import GetRealmExportsResponse
    from .get_server_settings_response import GetServerSettingsResponse
    from .get_server_settings_response_authentication_methods import GetServerSettingsResponseAuthenticationMethods
    from .get_server_settings_response_external_authentication_methods_item import (
        GetServerSettingsResponseExternalAuthenticationMethodsItem,
    )
    from .test_welcome_bot_custom_message_response import TestWelcomeBotCustomMessageResponse
    from .update_realm_user_settings_defaults_request_resolved_topic_notice_auto_read_policy import (
        UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy,
    )
    from .update_realm_user_settings_defaults_request_web_animate_image_previews import (
        UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AddCodePlaygroundResponse": ".add_code_playground_response",
    "AddLinkifierResponse": ".add_linkifier_response",
    "AddRealmDomainResponse": ".add_realm_domain_response",
    "AddRealmDomainResponseNewDomainItem": ".add_realm_domain_response_new_domain_item",
    "CreateCustomProfileFieldResponse": ".create_custom_profile_field_response",
    "ExportRealmRequestExportType": ".export_realm_request_export_type",
    "ExportRealmResponse": ".export_realm_response",
    "GetCustomEmojiResponse": ".get_custom_emoji_response",
    "GetCustomProfileFieldsResponse": ".get_custom_profile_fields_response",
    "GetLinkifiersResponse": ".get_linkifiers_response",
    "GetLinkifiersResponseLinkifiersItem": ".get_linkifiers_response_linkifiers_item",
    "GetPresenceResponse": ".get_presence_response",
    "GetRealmDomainsResponse": ".get_realm_domains_response",
    "GetRealmExportConsentsResponse": ".get_realm_export_consents_response",
    "GetRealmExportConsentsResponseExportConsentsItem": ".get_realm_export_consents_response_export_consents_item",
    "GetRealmExportsResponse": ".get_realm_exports_response",
    "GetServerSettingsResponse": ".get_server_settings_response",
    "GetServerSettingsResponseAuthenticationMethods": ".get_server_settings_response_authentication_methods",
    "GetServerSettingsResponseExternalAuthenticationMethodsItem": ".get_server_settings_response_external_authentication_methods_item",
    "TestWelcomeBotCustomMessageResponse": ".test_welcome_bot_custom_message_response",
    "UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy": ".update_realm_user_settings_defaults_request_resolved_topic_notice_auto_read_policy",
    "UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews": ".update_realm_user_settings_defaults_request_web_animate_image_previews",
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
    "AddCodePlaygroundResponse",
    "AddLinkifierResponse",
    "AddRealmDomainResponse",
    "AddRealmDomainResponseNewDomainItem",
    "CreateCustomProfileFieldResponse",
    "ExportRealmRequestExportType",
    "ExportRealmResponse",
    "GetCustomEmojiResponse",
    "GetCustomProfileFieldsResponse",
    "GetLinkifiersResponse",
    "GetLinkifiersResponseLinkifiersItem",
    "GetPresenceResponse",
    "GetRealmDomainsResponse",
    "GetRealmExportConsentsResponse",
    "GetRealmExportConsentsResponseExportConsentsItem",
    "GetRealmExportsResponse",
    "GetServerSettingsResponse",
    "GetServerSettingsResponseAuthenticationMethods",
    "GetServerSettingsResponseExternalAuthenticationMethodsItem",
    "TestWelcomeBotCustomMessageResponse",
    "UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy",
    "UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews",
]
