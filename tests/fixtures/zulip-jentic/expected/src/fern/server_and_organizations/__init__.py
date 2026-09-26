



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AddCodePlaygroundResponse,
        AddLinkifierResponse,
        CreateCustomProfileFieldResponse,
        ExportRealmRequestExportType,
        ExportRealmResponse,
        GetCustomEmojiResponse,
        GetCustomProfileFieldsResponse,
        GetLinkifiersResponse,
        GetLinkifiersResponseLinkifiersItem,
        GetPresenceResponse,
        GetRealmExportConsentsResponse,
        GetRealmExportConsentsResponseExportConsentsItem,
        GetRealmExportsResponse,
        GetServerSettingsResponse,
        GetServerSettingsResponseAuthenticationMethods,
        GetServerSettingsResponseExternalAuthenticationMethodsItem,
        TestWelcomeBotCustomMessageResponse,
        UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy,
        UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AddCodePlaygroundResponse": ".types",
    "AddLinkifierResponse": ".types",
    "CreateCustomProfileFieldResponse": ".types",
    "ExportRealmRequestExportType": ".types",
    "ExportRealmResponse": ".types",
    "GetCustomEmojiResponse": ".types",
    "GetCustomProfileFieldsResponse": ".types",
    "GetLinkifiersResponse": ".types",
    "GetLinkifiersResponseLinkifiersItem": ".types",
    "GetPresenceResponse": ".types",
    "GetRealmExportConsentsResponse": ".types",
    "GetRealmExportConsentsResponseExportConsentsItem": ".types",
    "GetRealmExportsResponse": ".types",
    "GetServerSettingsResponse": ".types",
    "GetServerSettingsResponseAuthenticationMethods": ".types",
    "GetServerSettingsResponseExternalAuthenticationMethodsItem": ".types",
    "TestWelcomeBotCustomMessageResponse": ".types",
    "UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy": ".types",
    "UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews": ".types",
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
    "CreateCustomProfileFieldResponse",
    "ExportRealmRequestExportType",
    "ExportRealmResponse",
    "GetCustomEmojiResponse",
    "GetCustomProfileFieldsResponse",
    "GetLinkifiersResponse",
    "GetLinkifiersResponseLinkifiersItem",
    "GetPresenceResponse",
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
